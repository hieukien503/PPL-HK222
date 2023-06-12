from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Utils import *
from CodeGenError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [[Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()), CName(self.libName)),
                Symbol("printFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType(list(), StringType()), CName(self.libName)),
                Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("readBoolean", MType(list(), BooleanType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
                ]]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)

class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "Class({0})".format(str(self.name))

class ClassDecl(Decl):
    def __init__(self, name, memlist: List[VarDecl]):
        self.name = name
        self.memlist = memlist

class CodeGenVisitor(Visitor, Utils):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = 'MT22Class'
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.stage = 0
        self.has_return = False
        self.has_break = False
        self.arr_type = None
        self.lhs_type = None
        self.inherit_func = None
        self.func_lst = []
        self.passed = []
        self.var_name = None
        self.clinit = None
        self.classEnv = []
        self.func = None
    
    def update(self, name, typ_, o):
        # name: name of function with type auto
        # typ_: Type to change
        # o: Any
        for x in range(len(o.sym[-1])):
            if o.sym[-1][x].name == name:
                o.sym[-1][x].mtype.rettype = typ_
                break
    
    def defaultValue(self, typ_):
        varType = type(typ_)
        if varType is IntegerType:
            return IntegerLit(0)
        elif varType is FloatType:
            return FloatLit(0.0)
        elif varType is StringType:
            return StringLit("")
        elif varType is BooleanType:
            return BooleanLit(False)
        else:
            expr = []
            if len(typ_.dimensions) == 1:
                for x in range(typ_.dimensions[0]):
                    expr += [self.defaultValue(typ_.typ)]
                return ArrayLit(expr)
            else:
                dimen = typ_.dimensions
                for x in range(dimen[0]):
                    temp = self.defaultValue(ArrayType(dimen[1:], typ_.typ))
                    expr += [temp]
                return ArrayLit(expr)

    def visitProgram(self, ast, c):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        vardecl_has_init = []
        var_decl_lst = []
        flag = []
        for x in ast.decls:
            if type(x) is FuncDecl:
                e.sym[0] += [Symbol(x.name, MType(list(map(lambda y: y.typ, x.params)), x.return_type), CName(self.className))]
                self.func_lst = [x] + self.func_lst if x.name != 'main' else self.func_lst + [x]
                flag += [False]
            else:
                if x.init is not None:
                    vardecl_has_init += [AssignStmt(Id(x.name), x.init)]
                elif x.init is None and type(x.typ) is ArrayType:
                    vardecl_has_init += [x]
                var_decl_lst += [x]
        
        for x in range(len(self.func_lst)):
            for y in range(len(self.func_lst)):
                if (self.func_lst[x].inherit == self.func_lst[y].name) and (flag[x] == False and flag[y] == False) and x < y:
                    self.func_lst[x], self.func_lst[y] = self.func_lst[y], self.func_lst[x]
                    flag[x], flag[y] = True, True

        for x in var_decl_lst:
            e.sym[0] += [self.visit(x, e)]
        
        self.genMETHOD(FuncDecl("<init>", VoidType(), [], "", BlockStmt([])), e, Frame("<init>", VoidType))
        self.func_lst.reverse()
        t = self.func_lst.pop(0)
        self.func_lst.append(t)
        for x in self.func_lst:
            out_var_lst = []
            for y in x.params:
                if y.out == True:
                    if type(y.typ) is not AutoType:
                        out_var_lst += [VarDecl(y.name, y.typ)]
                    else:
                        out_var_lst = []
                        break
            if out_var_lst != []:
                if x.name == 'swap':
                    self.visitClassDecl(ClassDecl('Swap', out_var_lst), e)
                else:
                    self.visitClassDecl(ClassDecl(x.name, out_var_lst), e)
                self.className = 'MT22Class'

        for x in self.func_lst:
            self.visit(x, e)
        
        for x in self.passed:
            self.visit(x, e)
        
        if vardecl_has_init != []:
            self.clinit = "<clinit>"
            self.genMETHOD(FuncDecl("<clinit>", VoidType(), [], "", BlockStmt(vardecl_has_init)), e, Frame("<clinit>", VoidType))
            self.clinit = None
        self.emit.emitEPILOG()
        return c
    
    def visitClassDecl(self, ast, o):
        self.className = ast.name
        emitter = self.emit
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java/lang/Object"))
        attrSym = []
        attrSym = [self.visit(x, o) for x in ast.memlist]
        self.classEnv += [(ast.name, attrSym)]
        self.genMETHOD(FuncDecl("<init>", VoidType(), [], "", BlockStmt([])), o, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        self.emit = emitter


    def genMETHOD(self, ast, o, frame):
        for x in ast.params:
            if type(x.typ) is AutoType:
                return None
        self.has_return = False
        isInit = ast.name == "<init>"
        isMain = (ast.name == "main" and len(ast.params) == 0 and type(ast.return_type) is VoidType)
        returnType = ast.return_type if type(ast.return_type) is not AutoType or self.lhs_type is None else self.lhs_type
        methodName = ast.name
        intype = [ArrayType([], StringType())] if isMain else list(map(lambda x: x.typ, ast.params))

        if type(returnType) is AutoType:
            o.sym = [[]] + o.sym
            for x in ast.params:
                o.sym[0] += [Symbol(x.name, x.typ, Index(frame.getNewIndex()))]
            frame.setCurrIndex(0)
            for x in ast.body.body:
                if type(x) is ReturnStmt and x.expr is not None:
                    code, typ = self.visit(x.expr, Access(frame, o.sym, False, True))
                    returnType = typ
                    break
                elif type(x) is ReturnStmt and x.expr is None:
                    returnType = VoidType()
                    break
            o.sym = o.sym[1:]

        self.update(ast.name, returnType, o)
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o.sym
        parent_param = []
                    

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            if ast.inherit is not None:
                self.inherit_func = ast.inherit
                for x in self.func_lst:
                    if x.name == self.inherit_func:
                        for y in x.params:
                            if y.inherit == True and (type(ast.body.body[0]) is CallStmt and ast.body.body[0].name == "super"):
                                parent_param += [self.visit(y, SubBody(frame, glenv))]
                        break
            glenv = [parent_param] + glenv
        else:
            local = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)] + env.sym), ast.params, SubBody(frame, []))
            if ast.inherit is not None:
                self.inherit_func = ast.inherit
                for x in self.func_lst:
                    if x.name == self.inherit_func:
                        for y in x.params:
                            if y.inherit == True and (type(ast.body.body[0]) is CallStmt and ast.body.body[0].name == "super"):
                                parent_param += [self.visit(y, SubBody(frame, glenv))]
                        break
            glenv = [local.sym + parent_param] + glenv

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
       
        self.visit(ast.body, SubBody(frame, glenv))
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType and not self.has_return:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        self.func = ast.name
        frame = Frame(ast.name, ast.return_type if type(ast.return_type) is not AutoType or self.lhs_type is None else self.lhs_type)
        self.genMETHOD(ast, o, frame)

    def visitCallStmt(self, ast, o):
        if ast.name == 'preventDefault':
            return None
        func_name = ast.name if ast.name != 'super' else self.inherit_func
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym[-1]
        sym = None
        if ast.name == 'super':
            sym = next(filter(lambda x: self.inherit_func == x.name, nenv), None)
        else:
            sym = next(filter(lambda x: ast.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())

        for x in self.func_lst:
            if x.name == func_name:
                for y in range(len(x.params)):
                    if x.params[y].out == True and not isinstance(ast.args[y], (ArrayCell, Id)):
                        raise IllegalRuntimeException(str(ast.args[y]))

        real_param = []
        has_auto_param = False
        for x in range(len(ast.args)):
            if type(ast.args[x]) is FuncCall:
                for y in self.func_lst:
                    if y.name == ast.args[x].name and type(y.return_type) is AutoType:
                        self.lhs_type = ctype.partype[x]
                for y in self.passed:
                    if y.name == ast.args[x].name and type(y.return_type) is AutoType:
                        self.lhs_type = ctype.partype[x]
            str1, typ1 = self.visit(ast.args[x], Access(frame, ctxt.sym, False, True))
            if type(ctype.partype[x]) is AutoType:
                has_auto_param = True
            if type(typ1) is IntegerType and type(ctype.partype[x]) is FloatType:
                typ1 = FloatType()
                str1 = str1 + self.emit.emitI2F(frame)
            elif type(ast.args[x]) is ArrayCell:
                str1 += self.emit.emitALOAD(typ1, frame)
            real_param += [typ1]
            temp = in_[1] + [typ1]
            in_ = (in_[0] + str1, in_[1] + temp)
        
        params = []
        inherit = None
        body = None
        out_param = []
        if has_auto_param == True:
            for x in self.func_lst:
                if x.name == func_name:
                    for y in range(len(x.params)):
                        str1, typ1 = self.visit(ast.args[y], Access(frame, o.sym, False, True))
                        params += [ParamDecl(x.params[y].name, typ1, x.params[y].out, x.params[y].inherit)]
                        if x.params[y].out == True:
                            out_param += [VarDecl(x.params[y].name, typ1)]
                    inherit = x.inherit
                    body = x.body
            if out_param != []:
                if func_name == 'swap':
                    func_name = 'Swap'
                self.visitClassDecl(ClassDecl(func_name, out_param), SubBody(None, o.sym))
                self.className = 'MT22Class'
            for x in range(len(nenv)):
                if nenv[x].name == ast.name:
                    t = nenv.pop(x)
                    nenv.insert(x, Symbol(ast.name, MType(real_param, t.mtype.rettype), CName(self.className)))
                    self.passed += [FuncDecl(ast.name, t.mtype.rettype, params, inherit, body)]

        ctype = ctype if real_param == [] else MType(real_param, ctype.rettype)
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + func_name, ctype, frame))
        for x in self.func_lst:
            if x.name == func_name:
                if func_name == 'swap':
                    func_name = 'Swap'
                for y in range(len(x.params)):
                    if x.params[y].out == True:
                        self.visit(AssignStmt(ast.args[y], Id(func_name + '.' + x.params[y].name)), o)

        if ast.name == 'super':
            for x in self.func_lst:
                for y in range(len(x.params)):
                    if x.params[y].inherit == True:
                        self.visit(AssignStmt(Id(x.params[y].name), ast.args[y]), o)

    def visitIntegerLit(self, ast, o):
        if type(o) is Frame:
            return self.emit.emitPUSHICONST(ast.val, o), IntegerType()
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()
    
    def visitFloatLit(self, ast, o):
        if type(o) is Frame:
            return self.emit.emitPUSHFCONST(str(ast.val), o), FloatType()
        return self.emit.emitPUSHFCONST(str(ast.val), o.frame), FloatType()
    
    def visitStringLit(self, ast, o):
        if type(o) is Frame:
            return self.emit.emitPUSHCONST("\"" + ast.val + "\"", StringType(), o), StringType()
        return self.emit.emitPUSHCONST("\"" + ast.val + "\"", StringType(), o.frame), StringType()

    def visitBooleanLit(self, ast, o):
        if type(o) is Frame:
            return self.emit.emitPUSHICONST(str(ast.val).lower(), o), BooleanType()
        return self.emit.emitPUSHICONST(str(ast.val).lower(), o.frame), BooleanType()

    def visitBinExpr(self, ast, o):
        if type(ast.left) is FuncCall:
            for x in self.func_lst:
                if x.name == ast.left.name and type(x.return_type) is AutoType:
                    e1c, self.lhs_type = self.visit(ast.right, o)
        
        elif type(ast.right) is FuncCall:
            for x in self.func_lst:
                if x.name == ast.right.name and type(x.return_type) is AutoType:
                    e1c, self.lhs_type = self.visit(ast.left, o)

        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        if type(e1t) is type(e2t):
            if type(e1t) is StringType:
                if type(ast.left) is StringLit and type(ast.right) is StringLit:
                    o.frame.pop()
                    o.frame.pop()
                    return self.visit(StringLit(ast.left.val + ast.right.val), o)
                else:
                    code1 = e1c + ("" if type(ast.left) is not ArrayCell else self.emit.emitALOAD(e1t, o.frame))
                    code2 = e2c + ("" if type(ast.right) is not ArrayCell else self.emit.emitALOAD(e2t, o.frame))
                    code = code1 + code2 + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()], StringType()), o.frame)
                    return code, StringType()
            else:
                code1 = e1c + ("" if type(ast.left) is not ArrayCell else self.emit.emitALOAD(e1t, o.frame))
                code2 = e2c + ("" if type(ast.right) is not ArrayCell else self.emit.emitALOAD(e2t, o.frame))
                if ast.op in ['+', '-']:
                    if isinstance(ast.left, (IntegerLit, FloatLit)) and isinstance(ast.right, (IntegerLit, FloatLit)):
                        if ast.op == '+':
                            return self.visit(IntegerLit(ast.left.val + ast.right.val), o) if type(ast.left) is IntegerLit else self.visit(FloatLit(ast.left.val + ast.right.val), o)
                        return self.visit(IntegerLit(ast.left.val - ast.right.val), o) if type(ast.left) is IntegerLit else self.visit(FloatLit(ast.left.val - ast.right.val), o)
                    return code1 + code2 + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t
                elif ast.op in ['*', '/']:
                    if isinstance(ast.left, (IntegerLit, FloatLit)) and isinstance(ast.right, (IntegerLit, FloatLit)):
                        if ast.op == '*':
                            return self.visit(IntegerLit(ast.left.val * ast.right.val), o) if type(ast.left) is IntegerLit else self.visit(FloatLit(ast.left.val * ast.right.val), o)
                        else:
                            if ast.right.val != 0:
                                return self.visit(IntegerLit(ast.left.val / ast.right.val), o) if type(ast.left) is IntegerLit else self.visit(FloatLit(ast.left.val / ast.right.val), o)
                    return code1 + code2 + self.emit.emitMULOP(ast.op, e1t, o.frame), e1t
                elif ast.op in ['<', '>', '<=', '>=', '!=', '==']:
                    return code1 + code2 + self.emit.emitREOP(ast.op, e1t, o.frame), BooleanType()
                elif ast.op == '&&':
                    label1 = o.frame.getNewLabel()
                    label2 = o.frame.getNewLabel()
                    if label1 > 2:
                        code1 = code1 + self.emit.emitIFTRUE(label1, o.frame) + self.emit.emitPUSHICONST(0, o.frame) + self.emit.emitGOTO(label2, o.frame)
                        code2 = self.emit.emitLABEL(label1, o.frame) + code2 + self.emit.emitLABEL(label2, o.frame)
                        return code1 + code2, BooleanType()
                    else:
                        code1 = code1 + self.emit.emitIFTRUE(label1, o.frame) + self.emit.emitPUSHICONST(0, o.frame) + self.emit.emitGOTO(label2, o.frame)
                        code2 = self.emit.emitLABEL(label1, o.frame) + code2 + self.emit.emitLABEL(label2, o.frame)
                        return code1 + code2, BooleanType()
                elif ast.op == '||':
                    label1 = o.frame.getNewLabel()
                    label2 = o.frame.getNewLabel()
                    if label1 > 2:
                        code1 = code1 + self.emit.emitIFFALSE(label1, o.frame) + self.emit.emitPUSHICONST(1, o.frame) + self.emit.emitGOTO(label2, o.frame)
                        code2 = self.emit.emitLABEL(label1, o.frame) + code2 + self.emit.emitLABEL(label2, o.frame)
                        return code1 + code2, BooleanType()
                    else:
                        code1 = code1 + self.emit.emitIFFALSE(label1, o.frame) + self.emit.emitPUSHICONST(1, o.frame) + self.emit.emitGOTO(label2, o.frame)
                        code2 = self.emit.emitLABEL(label1, o.frame) + code2 + self.emit.emitLABEL(label2, o.frame)
                        return code1 + code2, BooleanType()
                elif ast.op == '%':
                    return code1 + code2 + self.emit.emitMOD(o.frame), IntegerType()
        else:
            code1 = e1c + ("" if type(ast.left) is not ArrayCell else self.emit.emitALOAD(e1t, o.frame))
            code2 = e2c + ("" if type(ast.right) is not ArrayCell else self.emit.emitALOAD(e2t, o.frame))
            e1f = code1 + self.emit.emitI2F(o.frame) if type(e2t) is FloatType else code1
            e2f = code2 + self.emit.emitI2F(o.frame) if type(e1t) is FloatType else code2
            if ast.op in ['+', '-']:
                if isinstance(ast.left, (IntegerLit, FloatLit)) and isinstance(ast.right, (IntegerLit, FloatLit)):
                    if ast.op == '+':
                        return self.visit(FloatLit(ast.left.val + ast.right.val), o)
                    return self.visit(FloatLit(ast.left.val - ast.right.val), o)
                return e1f + e2f + self.emit.emitADDOP(ast.op, FloatType(), o.frame), FloatType()
            elif ast.op in ['*', '/']:
                if isinstance(ast.left, (IntegerLit, FloatLit)) and isinstance(ast.right, (IntegerLit, FloatLit)):
                    if ast.op == '*':
                        return self.visit(FloatLit(ast.left.val * ast.right.val), o)
                    else:
                        if ast.right.val != 0:
                            return self.visit(FloatLit(ast.left.val / ast.right.val), o)
                return e1f + e2f + self.emit.emitMULOP(ast.op, FloatType(), o.frame), FloatType()
            elif ast.op in ['<', '>', '<=', '>=']:
                if type(e2t) is FloatType or type(e1t) is FloatType:
                    return e1f + e2f + self.emit.emitREOP(ast.op, FloatType(), o.frame), BooleanType()
                else:
                    return e1f + e2f + self.emit.emitREOP(ast.op, IntegerType(), o.frame), BooleanType()
            elif ast.op in ['==', '!=']:
                return e1f + e2f + self.emit.emitREOP(ast.op, IntegerType(), o.frame), BooleanType()


    def visitVarDecl(self, ast, o):
        if type(ast.typ) is ArrayType:
            self.arr_type = ast.typ
        if o.frame is None:
            frame = Frame(ast.name, ast.typ)
            if ast.init is None:
                code = self.emit.emitATTRIBUTE(ast.name, ast.typ, False, CName(self.className))
                self.emit.printout(code)
                return Symbol(ast.name, ast.typ, CName(self.className))
            else:
                self.lhs_type = ast.typ
                init, rt = self.visit(ast.init, SubBody(frame, o.sym))
                init = init + self.emit.emitI2F(o.frame) if type(ast.typ) is FloatType and type(rt) is IntegerType else init
                rt = FloatType() if type(ast.typ) is FloatType else rt
                if type(rt) is AutoType:
                    self.update(ast.init.name, ast.typ, o.sym)
                    rt = ast.typ
                code = self.emit.emitATTRIBUTE(ast.name, rt, False, CName(self.className))
                self.emit.printout(code)
                return Symbol(ast.name, rt, CName(self.className))
        else:
            idx = o.frame.getNewIndex()
            if ast.init is None:
                if type(ast.typ) is ArrayType:
                    if self.clinit == "<clinit>":
                        ret_code = ""
                        if len(ast.typ.dimensions) == 1:
                            lit, typ = self.visit(IntegerLit(ast.typ.dimensions[0]), o)
                            ret_code = lit + self.emit.emitNEWARRAY(ast.typ.typ, o.frame) + self.emit.emitPUTSTATIC(self.className + "." + ast.name, ast.typ, o.frame)
                        else:
                            for x in ast.typ.dimensions:
                                lit, typ = self.visit(IntegerLit(x), o)
                                ret_code += lit
                            ret_code += self.emit.emitMULTIANEWARRAY(ast.typ, o.frame) + self.emit.emitPUTSTATIC(self.className + "." + ast.name, ast.typ, o.frame) 
                        self.emit.printout(ret_code)
                        return Symbol(ast.name, ast.typ, Index(idx))
                    else:
                        return self.visit(VarDecl(ast.name, ast.typ, self.defaultValue(ast.typ)), o)
                else:
                    return self.visit(VarDecl(ast.name, ast.typ, self.defaultValue(ast.typ)), o)
            else:
                self.lhs_type = ast.typ
                init, rt = self.visit(ast.init, Access(o.frame, o.sym, False, True))
                init = init + self.emit.emitI2F(o.frame) if type(ast.typ) is FloatType and type(rt) is IntegerType else init
                init = init + self.emit.emitALOAD(rt, o.frame) if type(ast.init) is ArrayCell else init
                rt = FloatType() if type(ast.typ) is FloatType else rt
                if type(rt) is AutoType:
                    self.update(ast.init.name, ast.typ, o.sym)
                    rt = ast.typ
                code = self.emit.emitVAR(idx, ast.name, rt, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
                self.emit.printout(code + init + self.emit.emitWRITEVAR(ast.name, rt, idx, o.frame))
                return Symbol(ast.name, rt, Index(idx))
    
    def visitId(self, ast, o):
        frame = o.frame
        idx = ast.name.find('.')
        if idx != -1:
            className = ast.name[:idx]
            varName = ast.name[(idx + 1):]
            _type = None
            for x in self.classEnv:
                if x[0] == className:
                    for y in x[1]:
                        if y.name == varName:
                            _type = y.mtype
            if isinstance(o, Access) and o.isLeft is True:
                return self.emit.emitPUTSTATIC(className + "." + varName, _type, frame), _type
            else:
                return self.emit.emitGETSTATIC(className + "." + varName, _type, frame), _type
        sym = None
        for x in o.sym:
            flag = False
            for y in x:
                if y.name == ast.name:
                    sym = y
                    flag = True
                    break
            if flag == True:
                break
        _type = sym.mtype
        if not isinstance(sym.value, Index):
            if isinstance(o, Access) and o.isLeft is True:
                return self.emit.emitPUTSTATIC(sym.value.value + "." + sym.name, _type, frame), sym.mtype
            else:
                return self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, _type, frame), sym.mtype
        else:
            if isinstance(o, Access) and o.isLeft is True:
                return self.emit.emitWRITEVAR(sym.name, _type, sym.value.value, frame), sym.mtype
            else:
                return self.emit.emitREADVAR(sym.name, _type, sym.value.value, frame), sym.mtype
    
    def visitParamDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, ast.name, ast.typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        return Symbol(ast.name, ast.typ, Index(idx))
    
    def visitAssignStmt(self, ast, o):
        frame = o.frame
        frame.push()
        frame.push()
        expCode, expType = self.visit(ast.rhs, Access(frame, o.sym, False, True))
        lhsCode, lhsType = self.visit(ast.lhs, Access(frame, o.sym, True, True))
        if isinstance(lhsType, FloatType) and isinstance(expType, IntegerType):
            expCode = expCode + self.emit.emitI2F(frame)
            expType = FloatType()
        if type(ast.rhs) is ArrayCell:
            expCode += self.emit.emitALOAD(expType, frame)
        self.emit.printout(expCode + lhsCode) if type(ast.lhs) is not ArrayCell else self.emit.printout(lhsCode + expCode + self.emit.emitASTORE(lhsType, frame))
        frame.pop()
        frame.pop()
    
    def visitBreakStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.has_break = True
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinueStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))
    
    def visitReturnStmt(self, ast, o):
        self.has_return = True
        frame = o.frame
        for x in self.func_lst:
            if x.name == self.func:
                for y in x.params:
                    if y.out == True:
                        if x.name == 'swap':
                            self.visit(AssignStmt(Id('Swap.' + y.name), Id(y.name)), o)
                        else:
                            self.visit(AssignStmt(Id(x.name + "." + y.name), Id(y.name)), o)
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else:
            expcode, exptype = self.visit(ast.expr, Access(frame, o.sym, False, True))
            if type(ast.expr) is ArrayCell:
                expcode += self.emit.emitALOAD(exptype, frame)
            if type(frame.returnType) is FloatType and type(exptype) is IntegerType:
                expcode = expcode + self.emit.emitI2F(frame)
                self.emit.printout(expcode + self.emit.emitRETURN(FloatType(), frame))
            else:
                self.emit.printout(expcode + self.emit.emitRETURN(exptype, frame))
    
    def visitIfStmt(self, ast, o):
        if_exprCode, if_exprType = self.visit(ast.cond, Access(o.frame, o.sym, False, True))
        self.emit.printout(if_exprCode)
        if ast.fstmt is not None:
            labelElse = o.frame.getNewLabel()
            labelExit = o.frame.getNewLabel()
            self.emit.printout(self.emit.emitIFFALSE(labelElse, o.frame))
            self.visit(ast.tstmt, o)
            if self.has_return == False:
                self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))
            self.emit.printout(self.emit.emitLABEL(labelElse, o.frame))
            self.visit(ast.fstmt, o)
            if self.has_return == False:
                self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))
        else:
            labelExit = o.frame.getNewLabel()
            self.emit.printout(self.emit.emitIFFALSE(labelExit, o.frame))
            self.visit(ast.tstmt, o)
            self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))
    
    def visitBlockStmt(self, ast, o):
        self.stage += 1
        glenv = SubBody(o.frame, [[]] + o.sym) if self.stage > 1 else o
        self.has_return = False
        self.has_break = False
        for x in ast.body:
            if type(x) is VarDecl:
                glenv.sym[0] += [self.visit(x, glenv)]
            else:
                self.visit(x, glenv)

        if ast.body != []:
            if self.has_return == False:
                for x in self.func_lst:
                    if x.name == self.func:
                        for y in x.params:
                            if y.out == True:
                                if x.name == 'swap':
                                    self.visit(AssignStmt(Id('Swap.' + y.name), Id(y.name)), glenv)
                                else:
                                    self.visit(AssignStmt(Id(x.name + "." + y.name), Id(y.name)), glenv)

        self.stage -= 1
    
    def visitFuncCall(self, ast, o):
        frame = o.frame
        nenv = o.sym[-1]
        sym = None
        for x in range(len(nenv)):
            if nenv[x].name == ast.name:
                if type(nenv[x].mtype.rettype) is AutoType:
                    nenv[x].mtype.rettype = self.lhs_type
                    sym = nenv[x]
                else:
                    sym = nenv[x]
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        has_auto_param = False
        has_out_param = False
        real_param = []

        for x in self.func_lst:
            if x.name == ast.name:
                for y in range(len(x.params)):
                    if x.params[y].out == True:
                        has_out_param = True

        for x in self.func_lst:
            if x.name == ast.name:
                for y in range(len(x.params)):
                    if x.params[y].out == True and not isinstance(ast.args[y], (ArrayCell, Id)):
                        raise IllegalRuntimeException(str(ast.args[y]))

        for x in range(len(ast.args)):
            if type(ast.args[x]) is FuncCall:
                for y in self.func_lst:
                    if y.name == ast.args[x].name and type(y.return_type) is AutoType:
                        self.lhs_type = ctype.partype[x]
                for y in self.passed:
                    if y.name == ast.args[x].name and type(y.return_type) is AutoType:
                        self.lhs_type = ctype.partype[x]

            str1, typ1 = self.visit(ast.args[x], Access(frame, o.sym, False, True))
            if type(ctype.partype[x]) is AutoType:
                has_auto_param = True
            if type(typ1) is IntegerType and type(ctype.partype[x]) is FloatType:
                typ1 = FloatType()
                str1 = str1 + self.emit.emitI2F(frame)
            elif type(ast.args[x]) is ArrayCell:
                str1 += self.emit.emitALOAD(typ1, frame)
            real_param += [typ1]
            temp = in_[1] + [typ1]
            in_ = (in_[0] + str1, in_[1] + temp)
        params = []
        inherit = None
        body = None
        out_param = []
        if has_auto_param == True:
            for x in self.func_lst:
                if x.name == ast.name:
                    for y in range(len(x.params)):
                        str1, typ1 = self.visit(ast.args[y], Access(frame, o.sym, False, True))
                        params += [ParamDecl(x.params[y].name, typ1, x.params[y].out, x.params[y].inherit)]
                        if x.params[y].out == True:
                            out_param += [VarDecl(x.params[y].name, typ1)]
                    inherit = x.inherit
                    body = x.body
            if out_param != []:
                if ast.name == 'swap':
                    self.visit(ClassDecl('Swap', out_param), SubBody(None, o.sym))
                else:
                    self.visitClassDecl(ClassDecl(ast.name, out_param), SubBody(None, o.sym))
                self.className = 'MT22Class'

            for x in range(len(nenv)):
                if nenv[x].name == ast.name:
                    t = nenv.pop(x)
                    nenv.insert(x, Symbol(ast.name, MType(real_param, t.mtype.rettype), CName(self.className)))
                    self.passed += [FuncDecl(ast.name, t.mtype.rettype, params, inherit, body)]

        ctype = ctype if real_param == [] else MType(real_param, ctype.rettype)
        if has_out_param and self.stage > 0:
            self.emit.printout(in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, frame))
            for x in self.func_lst:
                if x.name == ast.name:
                    for y in range(len(x.params)):
                        if x.params[y].out == True:
                            if ast.name == 'swap':
                                self.visit(AssignStmt(ast.args[y], Id('Swap.' + x.params[y].name)), o)
                            else:
                                self.visit(AssignStmt(ast.args[y], Id(ast.name + '.' + x.params[y].name)), o)
            return "", ctype.rettype
        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, frame), ctype.rettype

    def visitUnExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        bodyCode, bodyType = self.visit(ast.val, o)
        if ast.op == '!':
            return bodyCode + self.emit.emitNOT(BooleanType(), frame), BooleanType()
        elif ast.op == '-':
            return bodyCode + self.emit.emitNEGOP(bodyType, frame), bodyType
                
    
    def visitWhileStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        exp, exptype = self.visit(ast.cond, Access(frame, nenv, False, True))
        frame.enterLoop()
        label1 = frame.getContinueLabel()
        label2 = frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        self.emit.printout(exp)
        self.emit.printout(self.emit.emitIFFALSE(label2,frame))
        self.visit(ast.stmt, o)
        self.emit.printout(self.emit.emitGOTO(label1,frame))
        self.emit.printout(self.emit.emitLABEL(label2, frame))
        frame.exitLoop()
    
    def visitForStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        self.visit(ast.init, o)
        exp, exptype = self.visit(ast.cond, Access(frame, nenv, False, True))
        frame.enterLoop()
        label1 = frame.getContinueLabel()
        label2 = frame.getBreakLabel()
        label3 = frame.getNewLabel()
        # o.frame.conLabel += [frame.getNewLabel()]
        self.emit.printout(self.emit.emitLABEL(label3, frame))
        self.emit.printout(exp)
        self.emit.printout(self.emit.emitIFFALSE(label2, frame))
        self.visit(ast.stmt, o)
        # if not self.has_break:
        #     self.emit.printout(self.emit.emitLABEL(o.frame.conLabel[-1], frame))
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        self.visit(AssignStmt(ast.init.lhs, BinExpr('+', ast.init.lhs, ast.upd)), o)
        self.emit.printout(self.emit.emitGOTO(label3, frame))
        self.emit.printout(self.emit.emitLABEL(label2, frame))
        frame.exitLoop()
    
    def visitArrayLit(self, ast, o):
        frame = o.frame if type(o) is not Frame else o
        code = self.emit.emitPUSHCONST(str(len(ast.explist)), IntegerType(), frame)
        if type(ast.explist[0]) is not ArrayLit:
            code += self.emit.emitNEWARRAY(self.arr_type.typ, frame)
            for x in range(len(ast.explist)):
                code += self.emit.emitDUP(frame)
                e1c, e1t = self.visit(ast.explist[x], o)
                if type(self.arr_type.typ) is FloatType and type(e1t) is IntegerType:
                    e1c = e1c + self.emit.emitI2F(frame)
                    e1t = FloatType()
                code += self.emit.emitPUSHCONST(str(x), IntegerType(), frame)
                code += e1c + self.emit.emitASTORE(e1t, frame)
            return code, ArrayType([len(ast.explist)], self.arr_type.typ)
        else:
            e1c, e1t = self.visit(ast.explist[0], o)
            code += self.emit.emitANEWARRAY(e1t, frame)
            rt = None
            for x in range(len(ast.explist)):
                code += self.emit.emitDUP(frame)
                e1c, e1t = self.visit(ast.explist[x], o)
                rt = e1t
                code += self.emit.emitPUSHCONST(str(x), IntegerType(), frame)
                code += e1c + self.emit.emitASTORE(e1t, frame)
            return code, ArrayType([len(ast.explist)] + rt.dimensions, self.arr_type.typ)
    
    def visitArrayCell(self, ast, o):
        frame = o.frame
        sym = None
        for x in o.sym:
            flag = False
            for y in x:
                if y.name == ast.name:
                    sym = y
                    flag = True
                    break
            if flag == True:
                break
        _type = sym.mtype
        code = None
        rt = None
        if not isinstance(sym.value, Index):
            code, rt = self.emit.emitGETSTATIC(sym.value.value + "." + sym.name, _type, frame), sym.mtype
        else:
            code, rt = self.emit.emitREADVAR(sym.name, _type, sym.value.value, frame), sym.mtype
        dimension = _type.dimensions
        max_dimension = dimension
        for x in range(len(ast.cell)):
            dimension = dimension[1:]
            e1c, e1t = self.visit(ast.cell[x], Access(frame, o.sym, False, False))
            code += e1c
            if x < len(max_dimension) - 1:
                code += self.emit.emitALOAD(ArrayType(dimension, _type.typ), o.frame)
        if dimension == []:
            return code, _type.typ
        else:
            return code, ArrayType(dimension, _type.typ)
    
    def visitDoWhileStmt(self, ast, o):
        o.frame.enterLoop()
        labelContinue = o.frame.getContinueLabel()
        labelExit = o.frame.getBreakLabel()
        label1 = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(label1, o.frame))
        self.visit(ast.stmt, o)
        expCode, exp_type = self.visit(ast.cond, Access(o.frame, o.sym, False, True))
        self.emit.printout(self.emit.emitLABEL(labelContinue, o.frame))
        self.emit.printout(expCode)
        self.emit.printout(self.emit.emitIFFALSE(labelExit, o.frame))
        self.emit.printout(self.emit.emitGOTO(label1, o.frame))
        self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))
        o.frame.exitLoop()


