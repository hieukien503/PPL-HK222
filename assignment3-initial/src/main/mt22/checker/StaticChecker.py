from Visitor import Visitor
from AST import *
from Utils import Utils
from StaticError import *

class Symbol:
    def __init__(self, name: str, typ, init=None):
        self.name = name
        self.typ = typ
        self.init = init

class Param:
    def __init__(self, name: str, typ, inherit: bool, out: bool):
        self.name = name
        self.typ = typ
        self.inherit = inherit
        self.out = out

class Func:
    def __init__(self, name: str, par_list, ret_type, inherit: str or None, body):
        self.name = name
        self.lst = par_list
        self.ret_type = ret_type
        self.inherit = inherit
        self.body = body

class StaticChecker (Visitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        self.global_env = [[]]
        self.in_loop = []
        self.func_lst = []
        self.inherit_lst = [[]]
        self.parent_func = None
        self.idx = -1
        self.stage = 0
        self.pre_func = None
        self.typ = None
        self.func_call = None
        self.var_decl = []
        self.in_ifelse = []
        self.kept_ast = []
        self.save_stage = 0

    def check(self):
        self.visit(self.ast, self.global_env)

    def visitIntegerType(self, ast, param):
        return IntegerType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBooleanType(self, ast, param):
        return BooleanType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        return ArrayType(ast.dimensions, ast.typ)

    def visitAutoType(self, ast, param):
        return AutoType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitBinExpr(self, ast, param):
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)
        if ast.op in ['::']:
            if isinstance(left, AutoType) and isinstance(right, StringType):
                if isinstance(ast.left, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.left.name:
                            param[-1][x].ret_type = right
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.left, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.left.name:
                                    param[-1][x].lst[y].typ = right
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.left.name:
                                param[x][y].typ = right
                                flag = True
                                break
                        if flag == True:
                            break
                left = right
            elif isinstance(right, AutoType) and isinstance(left, StringType):
                if isinstance(ast.right, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.right.name:
                            param[-1][x].ret_type = left
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.right, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.right.name:
                                    param[-1][x].lst[y].typ = left
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.right.name:
                                param[x][y].typ = left
                                flag = True
                                break
                        if flag == True:
                            break
                right = left
            if not ((isinstance(left, StringType) and isinstance(right, StringType)) or (isinstance(left, (AutoType, tuple)) and isinstance(right, (AutoType, tuple)))):
                raise TypeMismatchInExpression(ast)
            else:
                return StringType()
        elif ast.op in ['==', '!=']:
            if isinstance(left, AutoType) and isinstance(right, (IntegerType, BooleanType)):
                if isinstance(ast.left, (FuncCall, CallStmt)):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.left.name:
                            param[-1][x].ret_type = right
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.left, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.left.name:
                                    param[-1][x].lst[y].typ = right
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.left.name:
                                param[x][y].typ = right
                                flag = True
                                break
                        if flag == True:
                            break
                left = right
            elif isinstance(right, AutoType) and isinstance(left, (IntegerType, BooleanType)):
                if isinstance(ast.right, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.right.name:
                            param[-1][x].ret_type = left
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.right, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.right.name:
                                    param[-1][x].lst[y].typ = left
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.right.name:
                                param[x][y].typ = left
                                flag = True
                                break
                        if flag == True:
                            break
                right = left
            if not ((isinstance(left, (IntegerType, BooleanType)) and isinstance(right, (IntegerType, BooleanType))) or (isinstance(left, (AutoType, tuple)) and isinstance(right, (AutoType, tuple)))):
                raise TypeMismatchInExpression(ast)
            else:
                return BooleanType()
        elif ast.op in ['<', '>', '<=', '>=']:
            if isinstance(left, AutoType) and isinstance(right, (IntegerType, FloatType)):
                if isinstance(ast.left, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.left.name:
                            param[-1][x].ret_type = right
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.left, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.left.name:
                                    param[-1][x].lst[y].typ = right
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.left.name:
                                param[x][y].typ = right
                                flag = True
                                break
                        if flag == True:
                            break
                left = right
            elif isinstance(right, AutoType) and isinstance(left, (IntegerType, FloatType)):
                if isinstance(ast.right, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.right.name:
                            param[-1][x].ret_type = left
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.right, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.right.name:
                                    param[-1][x].lst[y].typ = left
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.right.name:
                                param[x][y].typ = left
                                flag = True
                                break
                        if flag == True:
                            break
                right = left
            if not ((isinstance(left, (IntegerType, FloatType)) and isinstance(right, (IntegerType, FloatType))) or (isinstance(left, (AutoType, tuple)) and isinstance(right, (AutoType, tuple)))):
                raise TypeMismatchInExpression(ast)
            else:
                return BooleanType()
        elif ast.op in ['&&', '||']:
            if isinstance(left, AutoType) and isinstance(right, BooleanType):
                if isinstance(ast.left, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.left.name:
                            param[-1][x].ret_type = right
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.left, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.left.name:
                                    param[-1][x].lst[y].typ = right
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.left.name:
                                param[x][y].typ = right
                                flag = True
                                break
                        if flag == True:
                            break
                left = right
            elif isinstance(right, AutoType) and isinstance(left, BooleanType):
                if isinstance(ast.right, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.right.name:
                            param[-1][x].ret_type = left
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.right, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.right.name:
                                    param[-1][x].lst[y].typ = left
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.right.name:
                                param[x][y].typ = left
                                flag = True
                                break
                        if flag == True:
                            break
                right = left
            if not ((isinstance(left, BooleanType) and isinstance(right, BooleanType)) or (isinstance(left, (AutoType, tuple)) and isinstance(right, (AutoType, tuple)))):
                raise TypeMismatchInExpression(ast)
            else:
                return BooleanType()
        elif ast.op in ['+', '-', '*', '/']:
            if isinstance(left, AutoType) and isinstance(right, (IntegerType, FloatType)):
                if isinstance(ast.left, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.left.name:
                            param[-1][x].ret_type = right
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.left, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.left.name:
                                    param[-1][x].lst[y].typ = right
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.left.name:
                                param[x][y].typ = right
                                flag = True
                                break
                        if flag == True:
                            break
                left = right
            elif isinstance(right, AutoType) and isinstance(left, (IntegerType, FloatType)):
                if isinstance(ast.right, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.right.name:
                            param[-1][x].ret_type = left
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.right, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.right.name:
                                    param[-1][x].lst[y].typ = left
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.right.name:
                                param[x][y].typ = left
                                flag = True
                                break
                        if flag == True:
                            break
                right = left
            if not ((isinstance(left, (IntegerType, FloatType)) and isinstance(right, (IntegerType, FloatType))) or (isinstance(left, (AutoType, tuple)) and isinstance(right, (AutoType, tuple)))):
                raise TypeMismatchInExpression(ast)
            else:
                if (isinstance(left, FloatType) or isinstance(right, FloatType)):
                    return FloatType()
                elif isinstance(left, AutoType) and isinstance(right, AutoType):
                    return (FloatType(), IntegerType())
                else:
                    return IntegerType()
        else:
            if isinstance(left, AutoType) and isinstance(right, IntegerType):
                if isinstance(ast.left, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.left.name:
                            param[-1][x].ret_type = right
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.left, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.left.name:
                                    param[-1][x].lst[y].typ = right
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.left.name:
                                param[x][y].typ = right
                                flag = True
                                break
                        if flag == True:
                            break
                left = right
            if isinstance(right, AutoType) and isinstance(left, IntegerType):
                if isinstance(ast.right, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.right.name:
                            param[-1][x].ret_type = left
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.right, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.right.name:
                                    param[-1][x].lst[y].typ = left
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.right.name:
                                param[x][y].typ = left
                                flag = True
                                break
                        if flag == True:
                            break
                right = left
            if not ((isinstance(left, IntegerType) and isinstance(right, IntegerType)) or (isinstance(left, (AutoType, tuple)) and isinstance(right, (AutoType, tuple)))):
                raise TypeMismatchInExpression(ast)
            else:
                return IntegerType()

    def visitUnExpr(self, ast, param):
        operand = self.visit(ast.val, param)
        if ast.op in ['-']:
            if isinstance(operand, AutoType):
                if isinstance(ast.val, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.val.name:
                            param[-1][x].ret_type = self.typ
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.val, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.val.name:
                                    param[-1][x].lst[y].typ = self.typ
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.val.name:
                                param[x][y].typ = self.typ
                                flag = True
                                break
                        if flag == True:
                            break
                operand = self.typ
            if not isinstance(operand, (IntegerType, FloatType)):
                raise TypeMismatchInExpression(ast)
            return IntegerType() if isinstance(operand, IntegerType) else FloatType()
        else:
            if isinstance(operand, AutoType):
                if isinstance(ast.val, FuncCall):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.val.name:
                            param[-1][x].ret_type = BooleanType()
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                elif isinstance(ast.val, Param) and self.func_call is not None:
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                            for y in range(len(param[-1][x].lst)):
                                if param[-1][x].lst[y].name == ast.val.name:
                                    param[-1][x].lst[y].typ = BooleanType()
                else:
                    flag = False
                    for x in range(len(param)):
                        for y in range(len(param[x])):
                            if isinstance(param[x][y], Symbol) and param[x][y].name == ast.val.name:
                                param[x][y].typ = BooleanType()
                                flag = True
                                break
                        if flag == True:
                            break
                operand = BooleanType()
            if not isinstance(operand, BooleanType):
                raise TypeMismatchInExpression(ast)
            return BooleanType()

    def visitId(self, ast, param):
        for x in param[:-1]:
            for y in range(len(x)):
                if isinstance(x[y], Symbol):
                    if ast.name == x[y].name:
                        return x[y].typ
        for x in param[-1]:
            if isinstance(x, Func) and x.name == (self.func_call if self.func_call is not None else self.pre_func):
                for para in x.lst:
                    if ast.name == para.name:
                        return para.typ
        for x in self.inherit_lst:
            for y in x:
                if y[3] == self.parent_func:
                    for z in y[2]:
                        if z.name == ast.name:
                            return z.typ
        for x in range(len(param[-1])):
            if isinstance(param[-1][x], Symbol):
                if ast.name == param[-1][x].name and (self.idx == -1 or x <= self.idx):
                    return param[-1][x].typ
        raise Undeclared(Identifier(), ast.name)
            

    def visitArrayCell(self, ast, param):
        for x in param:
            for y in x:
                if isinstance(y, (Symbol, Param)):
                    if ast.name == y.name:
                        if not isinstance(y.typ, ArrayType):
                            raise TypeMismatchInExpression(ast)
                        else:
                            if len(y.typ.dimensions) < len(ast.cell):
                                raise TypeMismatchInExpression(ast)
                            for t in ast.cell:
                                typ = self.visit(t, param)
                                if isinstance(typ, AutoType):
                                    for func in range(len(param[-1])):
                                        if type(param[-1][func]) is Func and param[-1][func].name == ast.init.name:
                                            param[-1][func].ret_type = IntegerType()
                                            self.func_call = param[-1][func].name
                                            self.save_stage = 0
                                            param = self.visit(param[-1][func].body, param)
                                            self.save_stage = 0
                                            self.func_call = None
                                            typ = IntegerType()
                                if not isinstance(typ, IntegerType):
                                    raise TypeMismatchInExpression(t)
                        dimen = y.typ.dimensions[len(ast.cell):] if len(ast.cell) < len(y.typ.dimensions) else []
                        return y.typ.typ if dimen == [] else ArrayType(dimen, y.typ.typ)
        raise Undeclared(Variable(), ast.name)

    def visitIntegerLit(self, ast, param):
        return IntegerType()

    def visitFloatLit(self, ast, param):
        return FloatType()

    def visitStringLit(self, ast, param):
        return StringType()

    def visitBooleanLit(self, ast, param):
        return BooleanType()

    def visitArrayLit(self, ast, param):
        self.kept_ast += [ast]
        if ast.explist == []:
            return ArrayType([0], AtomicType)
        first_type = self.visit(ast.explist[0], param)
        for x in ast.explist[1:]:
            temp = self.visit(x, param)
            if type(temp) != type(first_type):
                raise IllegalArrayLiteral(self.kept_ast[0])
        
        self.kept_ast = self.kept_ast[:-1]
        if isinstance(first_type, (IntegerType, FloatType, StringType, BooleanType)):
            return ArrayType([len(ast.explist)], first_type)
        if isinstance(first_type, AutoType):
            for x in ast.explist:
                for y in range(len(param[-1])):
                    if type(param[-1][y]) is Func and param[-1][y].name == x.name:
                        param[-1][y].ret_type = self.typ.typ
                        self.func_call = param[-1][y].name
                        self.save_stage = 0
                        param = self.visit(param[-1][y].body, param)
                        self.save_stage = 0
                        self.func_call = None
                        break
            return ArrayType([len(ast.explist)], self.typ.typ)           
        return ArrayType([len(ast.explist)] + first_type.dimensions, first_type.typ)

    def visitFuncCall(self, ast, param):
        lst_specFunc = ['readInteger', 'readFloat', 'readString', 'readBoolean']
        if ast.name in lst_specFunc:
            if ast.name == lst_specFunc[0]:
                if len(ast.args) == 0:
                    return IntegerType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif ast.name == lst_specFunc[1]:
                if len(ast.args) == 0:
                    return FloatType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif ast.name == lst_specFunc[2]:
                if len(ast.args) == 0:
                    return StringType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                if len(ast.args) == 0:
                    return BooleanType()
                else:
                    raise TypeMismatchInExpression(ast)
        else:
            for x in param:
                for y in x:
                    if isinstance(y, (Param, Symbol)) and y.name == ast.name:
                        raise TypeMismatchInExpression(ast)
            for x in range(len(param[-1])):
                if type(param[-1][x]) is Func:
                    if ast.name == param[-1][x].name:
                        self.func_call = ast.name
                        if isinstance(param[-1][x].ret_type, VoidType):
                            raise TypeMismatchInExpression(ast)
                        if len(ast.args) == len(param[-1][x].lst):
                            has_auto_param = False
                            for y in range(len(ast.args)):
                                t = self.visit(ast.args[y], param)
                                if type(t) != type(param[-1][x].lst[y].typ) and not (isinstance(param[-1][x].lst[y].typ, AutoType) or isinstance(t, AutoType)) and not (isinstance(param[-1][x].lst[y].typ, FloatType) and isinstance(t, (FloatType, IntegerType))):
                                    raise TypeMismatchInExpression(ast)
                                if isinstance(param[-1][x].lst[y].typ, AutoType):
                                    param[-1][x].lst[y].typ = t
                                    has_auto_param = True
                                elif isinstance(t, AutoType):
                                    if isinstance(ast.args[y], Param):
                                        for para in range(len(param[-1][x].lst)):
                                            if param[-1][x].lst[para].name == ast.args[y].name:
                                                param[-1][x].lst[para].typ = param[-1][x].lst[y].typ
                                    elif isinstance(ast.args[y], FuncCall):
                                        for func in range(len(param[-1])):
                                            if type(func) is Func and param[-1][func].name == ast.args[func].name:
                                                param[-1][func].ret_type = param[-1][x].lst[y].typ
                                                save_func_call = self.func_call
                                                self.func_call = ast.args[y].name
                                                self.save_stage = 0
                                                param = self.visit(param[-1][func].body, param)
                                                self.save_stage = 0
                                                self.func_call = save_func_call
                            if has_auto_param == True:
                                self.save_stage = 0
                                safe_param = [param[-1][x].lst] + [param[-1]]
                                safe_param = self.visit(param[-1][x].body, safe_param)
                                self.save_stage = 0
                            self.func_call = None
                            return param[-1][x].ret_type
                        else:
                            raise TypeMismatchInExpression(ast)
            raise Undeclared(Function(), ast.name)

    def visitAssignStmt(self, ast, param):
        rhs_type = self.visit(ast.rhs, param)
        lhs_type = self.visit(ast.lhs, param)
        if isinstance(rhs_type, AutoType):
            for x in range(len(param[-1])):
                if type(param[-1][x]) is Func and param[-1][x].name == ast.rhs.name:
                    param[-1][x].ret_type = lhs_type
                    self.func_call = param[-1][x].name
                    self.save_stage = 0
                    param = self.visit(param[-1][x].body, param)
                    self.save_stage = 0
                    self.func_call = None
                if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                    for y in range(len(param[-1][x].lst)):
                        if param[-1][x].lst[y].name == ast.rhs.name:
                            param[-1][x].lst[y].typ = lhs_type
            rhs_type = lhs_type
        elif isinstance(lhs_type, AutoType) and self.func_call is not None:
            for x in range(len(param[-1])):
                if type(param[-1][x]) is Func and param[-1][x].name == self.pre_func:
                    for y in range(len(param[-1][x].lst)):
                        if param[-1][x].lst[y].name == ast.lhs.name:
                            param[-1][x].lst[y].typ = rhs_type
            lhs_type = rhs_type
        self.typ = lhs_type
        if isinstance(lhs_type, FloatType):
            if not isinstance(rhs_type, (FloatType, IntegerType)):
                raise TypeMismatchInStatement(ast)
        else:
            if isinstance(lhs_type, (VoidType, ArrayType)):
                raise TypeMismatchInStatement(ast)
            else:
                if type(lhs_type) != type(rhs_type) and not isinstance(lhs_type, AutoType):
                    raise TypeMismatchInStatement(ast)
        return param

    def visitBlockStmt(self, ast, param):
        self.save_stage += 1
        if self.func_call is None:
            self.stage += 1

        safe_param = param
        if self.stage > 1:
            param = [[]] + param
        for x in ast.body:
            if x == ast.body[0] and self.stage == 1 and self.func_call is None:
                if self.parent_func is not None:
                    for func in param[-1]:
                        if type(func) is Func and func.name == self.parent_func and func.lst != []:
                            if not isinstance(x, CallStmt) or not (isinstance(x, CallStmt) and (x.name == 'preventDefault' or x.name == 'super')):
                                raise InvalidStatementInFunction(self.pre_func)
                else:
                    if isinstance(x, CallStmt) and (x.name == 'preventDefault' or x.name == 'super'):
                        raise InvalidStatementInFunction(self.pre_func)
            elif x != ast.body[0] and self.stage == 1:
                if isinstance(x, CallStmt) and (x.name == 'preventDefault' or x.name == 'super'):
                    raise InvalidStatementInFunction(self.pre_func)
            if isinstance(x, VarDecl):
                param = self.visit(x, param)
            elif isinstance(x, (ForStmt, DoWhileStmt, WhileStmt)):
                self.in_loop = self.in_loop + [True]
                param = self.visit(x, param)
                self.in_loop = self.in_loop[:-1]
            elif isinstance(x, ReturnStmt):
                if self.in_ifelse == []:
                    param = self.visit(x, param)
                    break
                else:
                    param = self.visit(x, param)
            else:
                param = self.visit(x, param)
        
        if ast.body == [] and self.parent_func is not None:
            for func in param[-1]:
                if type(func) is Func and func.name == self.parent_func and func.lst != []:
                    raise InvalidStatementInFunction(self.pre_func)
        
        param = param[1:] if safe_param[0] != param[0] else param
        self.save_stage -= 1
        if self.func_call is None:
            self.stage -= 1
        if self.stage == 0:
            param = param[1:] if len(param) > 1 else param
        return param

    def visitIfStmt(self, ast, param):
        self.in_ifelse += [True]
        cond = self.visit(ast.cond, param)
        if not isinstance(cond, BooleanType):
            if isinstance(cond, AutoType):
                for x in range(len(param[-1])):
                    if type(param[-1][x]) is Func and param[-1][x].name == ast.cond.name:
                        param[-1][x].ret_type = BooleanType()
                        cond = BooleanType()
                        self.func_call = param[-1][x].name
                        self.save_stage = 0
                        param = self.visit(param[-1][x].body, param)
                        self.save_stage = 0
                        self.func_call = None
            else:
                raise TypeMismatchInStatement(ast)
        param = self.visit(ast.tstmt, param)
        if ast.fstmt is not None:
            param = self.visit(ast.fstmt, param)
        self.in_ifelse = self.in_ifelse[:-1]
        return param

    def visitForStmt(self, ast, param):
        scalar_type = self.visit(ast.init.lhs, param)
        initExp_type = self.visit(ast.init.rhs, param)
        if not isinstance(scalar_type, IntegerType):
            if isinstance(initExp_type, AutoType):
                for x in range(len(param[-1])):
                    if type(param[-1][x]) is Func and param[-1][x].name == ast.init.rhs.name:
                        param[-1][x].ret_type = IntegerType()
                        initExp_type = IntegerType()
                        self.func_call = param[-1][x].name
                        self.save_stage = 0
                        param = self.visit(param[-1][x].body, param)
                        self.save_stage = 0
                        self.func_call = None
            if not isinstance(initExp_type, IntegerType):
                raise TypeMismatchInStatement(ast)
        upd = self.visit(ast.upd, param)
        if not isinstance(upd, IntegerType):
            if isinstance(upd, AutoType):
                for x in range(len(param[-1])):
                    if type(param[-1][x]) is Func and param[-1][x].name == ast.upd.name:
                        param[-1][x].ret_type = IntegerType()
                        upd = IntegerType()
                        self.func_call = param[-1][x].name
                        self.save_stage = 0
                        param = self.visit(param[-1][x].body, param)
                        self.save_stage = 0
                        self.func_call = None
            else:
                raise TypeMismatchInStatement(ast)
        cond = self.visit(ast.cond, param)
        if not isinstance(cond, BooleanType):
            if isinstance(cond, AutoType):
                for x in range(len(param[-1])):
                    if type(param[-1][x]) is Func and param[-1][x].name == ast.cond.name:
                        param[-1][x].ret_type = BooleanType()
                        cond = BooleanType()
                        self.func_call = param[-1][x].name
                        self.save_stage = 0
                        param = self.visit(param[-1][x].body, param)
                        self.save_stage = 0
                        self.func_call = None
            else:
                raise TypeMismatchInStatement(ast)
        param = self.visit(ast.stmt, param)
        return param

    def visitWhileStmt(self, ast, param):
        cond = self.visit(ast.cond, param)
        if not isinstance(cond, BooleanType):
            if isinstance(cond, AutoType):
                for x in range(len(param[-1])):
                    if type(param[-1][x]) is Func and param[-1][x].name == ast.cond.name:
                        param[-1][x].ret_type = BooleanType()
                        cond = BooleanType()
                        self.func_call = param[-1][x].name
                        self.save_stage = 0
                        param = self.visit(param[-1][x].body, param)
                        self.save_stage = 0
                        self.func_call = None
            else:
                raise TypeMismatchInStatement(ast)
        param = self.visit(ast.stmt, param)
        return param

    def visitDoWhileStmt(self, ast, param):
        param = self.visit(ast.stmt, param)
        cond = self.visit(ast.cond, param)
        if not isinstance(cond, BooleanType):
            if isinstance(cond, AutoType):
                for x in range(len(param[-1])):
                    if type(param[-1][x]) is Func and param[-1][x].name == ast.cond.name:
                        param[-1][x].ret_type = BooleanType()
                        cond = BooleanType()
                        self.func_call = param[-1][x].name
                        self.save_stage = 0
                        param = self.visit(param[-1][x].body, param)
                        self.save_stage = 0
                        self.func_call = None
            else:
                raise TypeMismatchInStatement(ast)
        return param

    def visitBreakStmt(self, ast, param):
        if self.in_loop == []:
            raise MustInLoop(ast)
        return param

    def visitContinueStmt(self, ast, param):
        if self.in_loop == []:
            raise MustInLoop(ast)
        return param

    def visitReturnStmt(self, ast, param):
        for x in param[-1]:
            if type(x) is Func and x.name == (self.func_call if self.func_call is not None else self.pre_func):
                if not isinstance(x.ret_type, AutoType):
                    if isinstance(x.ret_type, VoidType) and not (ast.expr is None):
                        raise TypeMismatchInStatement(ast)
                    if not isinstance(x.ret_type, VoidType) and (ast.expr is None):
                        raise TypeMismatchInStatement(ast)
                    if ast.expr is not None:
                        t = self.visit(ast.expr, param)
                        if type(t) is tuple:
                            return param
                        if isinstance(t, VoidType):
                            raise TypeMismatchInStatement(ast)
                        if type(t) is AutoType:
                            for y in range(len(param[-1])):
                                if type(param[-1][y]) is Func and param[-1][y].name == ast.expr.name:
                                    param[-1][y].ret_type = x.ret_type
                                    self.func_call = param[-1][y].name
                                    self.save_stage = 0
                                    param = self.visit(param[-1][y].body, param)
                                    self.save_stage = 0
                                    self.func_call = None
                                    t = x.ret_type
                        if type(t) != type(x.ret_type) and not (isinstance(x.ret_type, FloatType) and isinstance(t, (FloatType, IntegerType))):
                            raise TypeMismatchInStatement(ast)
                else:
                    if ast.expr is not None:
                        t = self.visit(ast.expr, param)
                        if type(t) is tuple:
                            return param
                        for y in range(len(param[-1])):
                            if type(param[-1][y]) is Func and param[-1][y].name == x.name:
                                param[-1][y].ret_type = t
                    else:
                        for y in range(len(param[-1])):
                            if type(param[-1][y]) is Func and param[-1][y].name == x.name:
                                param[-1][y].ret_type = VoidType()
        return param

    def visitCallStmt(self, ast, param):
        lst_specFunc = ['printInteger', 'printFloat', 'printString', 'printBoolean', 'preventDefault', 'super']
        if ast.name in lst_specFunc:
            if ast.name == lst_specFunc[0]:
                if len(ast.args) == 1:
                    if isinstance(self.visit(ast.args[0], param), IntegerType):
                        return param
                    elif isinstance(self.visit(ast.args[0], param), AutoType):
                        for x in range(len(param[-1])):
                            if type(param[-1][x]) is Func and param[-1][x].name == ast.args[0].name:
                                param[-1][x].ret_type = IntegerType
                                self.func_call = param[-1][x].name
                                self.save_stage = 0
                                param = self.visit(param[-1][x].body, param)
                                self.save_stage = 0
                                self.func_call = None
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            elif ast.name == lst_specFunc[1]:
                if len(ast.args) == 1:
                    if isinstance(self.visit(ast.args[0], param), (FloatType, IntegerType)):
                        return param
                    elif isinstance(self.visit(ast.args[0], param), AutoType):
                        for x in range(len(param[-1])):
                            if type(param[-1][x]) is Func and param[-1][x].name == ast.args[0].name:
                                param[-1][x].ret_type = FloatType
                                self.func_call = param[-1][x].name
                                self.save_stage = 0
                                param = self.visit(param[-1][x].body, param)
                                self.save_stage = 0
                                self.func_call = None
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            elif ast.name == lst_specFunc[2]:
                if len(ast.args) == 1:
                    if isinstance(self.visit(ast.args[0], param), StringType):
                        return param
                    elif isinstance(self.visit(ast.args[0], param), AutoType):
                        for x in range(len(param[-1])):
                            if type(param[-1][x]) is Func and param[-1][x].name == ast.args[0].name:
                                param[-1][x].ret_type = StringType
                                self.func_call = param[-1][x].name
                                self.save_stage = 0
                                param = self.visit(param[-1][x].body, param)
                                self.save_stage = 0
                                self.func_call = None
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            elif ast.name == lst_specFunc[3]:
                if len(ast.args) == 1:
                    if isinstance(self.visit(ast.args[0], param), BooleanType):
                        return param
                    elif isinstance(self.visit(ast.args[0], param), AutoType):
                        for x in range(len(param[-1])):
                            if type(param[-1][x]) is Func and param[-1][x].name == ast.args[0].name:
                                param[-1][x].ret_type = BooleanType
                                self.func_call = param[-1][x].name
                                self.save_stage = 0
                                param = self.visit(param[-1][x].body, param)
                                self.save_stage = 0
                                self.func_call = None
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            elif ast.name == lst_specFunc[4]:
                if len(ast.args) == 0:
                    return param
                else:
                    raise TypeMismatchInStatement(ast)
            else:
                for x in range(len(param[-1])):
                    if type(param[-1][x]) is Func:
                        if self.parent_func == param[-1][x].name:
                            if len(ast.args) == len(param[-1][x].lst):
                                for y in range(len(ast.args)):
                                    if not isinstance(ast.args[y], Id) and param[-1][x].lst[y].out == True:
                                        raise TypeMismatchInExpression(ast)
                                    t = self.visit(ast.args[y], param)
                                    if type(t) != type(param[-1][x].lst[y].typ) and not (isinstance(param[-1][x].lst[y].typ, AutoType) or isinstance(t, AutoType)) and not (isinstance(param[-1][x].lst[y].typ, FloatType) and isinstance(t, (FloatType, IntegerType))):
                                        raise TypeMismatchInExpression(ast)
                                    if isinstance(param[-1][x].lst[y].typ, AutoType):
                                        param[-1][x].lst[y].typ = t
                                    elif isinstance(t, AutoType):
                                        if isinstance(ast.args[y], Param):
                                            for para in range(len(param[-1][x].lst)):
                                                if param[-1][x].lst[para].name == ast.args[y].name:
                                                    param[-1][x].lst[para].typ = param[-1][x].lst[y].typ
                                        elif isinstance(ast.args[y], FuncCall):
                                            for func in range(len(param[-1])):
                                                if type(param[-1][func]) is Func and param[-1][func].name == ast.args[y].name:
                                                    param[-1][func].ret_type = param[-1][x].lst[y].typ
                                                    self.func_call = self.parent_func
                                                    self.save_stage = 0
                                                    param = self.visit(param[-1][func].body, param)
                                                    self.save_stage = 0
                                                    self.func_call = None
                                return param
                            else:
                                if len(ast.args) < len(param[-1][x].lst):
                                    raise TypeMismatchInExpression("")
                                else:
                                    raise TypeMismatchInExpression(ast.args[len(param[-1][x].lst)])
                return param
        else:
            self.func_call = ast.name
            for x in range(len(param[-1])):
                if type(param[-1][x]) is Func:
                    if ast.name == param[-1][x].name:
                        if len(ast.args) == len(param[-1][x].lst):
                            for y in range(len(ast.args)):
                                t = self.visit(ast.args[y], param)
                                if type(t) != type(param[-1][x].lst[y].typ) and not (isinstance(param[-1][x].lst[y].typ, AutoType) or isinstance(t, AutoType)) and not (isinstance(param[-1][x].lst[y].typ, FloatType) and isinstance(t, (FloatType, IntegerType))):
                                    raise TypeMismatchInStatement(ast)
                                if isinstance(param[-1][x].lst[y].typ, AutoType):
                                    param[-1][x].lst[y].typ = t
                                elif isinstance(t, AutoType):
                                    if isinstance(ast.args[y], Param):
                                        for para in range(len(param[-1][x].lst)):
                                            if param[-1][x].lst[para].name == ast.args[y].name:
                                                param[-1][x].lst[para].typ = param[-1][x].lst[y].typ
                                    elif isinstance(ast.args[y], FuncCall):
                                        for func in range(len(param[-1])):
                                            if type(func) is Func and param[-1][func].name == ast.args[func].name:
                                                param[-1][func].ret_type = param[-1][x].lst[y].typ
                                                save_func_call = self.func_call
                                                self.func_call = ast.args[y].name
                                                self.save_stage = 0
                                                param = self.visit(param[-1][func].body, param)
                                                self.save_stage = 0
                                                self.func_call = save_func_call
                            self.func_call = None
                            return param
                        else:
                            raise TypeMismatchInStatement(ast)
            raise Undeclared(Function(), ast.name)
        return param

    def visitVarDecl(self, ast, param):
        if ast.name in ['printInteger', 'printFloat', 'printString', 'printBoolean', 'preventDefault', 'super', 'readInteger', 'readFloat', 'readString', 'readBoolean']:
            raise Redeclared(Variable(), ast.name)
        
        if len(param) == 1:
            if self.lookup(ast.name, self.var_decl, lambda x: x.name) is not None:
                raise Redeclared(Variable(), ast.name)
            if self.lookup(ast.name, param[-1][:self.idx], lambda x: x.name) is not None:
                raise Redeclared(Variable(), ast.name)
        elif self.lookup(ast.name, param[0], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.name)
        
        varType = self.visit(ast.typ, param)
        self.typ = varType
        if isinstance(varType, AutoType):
            if ast.init is None:
                raise Invalid(Variable(), ast.name)
            if self.stage == 0:
                param[0].insert(self.idx, Symbol(ast.name, varType, ast.init))
                exp_typ = self.visit(ast.init, param)
                param[0][self.idx].typ = exp_typ
            else:
                param[0] = [Symbol(ast.name, varType, ast.init)] + param[0]
                exp_typ = self.visit(ast.init, param)
                param[0][0].typ = exp_typ
        else:
            if self.stage == 0:
                param[0].insert(self.idx, Symbol(ast.name, varType, ast.init))
            else:
                param[0] = [Symbol(ast.name, varType, ast.init)] + param[0]

            if ast.init is not None:
                if isinstance(ast.init, FuncCall) and ast.init.name == ast.name:
                    raise TypeMismatchInExpression(ast.init)
                exp_typ = self.visit(ast.init, param)
                if isinstance(exp_typ, AutoType):
                    for x in range(len(param[-1])):
                        if type(param[-1][x]) is Func and param[-1][x].name == ast.init.name:
                            param[-1][x].ret_type = varType
                            self.func_call = param[-1][x].name
                            self.save_stage = 0
                            param = self.visit(param[-1][x].body, param)
                            self.save_stage = 0
                            self.func_call = None
                            exp_typ = self.visit(ast.init, param)
                        exp_typ = varType
                elif isinstance(varType, FloatType):
                    if not (isinstance(exp_typ, (FloatType, IntegerType))):
                        raise TypeMismatchInVarDecl(ast)
                elif isinstance(exp_typ, tuple):
                    if not isinstance(varType, FloatType):
                        raise TypeMismatchInVarDecl(ast)
                else:
                    if isinstance(varType, ArrayType) and isinstance(exp_typ, ArrayType):
                        if not (isinstance(varType.typ, FloatType) and isinstance(exp_typ.typ, (FloatType, IntegerType)) or type(varType.typ) == type(exp_typ.typ)):
                            raise TypeMismatchInVarDecl(ast)
                        else:
                            if len(varType.dimensions) != len(exp_typ.dimensions):
                                raise TypeMismatchInVarDecl(ast)
                            for x in range(len(exp_typ.dimensions)):
                                if varType.dimensions[x] != exp_typ.dimensions[x]:
                                    raise TypeMismatchInVarDecl(ast)
                    elif type(varType) != type(exp_typ):
                        raise TypeMismatchInVarDecl(ast)
        return param

    def visitParamDecl(self, ast, param):
        return Param(ast.name, ast.typ, ast.inherit, ast.out)

    def visitFuncDecl(self, ast, param):
        if ast.name in ['printInteger', 'printFloat', 'printString', 'printBoolean', 'preventDefault', 'super', 'readInteger', 'readFloat', 'readString', 'readBoolean']:
            raise Redeclared(Function(), ast.name)
        if self.lookup(ast.name, param[-1][:self.idx], lambda x: x.name) is not None:
            raise Redeclared(Function(), ast.name) 
        params = []
        parent_param = []
        self.pre_func = ast.name
        
        if ast.inherit is not None:
            self.parent_func = ast.inherit
            if self.lookup (ast.inherit, self.func_lst, lambda z: type(z) is FuncDecl and z.name) is None:
                raise Undeclared(Function(), ast.inherit)
            for x in self.func_lst:
                if isinstance(x, FuncDecl) and x.name == ast.inherit:
                    for y in x.params:
                        if self.lookup(y.name, parent_param, lambda z: z.name) is not None:
                            raise Redeclared(Parameter(), y.name)
                        if y.inherit == True:
                            parent_param += [self.visit(y, param)]
                    break
        else:
            self.parent_func = None
            parent_param = []

        for x1 in ast.params:
            if self.lookup(x1.name, params, lambda y: y.name) is not None:
                raise Redeclared(Parameter(), x1.name)
            else:
                params += [self.visit(x1, param)]
        
        is_prevent = False
        for x in parent_param:
            if x.inherit == True:
                for y in params:
                    if x.name == y.name:
                        if len(ast.body.body) > 0 and (isinstance(ast.body.body[0], CallStmt) and ast.body.body[0].name == "preventDefault"):
                            is_prevent = True
                            break
                        else:
                            raise Invalid(Parameter(), x.name)
                if is_prevent == True:
                    break
        if len(ast.body.body) > 0 and (isinstance(ast.body.body[0], CallStmt) and ast.body.body[0].name == "preventDefault"):
            is_prevent = True
        parent_param = [] if is_prevent == True else parent_param
        flag = False
        for x in self.inherit_lst:
            for y in x:
                if y[3] == ast.name:
                    flag = True
                    x.append([ast.name, params, parent_param, ast.inherit])
                    break
                elif y[3] == ast.inherit:
                    flag = True
                    x = [[ast.name, params, parent_param, ast.inherit]] + x
                    break
                elif y[0] == ast.name:
                    flag = True
                    break
        if flag == False:
            self.inherit_lst = [[]] + self.inherit_lst if self.inherit_lst != [[]] else [[]]
            self.inherit_lst[0] +=  [[ast.name, params, parent_param, ast.inherit]]
        
        params = params + parent_param
        param = [params] + param
        param = self.visit(ast.body, param)
        self.pre_func = None
        return param

    def visitProgram(self, ast, param):
        self.func_lst = []
        for x in ast.decls:
            if isinstance(x, FuncDecl):
                param[-1] += [Func(x.name, [self.visit(para, param) for para in x.params], x.return_type, x.inherit, x.body)]
            self.func_lst += [x]
  
        func_decl = []
        i = 0
        for x in self.func_lst:
            if isinstance(x, FuncDecl):
                if self.lookup(x.name, func_decl, lambda z: z.name) is not None:
                    raise Redeclared(Function(), x.name)
                for y in range(len(param[-1])):
                    if type(param[-1][y]) is Func and x.name == param[-1][y].name:
                        self.idx = y
                        param = self.visit(x, param)
                        func_decl += [x]
                        self.idx = -1
            else:
                self.idx = i
                param = self.visit(x, param)
                self.idx = -1
                self.var_decl += [x]
            i += 1

        entry_point = False
        for x in ast.decls:
            if isinstance(x, FuncDecl):
                if x.name == 'main' and x.params == [] and isinstance(x.return_type, VoidType):
                    entry_point = True
                    break
        
        if entry_point == False:
            raise NoEntryPoint()