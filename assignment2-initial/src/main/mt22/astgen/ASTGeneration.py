from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        decls = []
        for x in ctx.declare():
            decl = self.visitDeclare(x)
            if isinstance(decl, list):
                decls.extend(decl)
            else:
                decls.append(decl)
        return Program(decls)
    
    def visitDeclare(self, ctx: MT22Parser.DeclareContext):
        return self.visitChildren(ctx)
    
    def visitFunc_decl(self, ctx: MT22Parser.Func_declContext):
        functype = self.visitFunc_type(ctx.func_type())
        funcname = ctx.ID()[0].getText()
        paralist = self.visitPara_list(ctx.para_list()) if ctx.para_list() else []
        blockstmt = self.visitBlock_func(ctx.block_func())
        inherit = None if len(ctx.ID()) == 1 else ctx.ID()[1].getText()
        return FuncDecl(funcname, functype, paralist, inherit, blockstmt)
    
    def visitPrim_type(self, ctx: MT22Parser.Prim_typeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else:
            return BooleanType()
    
    def visitIntList(self, ctx:MT22Parser.IntListContext):
        lst = [int(x.getText()) for x in ctx.INT_LIT()]
        return lst
    
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        int_list = self.visitIntList(ctx.intList())
        prim_type = self.visitPrim_type(ctx.prim_type())
        return ArrayType(int_list, prim_type)
    
    
    def visitVar_type(self, ctx: MT22Parser.Var_typeContext):
        if ctx.prim_type():
            return self.visitPrim_type(ctx.prim_type())
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visitArray_type(ctx.array_type())
    
    def visitFunc_type(self, ctx: MT22Parser.Func_typeContext):
        if ctx.var_type():
            return self.visitVar_type(ctx.var_type())
        return VoidType()
       
    def visitVarlist(self, ctx:MT22Parser.VarlistContext):
        lst = [x for x in ctx.ID()]
        return lst

    def visitVar_decl(self, ctx: MT22Parser.Var_declContext):
        varlist = self.visitVarlist(ctx.varlist())
        vartype = self.visitVar_type(ctx.var_type())
        initExp = [self.visitExpression(x) for x in ctx.expression()] if ctx.ASSIGN() else None
        if initExp is None:
            return [VarDecl(varlist[x].getText(), vartype) for x in range(len(varlist))]
        return [VarDecl(varlist[x].getText(), vartype, initExp[x]) for x in range(len(varlist))]
    
    def visitPara_dec(self, ctx:MT22Parser.Para_decContext):
        para_var = ctx.ID().getText()
        para_type = self.visitVar_type(ctx.var_type())
        inherit = True if ctx.INHERIT() else False
        out = True if ctx.OUT() else False
        return ParamDecl(para_var, para_type, out, inherit)
    
    def visitPara_list(self, ctx:MT22Parser.Para_listContext):
        return [self.visitPara_dec(x) for x in ctx.para_dec()]
    
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        return [self.visitExpression(x) for x in ctx.expression()]
    
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        if ctx.CONCAT():
            op = ctx.CONCAT()
            left = self.visitExpression1(ctx.expression1()[0])
            right = self.visitExpression1(ctx.expression1()[1])
            return BinExpr(op, left, right)
        else:
            return self.visitChildren(ctx)
    
    def visitExpression1(self, ctx:MT22Parser.Expression1Context):
        if ctx.EQ():
            op = ctx.EQ()
            left = self.visitExpression2(ctx.expression2()[0])
            right = self.visitExpression2(ctx.expression2()[1])
            return BinExpr(op, left, right)
        elif ctx.NOT_EQ():
            op = ctx.NOT_EQ()
            left = self.visitExpression2(ctx.expression2()[0])
            right = self.visitExpression2(ctx.expression2()[1])
            return BinExpr(op, left, right)
        elif ctx.LT():
            op = ctx.LT()
            left = self.visitExpression2(ctx.expression2()[0])
            right = self.visitExpression2(ctx.expression2()[1])
            return BinExpr(op, left, right)
        elif ctx.LTE():
            op = ctx.LTE()
            left = self.visitExpression2(ctx.expression2()[0])
            right = self.visitExpression2(ctx.expression2()[1])
            return BinExpr(op, left, right)
        elif ctx.GT():
            op = ctx.GT()
            left = self.visitExpression2(ctx.expression2()[0])
            right = self.visitExpression2(ctx.expression2()[1])
            return BinExpr(op, left, right)
        elif ctx.GTE():
            op = ctx.GTE()
            left = self.visitExpression2(ctx.expression2()[0])
            right = self.visitExpression2(ctx.expression2()[1])
            return BinExpr(op, left, right)
        else:
            return self.visitChildren(ctx)
    
    def visitExpression2(self, ctx:MT22Parser.Expression2Context):
        if ctx.AND():
            op = ctx.AND()
            left = self.visitExpression2(ctx.expression2())
            right = self.visitExpression3(ctx.expression3())
            return BinExpr(op, left, right)
        elif ctx.OR():
            op = ctx.OR()
            left = self.visitExpression2(ctx.expression2())
            right = self.visitExpression3(ctx.expression3())
            return BinExpr(op, left, right)
        else:
            return self.visitExpression3(ctx.expression3())
    
    def visitExpression3(self, ctx:MT22Parser.Expression3Context):
        if ctx.ADD():
            op = ctx.ADD()
            left = self.visitExpression3(ctx.expression3())
            right = self.visitExpression4(ctx.expression4())
            return BinExpr(op, left, right)
        elif ctx.SUB():
            op = ctx.SUB()
            left = self.visitExpression3(ctx.expression3())
            right = self.visitExpression4(ctx.expression4())
            return BinExpr(op, left, right)
        else:
            return self.visitExpression4(ctx.expression4())
        
    def visitExpression4(self, ctx:MT22Parser.Expression4Context):
        if ctx.MUL():
            op = ctx.MUL()
            left = self.visitExpression4(ctx.expression4())
            right = self.visitExpression5(ctx.expression5())
            return BinExpr(op, left, right)
        elif ctx.DIV():
            op = ctx.DIV()
            left = self.visitExpression4(ctx.expression4())
            right = self.visitExpression5(ctx.expression5())
            return BinExpr(op, left, right)
        elif ctx.MOD():
            op = ctx.MOD()
            left = self.visitExpression4(ctx.expression4())
            right = self.visitExpression5(ctx.expression5())
            return BinExpr(op, left, right)
        else:
            return self.visitExpression5(ctx.expression5())
    
    def visitExpression5(self, ctx:MT22Parser.Expression5Context):
        if ctx.NEGATION():
            op = ctx.NEGATION()
            operand = self.visitExpression5(ctx.expression5())
            return UnExpr(op, operand)
        else:
            return self.visitExpression6(ctx.expression6())
    
    def visitExpression6(self, ctx:MT22Parser.Expression6Context):
        if ctx.SUB():
            op = ctx.SUB()
            operand = self.visitExpression6(ctx.expression6())
            return UnExpr(op, operand)
        else:
            return self.visitExpression7(ctx.expression7())
    
    def visitExpression7(self, ctx:MT22Parser.Expression7Context):
        if ctx.array_Ele():
            return self.visitArray_Ele(ctx.array_Ele())
        else:
            return self.visitOperands(ctx.operands())
        
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        if ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.R_OPEN() and ctx.R_CLOSE():
            return self.visitExpression(ctx.expression())
        elif ctx.func_call():
            return self.visitFunc_call(ctx.func_call())
        else:
            return self.visitArray_literal(ctx.array_literal())
    
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        if ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            s = ctx.FLOAT_LIT().getText()
            if len(s) >= 3:
                if s[0] == '.' and (s[1] == 'e' or s[1] == 'E'):
                    s = '0' + s
                    return FloatLit(float(s))
            return FloatLit(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STR_LIT():
            return StringLit(ctx.STR_LIT())
        else:
            return BooleanLit(False) if ctx.FALSE() else BooleanLit(True)

    def visitArray_Ele(self, ctx:MT22Parser.Array_EleContext):
        iden = ctx.ID().getText()
        exp_list = self.visitExpression_list(ctx.expression_list())
        return ArrayCell(iden, exp_list)
    
    def visitArray_literal(self, ctx:MT22Parser.Array_literalContext):
        exp_list = self.visitExpression_list(ctx.expression_list()) if ctx.expression_list() else []
        return ArrayLit(exp_list)
    
    def visitBlock_func(self, ctx:MT22Parser.Block_funcContext):
        stmt_list = []
        for x in ctx.stmt():
            y = self.visitStmt(x)
            if isinstance(y, list):
                stmt_list.extend(y)
            else:
                stmt_list.append(y)
        return BlockStmt(stmt_list)
    
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx:MT22Parser.StatementContext):
        if ctx.for_stmt():
            return self.visitFor_stmt(ctx.for_stmt())
        elif ctx.if_stmt():
            return self.visitIf_stmt(ctx.if_stmt())
        elif ctx.break_stmt():
            return self.visitBreak_stmt(ctx.break_stmt())
        elif ctx.cont_stmt():
            return self.visitCont_stmt(ctx.cont_stmt())
        elif ctx.return_stmt():
            return self.visitReturn_stmt(ctx.return_stmt())
        elif ctx.do_while_stmt():
            return self.visitDo_while_stmt(ctx.do_while_stmt())
        elif ctx.while_stmt():
            return self.visitWhile_stmt(ctx.while_stmt())
        elif ctx.call_func():
            return self.visitCall_func(ctx.call_func())
        elif ctx.assign_stmt():
            return self.visitAssign_stmt(ctx.assign_stmt())
        else:
            return self.visitBlock_func(ctx.block_func())

    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        init = self.visitInit_stmt(ctx.init_stmt())
        cond = self.visitExpression(ctx.expression()[0])
        update = self.visitExpression(ctx.expression()[1])
        body = self.visitStatement(ctx.statement())
        return ForStmt(init, cond, update, body)
    
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        cond = self.visitExpression(ctx.expression())
        tstmt = self.visitStatement(ctx.statement()[0])
        fstmt = None if not ctx.ELSE() else self.visitStatement(ctx.statement()[1])
        return IfStmt(cond, tstmt, fstmt)

    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        body = self.visitBlock_func(ctx.block_func())
        cond = self.visitExpression(ctx.expression())
        return DoWhileStmt(cond, body)

    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        body = self.visitStatement(ctx.statement())
        cond = self.visitExpression(ctx.expression())
        return WhileStmt(cond, body)
    
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()
    
    def visitCont_stmt(self, ctx: MT22Parser.Cont_stmtContext):
        return ContinueStmt()
    
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return ReturnStmt(self.visitExpression(ctx.expression())) if ctx.expression() else ReturnStmt()
    
    def visitCall_func(self, ctx:MT22Parser.Call_funcContext):
        func_name = ctx.ID().getText()
        arg_lst = [] if not ctx.expression_list() else self.visitExpression_list(ctx.expression_list())
        return CallStmt(func_name, arg_lst)
    
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        lhs = self.visitLhs(ctx.lhs())
        rhs = self.visitExpression(ctx.expression())
        return AssignStmt(lhs, rhs)
    
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visitArray_Ele(ctx.array_Ele())
    
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        func_name = ctx.ID().getText()
        arg_lst = [] if not ctx.expression_list() else self.visitExpression_list(ctx.expression_list())
        return FuncCall(func_name, arg_lst)

    def visitInit_stmt(self, ctx:MT22Parser.Init_stmtContext):
        lhs = self.visitLhs(ctx.lhs())
        rhs = self.visitExpression(ctx.expression())
        return AssignStmt(lhs, rhs)
        

