# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#array_literal.
    def visitArray_literal(self, ctx:MT22Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declare.
    def visitDeclare(self, ctx:MT22Parser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_type.
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prim_type.
    def visitPrim_type(self, ctx:MT22Parser.Prim_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varlist.
    def visitVarlist(self, ctx:MT22Parser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intList.
    def visitIntList(self, ctx:MT22Parser.IntListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_Ele.
    def visitArray_Ele(self, ctx:MT22Parser.Array_EleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_type.
    def visitFunc_type(self, ctx:MT22Parser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_list.
    def visitPara_list(self, ctx:MT22Parser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_dec.
    def visitPara_dec(self, ctx:MT22Parser.Para_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_func.
    def visitBlock_func(self, ctx:MT22Parser.Block_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#cont_stmt.
    def visitCont_stmt(self, ctx:MT22Parser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_func.
    def visitCall_func(self, ctx:MT22Parser.Call_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_stmt.
    def visitInit_stmt(self, ctx:MT22Parser.Init_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression1.
    def visitExpression1(self, ctx:MT22Parser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression2.
    def visitExpression2(self, ctx:MT22Parser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression3.
    def visitExpression3(self, ctx:MT22Parser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression4.
    def visitExpression4(self, ctx:MT22Parser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression5.
    def visitExpression5(self, ctx:MT22Parser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression6.
    def visitExpression6(self, ctx:MT22Parser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression7.
    def visitExpression7(self, ctx:MT22Parser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        return self.visitChildren(ctx)



del MT22Parser