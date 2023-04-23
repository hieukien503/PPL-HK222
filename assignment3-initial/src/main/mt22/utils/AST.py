from abc import ABC, abstractmethod, ABCMeta
from typing import List, Tuple


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def accept(self, v, param):
        method_name = 'visit{}'.format(self.__class__.__name__)
        visit = getattr(v, method_name)
        return visit(self, param)


class Stmt(AST):
    pass


class Expr(Stmt):
    pass


class Type(AST):
    pass


class Decl(AST):
    pass

# Types


class AtomicType(Type):
    pass


class IntegerType(AtomicType):
    def __str__(self):
        return self.__class__.__name__


class FloatType(AtomicType):
    def __str__(self):
        return self.__class__.__name__


class BooleanType(AtomicType):
    def __str__(self):
        return self.__class__.__name__


class StringType(AtomicType):
    def __str__(self):
        return self.__class__.__name__


class ArrayType(Type):
    def __init__(self, dimensions: List[int], typ: AtomicType):
        self.dimensions = dimensions
        self.typ = typ

    def __str__(self):
        return "ArrayType([{}], {})".format(", ".join([str(dimen) for dimen in self.dimensions]), str(self.typ))


class AutoType(Type):
    def __str__(self):
        return self.__class__.__name__


class VoidType(Type):
    def __str__(self):
        return self.__class__.__name__


# Expressions

class LHS(Expr):
    pass


class BinExpr(Expr):
    def __init__(self, op: str, left: Expr, right: Expr):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return "BinExpr({}, {}, {})".format(self.op, str(self.left), str(self.right))


class UnExpr(Expr):
    def __init__(self, op: str, val: Expr):
        self.op = op
        self.val = val

    def __str__(self):
        return "UnExpr({}, {})".format(self.op, str(self.val))


class Id(LHS):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return "Id({})".format(self.name)


class ArrayCell(LHS):
    def __init__(self, name: str, cell: List[Expr]):
        self.name = name
        self.cell = cell

    def __str__(self):
        return "ArrayCell({}, [{}])".format(self.name, ", ".join([str(expr) for expr in self.cell]))


class IntegerLit(Expr):
    def __init__(self, val: int):
        self.val = val

    def __str__(self):
        return "IntegerLit({})".format(self.val)


class FloatLit(Expr):
    def __init__(self, val: float):
        self.val = val

    def __str__(self):
        return "FloatLit({})".format(self.val)


class StringLit(Expr):
    def __init__(self, val: str):
        self.val = val

    def __str__(self):
        return "StringLit({})".format(self.val)


class BooleanLit(Expr):
    def __init__(self, val: bool):
        self.val = val

    def __str__(self):
        return "BooleanLit({})".format("True" if self.val else "False")


class ArrayLit(Expr):
    def __init__(self, explist: List[Expr]):
        self.explist = explist

    def __str__(self):
        return "ArrayLit([{}])".format(", ".join([str(exp) for exp in self.explist]))


class FuncCall(Expr):
    def __init__(self, name: str, args: List[Expr]):
        self.name = name
        self.args = args

    def __str__(self):
        return "FuncCall({}, [{}])".format(self.name, ", ".join([str(expr) for expr in self.args]))


# Statements

class AssignStmt(Stmt):
    def __init__(self, lhs: LHS, rhs: Expr):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return "AssignStmt({}, {})".format(str(self.lhs), self.rhs)


class BlockStmt(Stmt):
    def __init__(self, body: List[Stmt or VarDecl]):
        self.body = body

    def __str__(self):
        return "BlockStmt([{}])".format(", ".join([str(body) for body in self.body]))


class IfStmt(Stmt):
    def __init__(self, cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None):
        self.cond = cond
        self.tstmt = tstmt
        self.fstmt = fstmt

    def __str__(self):
        return "IfStmt({}, {}{})".format(str(self.cond), str(self.tstmt), ", " + str(self.fstmt) if self.fstmt else "")


class ForStmt(Stmt):
    def __init__(self, init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt):
        self.init = init
        self.cond = cond
        self.upd = upd
        self.stmt = stmt

    def __str__(self):
        return "ForStmt({}, {}, {}, {})".format(str(self.init), str(self.cond), str(self.upd), str(self.stmt))


class WhileStmt(Stmt):
    def __init__(self, cond: Expr, stmt: Stmt):
        self.cond = cond
        self.stmt = stmt

    def __str__(self):
        return "WhileStmt({}, {})".format(str(self.cond), str(self.stmt))


class DoWhileStmt(Stmt):
    def __init__(self, cond: Expr, stmt: BlockStmt):
        self.cond = cond
        self.stmt = stmt

    def __str__(self):
        return "DoWhileStmt({}, {})".format(str(self.cond), str(self.stmt))


class BreakStmt(Stmt):
    def __str__(self):
        return "BreakStmt()"


class ContinueStmt(Stmt):
    def __str__(self):
        return "ContinueStmt()"


class ReturnStmt(Stmt):
    def __init__(self, expr: Expr or None = None):
        self.expr = expr

    def __str__(self):
        return "ReturnStmt({})".format(str(self.expr) if self.expr else "")


class CallStmt(Stmt):
    def __init__(self, name: str, args: List[Expr]):
        self.name = name
        self.args = args

    def __str__(self):
        return "CallStmt({}, {})".format(self.name, ", ".join([str(expr) for expr in self.args]))


# Declarations


class VarDecl(Decl):
    def __init__(self, name: str, typ: Type, init: Expr or None = None):
        self.name = name
        self.typ = typ
        self.init = init

    def __str__(self):
        return "VarDecl({}, {}{})".format(self.name, str(self.typ), ", " + str(self.init) if self.init else "")


class ParamDecl(Decl):
    def __init__(self, name: str, typ: Type, out: bool = False, inherit: bool = False):
        self.name = name
        self.typ = typ
        self.out = out
        self.inherit = inherit

    def __str__(self):
        return "{}{}Param({}, {})".format("Inherit" if self.inherit else "", "Out" if self.out else "", self.name, str(self.typ))


class FuncDecl(Decl):
    def __init__(self, name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt):
        self.name = name
        self.return_type = return_type
        self.params = params
        self.inherit = inherit
        self.body = body

    def __str__(self):
        return "FuncDecl({}, {}, [{}], {}, {})".format(self.name, str(self.return_type), ", ".join([str(param) for param in self.params]), self.inherit if self.inherit else "None", str(self.body))

# Program


class Program(AST):
    def __init__(self, decls: List[Decl]):
        self.decls = decls

    def __str__(self):
        return "Program([\n\t{}\n])".format("\n\t".join([str(decl) for decl in self.decls]))
