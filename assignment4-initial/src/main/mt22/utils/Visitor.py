from abc import ABC, ABCMeta


class Visitor(ABC):

    def visit(self, ast, param):
        return ast.accept(self, param)

    def visitIntegerType(self, ast, param): pass
    def visitFloatType(self, ast, param): pass
    def visitBooleanType(self, ast, param): pass
    def visitStringType(self, ast, param): pass
    def visitArrayType(self, ast, param): pass
    def visitAutoType(self, ast, param): pass
    def visitVoidType(self, ast, param): pass

    def visitBinExpr(self, ast, param): pass
    def visitUnExpr(self, ast, param): pass
    def visitId(self, ast, param): pass
    def visitArrayCell(self, ast, param): pass
    def visitIntegerLit(self, ast, param): pass
    def visitFloatLit(self, ast, param): pass
    def visitStringLit(self, ast, param): pass
    def visitBooleanLit(self, ast, param): pass
    def visitArrayLit(self, ast, param): pass
    def visitFuncCall(self, ast, param): pass

    def visitAssignStmt(self, ast, param): pass
    def visitBlockStmt(self, ast, param): pass
    def visitIfStmt(self, ast, param): pass
    def visitForStmt(self, ast, param): pass
    def visitWhileStmt(self, ast, param): pass
    def visitDoWhileStmt(self, ast, param): pass
    def visitBreakStmt(self, ast, param): pass
    def visitContinueStmt(self, ast, param): pass
    def visitReturnStmt(self, ast, param): pass
    def visitCallStmt(self, ast, param): pass

    def visitVarDecl(self, ast, param): pass
    def visitParamDecl(self, ast, param): pass
    def visitFuncDecl(self, ast, param): pass

    def visitProgram(self, ast, param): pass
