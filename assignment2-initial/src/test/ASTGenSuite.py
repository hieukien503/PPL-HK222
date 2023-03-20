import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """i, j, t: string = \"20\", \"30\", \"40\";
        main: function void()
        {
            k = j :: (i :: t);
            printString(k);
        }"""
        expect = """Program([
	VarDecl(i, StringType, StringLit(20))
	VarDecl(j, StringType, StringLit(30))
	VarDecl(t, StringType, StringLit(40))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(k), BinExpr(::, Id(j), BinExpr(::, Id(i), Id(t)))), CallStmt(printString, Id(k))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_301(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))
    def test_302(self):
        input = """a, b, c, d: integer = 3, 4, 10, 9_3617;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(10))
	VarDecl(d, IntegerType, IntegerLit(93617))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))
    def test_303(self):
        input = """a: string = \"Hello, World\";"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(Hello, World))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))
    def test_304(self):
        input = """a: array[2, 3] of integer = {{1, 2, 3}, {4, 5, 6}};"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
    def test_305(self):
        input = """a: integer = -123456789;"""
        expect = """Program([
	VarDecl(a, IntegerType, UnExpr(-, IntegerLit(123456789)))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
    def test_306(self):
        input = """main: function void() {
            a, b: string = "Hello", ", world!";
            c: string = a::b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, StringLit(Hello)), VarDecl(b, StringType, StringLit(, world!)), VarDecl(c, StringType, BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    def test_307(self):
        input = """foo: function void(out n: integer, delta: integer) {
            n = n + delta;
            return;
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    def test_308(self):
        input = """fibo: function integer(n: integer) {
            if (n <= 2) return 1;
            else return fibo(n - 1) + fibo(n - 2);
        }
            main: function void() {
                printInteger(fibo(20));
        }"""
        expect = """Program([
	FuncDecl(fibo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(2)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(+, FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(2))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, FuncCall(fibo, [IntegerLit(20)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_309(self):
        input = """abc: integer;"""
        expect = """Program([
	VarDecl(abc, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 309))
    def test_310(self):
        input = """a: array [2, 3] of integer;"""
        expect = """Program([
	VarDecl(a, ArrayType([2, 3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    def test_311(self):
        input = """a, b: integer = 1, 2;
        x: float = 9.25;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(x, FloatType, FloatLit(9.25))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_312(self):
        input = """i: integer = 0;"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(0))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    def test_313(self):
        input = """foo: function void() inherit fact { return; }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], fact, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
    def test_314(self):
        input = """a, x: integer;"""
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 314))
    def test_315(self):
        input = """a: boolean = true;"""
        expect = """Program([
	VarDecl(a, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    def test_316(self):
        input = """main: function void() {
            i: integer = 0;
            do
            {
                printInteger(i);
                i = i + 1;
            } while (true);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BooleanLit(True), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
    def test_317(self):
        input = """a: array [1] of integer = {};"""
        expect = """Program([
	VarDecl(a, ArrayType([1], IntegerType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
    def test_318(self):
        input = """a, b: integer = 1 / 2, 20 + 30;"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(/, IntegerLit(1), IntegerLit(2)))
	VarDecl(b, IntegerType, BinExpr(+, IntegerLit(20), IntegerLit(30)))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    def test_319(self):
        input = """a, b, c: integer = 20, 1_96_3, 108;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(20))
	VarDecl(b, IntegerType, IntegerLit(1963))
	VarDecl(c, IntegerType, IntegerLit(108))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))
    def test_320(self):
        input = """foo: function integer (inherit out a: integer) inherit foo1 {
            preventDefault();
            return a + (-2018);
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [InheritOutParam(a, IntegerType)], foo1, BlockStmt([CallStmt(preventDefault, ), ReturnStmt(BinExpr(+, Id(a), UnExpr(-, IntegerLit(2018))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    def test_321(self):
        input = """perfectNum: function boolean (N: integer) {
            if ((N == 6) || (N == 28) || (N == 496) || (N == 8128) || (N == 33550336))
            {
                return true;
            }
            return false;
        }"""
        expect = """Program([
	FuncDecl(perfectNum, BooleanType, [Param(N, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(||, BinExpr(==, Id(N), IntegerLit(6)), BinExpr(==, Id(N), IntegerLit(28))), BinExpr(==, Id(N), IntegerLit(496))), BinExpr(==, Id(N), IntegerLit(8128))), BinExpr(==, Id(N), IntegerLit(33550336))), BlockStmt([ReturnStmt(BooleanLit(True))])), ReturnStmt(BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))
    def test_322(self):
        input = """foo: function integer (a: integer) {
            a = a + (-2018);
            return a;
        }
        main: function void() {
            a: integer = 2018;
            a = a + foo(a);
            readInteger(a);
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), UnExpr(-, IntegerLit(2018)))), ReturnStmt(Id(a))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(2018)), AssignStmt(Id(a), BinExpr(+, Id(a), FuncCall(foo, [Id(a)]))), CallStmt(readInteger, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
    def test_323(self):
        input = """x: float;
        foo: function integer() { 
            return 0;
        }
        a: integer = 10;"""
        expect = """Program([
	VarDecl(x, FloatType)
	FuncDecl(foo, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
	VarDecl(a, IntegerType, IntegerLit(10))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    def test_324(self):
        input = """x: float;
        foo: function integer() { 
            return 0;
        }
        goo: function void() {
            i: string;
        }"""
        expect = """Program([
	VarDecl(x, FloatType)
	FuncDecl(foo, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
	FuncDecl(goo, VoidType, [], None, BlockStmt([VarDecl(i, StringType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    def test_325(self):
        input = """x: integer = 10 - (2 + 3 * 4) / 7;"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(-, IntegerLit(10), BinExpr(/, BinExpr(+, IntegerLit(2), BinExpr(*, IntegerLit(3), IntegerLit(4))), IntegerLit(7))))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
    def test_326(self):
        input = """x: boolean = !((2 < 3) && (3 < 4));"""
        expect = """Program([
	VarDecl(x, BooleanType, UnExpr(!, BinExpr(&&, BinExpr(<, IntegerLit(2), IntegerLit(3)), BinExpr(<, IntegerLit(3), IntegerLit(4)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
    def test_327(self):
        input = """fact: function void(a: integer) {
            printInteger(a + 2018);
        }
        main: function void() {
            fact(2018);
        }"""
        expect = """Program([
	FuncDecl(fact, VoidType, [Param(a, IntegerType)], None, BlockStmt([CallStmt(printInteger, BinExpr(+, Id(a), IntegerLit(2018)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(fact, IntegerLit(2018))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    def test_328(self):
        input = """goo: function void(a: integer, b: float) {
            c: auto = a + 2 * b;
            printInteger(c);
        }
        main: function void() {
            goo(3, 2.7);
        }"""
        expect = """Program([
	FuncDecl(goo, VoidType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(c, AutoType, BinExpr(+, Id(a), BinExpr(*, IntegerLit(2), Id(b)))), CallStmt(printInteger, Id(c))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(goo, IntegerLit(3), FloatLit(2.7))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    def test_329(self):
        input = """goo: function string(a: array [100] of string, N: integer) {
            i: integer;
            s: string = "";
            for (i = 0, i < N, i + 1) {
                s = s :: a[i];
            }
            return s;
        }
        main: function void() {}"""
        expect = """Program([
	FuncDecl(goo, StringType, [Param(a, ArrayType([100], StringType)), Param(N, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(s, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(N)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(s), BinExpr(::, Id(s), ArrayCell(a, [Id(i)])))])), ReturnStmt(Id(s))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    def test_330(self):
        input = """abc: function auto(a: integer, b: float) {
            c: auto = 2 * a + b;
            printInteger(c);
        }
        main: function void(a: float) {
            abc(1, 2.0);
        }"""
        expect = """Program([
	FuncDecl(abc, AutoType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(c, AutoType, BinExpr(+, BinExpr(*, IntegerLit(2), Id(a)), Id(b))), CallStmt(printInteger, Id(c))]))
	FuncDecl(main, VoidType, [Param(a, FloatType)], None, BlockStmt([CallStmt(abc, IntegerLit(1), FloatLit(2.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
    def test_331(self):
        input = """main: function integer() {}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
    def test_332(self):
        input = """a29872: boolean = !((2 < 3) && (3 < 4));"""
        expect = """Program([
	VarDecl(a29872, BooleanType, UnExpr(!, BinExpr(&&, BinExpr(<, IntegerLit(2), IntegerLit(3)), BinExpr(<, IntegerLit(3), IntegerLit(4)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
    def test_333(self):
        input = """a, b: array [5_1, 9_6,78] of integer;
                   x: float;"""
        expect = """Program([
	VarDecl(a, ArrayType([51, 96, 78], IntegerType))
	VarDecl(b, ArrayType([51, 96, 78], IntegerType))
	VarDecl(x, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
    def test_334(self):
        input = """a, b: array [3, 4, 5] of integer;
                   x: float = -2.95;"""
        expect = """Program([
	VarDecl(a, ArrayType([3, 4, 5], IntegerType))
	VarDecl(b, ArrayType([3, 4, 5], IntegerType))
	VarDecl(x, FloatType, UnExpr(-, FloatLit(2.95)))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
    def test_335(self):
        input = """a, b: array [2] of integer;
        main: function void() {
            a[0] = 2018;
            a[1] = -2018;
            b[0] = a[0] + a[1];
            b[1] = a[0] - a[1];
        }
        """
        expect = """Program([
	VarDecl(a, ArrayType([2], IntegerType))
	VarDecl(b, ArrayType([2], IntegerType))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(2018)), AssignStmt(ArrayCell(a, [IntegerLit(1)]), UnExpr(-, IntegerLit(2018))), AssignStmt(ArrayCell(b, [IntegerLit(0)]), BinExpr(+, ArrayCell(a, [IntegerLit(0)]), ArrayCell(a, [IntegerLit(1)]))), AssignStmt(ArrayCell(b, [IntegerLit(1)]), BinExpr(-, ArrayCell(a, [IntegerLit(0)]), ArrayCell(a, [IntegerLit(1)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    def test_336(self):
        input = """a: array [4] of integer;
        main: function void() {
            i: integer;
            for (i = 0, i < 4, i + 1) {
                a[i] = readInteger();
                printInteger(a[i]);
            }
        }"""
        expect = """Program([
	VarDecl(a, ArrayType([4], IntegerType))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), FuncCall(readInteger, [])), CallStmt(printInteger, ArrayCell(a, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
    def test_337(self):
        input = """a: array [4] of integer;
        main: function void() {
            i: integer;
            for (i = 0, i < 4, i + 1) {
                a[i] = 3 * readInteger();
                printInteger(a[i]);
            }
        }"""
        expect = """Program([
	VarDecl(a, ArrayType([4], IntegerType))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(*, IntegerLit(3), FuncCall(readInteger, []))), CallStmt(printInteger, ArrayCell(a, [Id(i)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
    def test_338(self):
        input = """i, j, k: integer = 20, 30, 1_234;"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(20))
	VarDecl(j, IntegerType, IntegerLit(30))
	VarDecl(k, IntegerType, IntegerLit(1234))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
    def test_339(self):
        input = """i, j: integer = 20, 30;"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(20))
	VarDecl(j, IntegerType, IntegerLit(30))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
    def test_340(self):
        input = """x: integer = 20;
        a: auto = x + 3.7;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(20))
	VarDecl(a, AutoType, BinExpr(+, Id(x), FloatLit(3.7)))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
    def test_341(self):
        input = """foo: function boolean(a: boolean, out b: boolean) {}"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(a, BooleanType), OutParam(b, BooleanType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
    def test_342(self):
        input = """test_bool: boolean = false;"""
        expect = """Program([
	VarDecl(test_bool, BooleanType, BooleanLit(False))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
    def test_343(self):
        input = """main: function void() {
            a: array [100] of integer;
            i: integer;
            for (i = 0, i < 100, i + 1) {
                a[i] = readInteger();
                if (a[i] % 2 == 0)
                {
                    a[i] = a[i] / 2;
                }
                else
                {
                    a[i] = a[i] * 3 + 1;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([100], IntegerType)), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), FuncCall(readInteger, [])), IfStmt(BinExpr(==, BinExpr(%, ArrayCell(a, [Id(i)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(/, ArrayCell(a, [Id(i)]), IntegerLit(2)))]), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(+, BinExpr(*, ArrayCell(a, [Id(i)]), IntegerLit(3)), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
    def test_344(self):
        input = """main: function void() {
            a: array [100] of integer;
            i, n: integer;
            do
            {
                n = readInteger();
            } while ((n <= 0) || (n >= 100));
            for (i = 0, i < n, i + 1) {
                a[i] = readInteger();
                if (a[i] % 2 == 0)
                {
                    a[i] = a[i] / 2;
                }
                else
                {
                    a[i] = a[i] * 3 + 1;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([100], IntegerType)), VarDecl(i, IntegerType), VarDecl(n, IntegerType), DoWhileStmt(BinExpr(||, BinExpr(<=, Id(n), IntegerLit(0)), BinExpr(>=, Id(n), IntegerLit(100))), BlockStmt([AssignStmt(Id(n), FuncCall(readInteger, []))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), FuncCall(readInteger, [])), IfStmt(BinExpr(==, BinExpr(%, ArrayCell(a, [Id(i)]), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(/, ArrayCell(a, [Id(i)]), IntegerLit(2)))]), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(+, BinExpr(*, ArrayCell(a, [Id(i)]), IntegerLit(3)), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
    def test_345(self):
        input = """a_int: integer = 20;
        foo: function void (out a: integer) {
            a = a + 10;
        }
        main: function void() {
            foo(a_int);
            printInteger(a_int);
        }"""
        expect = """Program([
	VarDecl(a_int, IntegerType, IntegerLit(20))
	FuncDecl(foo, VoidType, [OutParam(a, IntegerType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(10)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, Id(a_int)), CallStmt(printInteger, Id(a_int))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
    def test_346(self):
        input = """foo: function array[10] of integer(a: array [10] of integer) {
            return a;
        }
        b: integer = 20;
        main: function void() { return; }"""
        expect = """Program([
	FuncDecl(foo, ArrayType([10], IntegerType), [Param(a, ArrayType([10], IntegerType))], None, BlockStmt([ReturnStmt(Id(a))]))
	VarDecl(b, IntegerType, IntegerLit(20))
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
    def test_347(self):
        input = """foo: function auto (a: integer) {
            if (a > 220) {
                if (a % 2 == 0)
                {
                    return a;
                }
                else
                {
                    return a + 1;
                }
            }
            else
            {
                return a + 10;
            }
        }"""
        expect = """Program([
	FuncDecl(foo, AutoType, [Param(a, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(220)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(a), IntegerLit(2)), IntegerLit(0)), BlockStmt([ReturnStmt(Id(a))]), BlockStmt([ReturnStmt(BinExpr(+, Id(a), IntegerLit(1)))]))]), BlockStmt([ReturnStmt(BinExpr(+, Id(a), IntegerLit(10)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
    def test_348(self):
        input = """i, j, k: integer = 20, 30, 40;
        main: function void()
        {
            i = j + k;
            printInteger(i);
        }"""
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(20))
	VarDecl(j, IntegerType, IntegerLit(30))
	VarDecl(k, IntegerType, IntegerLit(40))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(j), Id(k))), CallStmt(printInteger, Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
    def test_349(self):
        input = """i, j, k: float = 2.75, 1.98, 3.17;
        main: function void()
        {
            t = i + j + k;
            printFloat(t);
        }"""
        expect = """Program([
	VarDecl(i, FloatType, FloatLit(2.75))
	VarDecl(j, FloatType, FloatLit(1.98))
	VarDecl(k, FloatType, FloatLit(3.17))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(t), BinExpr(+, BinExpr(+, Id(i), Id(j)), Id(k))), CallStmt(printFloat, Id(t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    def test_350(self):
        input = """i, j: string = \"Baba\", \"Mama\";
        main: function void()
        {
            k = j :: i;
            t = (k :: j) :: i;
            l = k :: (j :: i);
            printString(t);
            printString(l);
        }"""
        expect = """Program([
	VarDecl(i, StringType, StringLit(Baba))
	VarDecl(j, StringType, StringLit(Mama))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(k), BinExpr(::, Id(j), Id(i))), AssignStmt(Id(t), BinExpr(::, BinExpr(::, Id(k), Id(j)), Id(i))), AssignStmt(Id(l), BinExpr(::, Id(k), BinExpr(::, Id(j), Id(i)))), CallStmt(printString, Id(t)), CallStmt(printString, Id(l))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    def test_351(self):
        input = """main: function void(){
            a[3 + 5, 2 * x] = y[4] - 7;
            return;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(3), IntegerLit(5)), BinExpr(*, IntegerLit(2), Id(x))]), BinExpr(-, ArrayCell(y, [IntegerLit(4)]), IntegerLit(7))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    def test_352(self):
        input = """main: function void(){
            a[0] = foo(2018) + goo(3);
            return;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(+, FuncCall(foo, [IntegerLit(2018)]), FuncCall(goo, [IntegerLit(3)]))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
    def test_353(self):
        input = """main: function void(){
            i: integer = 3;
            do
            {
                i = i + 1;
            }   
            while (i < 200);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(3)), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(200)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
    def test_354(self):
        input = """main: function void(){
            i: integer = 3;
            do {
                i = i + 1;
            } while (i < 20);
            printInteger(i);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(3)), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(20)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), CallStmt(printInteger, Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
    def test_355(self):
        input = """i, j, k: float = 1_23.45, 287.E20, .25e10;"""
        expect = """Program([
	VarDecl(i, FloatType, FloatLit(123.45))
	VarDecl(j, FloatType, FloatLit(2.87e+22))
	VarDecl(k, FloatType, FloatLit(2500000000.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
    def test_356(self):
        input = """foo: function void () inherit bar {
            if (a < b)
                if (c < d)
                    printString("True");
                else
                    printString("False");
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], bar, BlockStmt([IfStmt(BinExpr(<, Id(a), Id(b)), IfStmt(BinExpr(<, Id(c), Id(d)), CallStmt(printString, StringLit(True)), CallStmt(printString, StringLit(False))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_357(self):
        input = """main: function void () {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
    def test_358(self):
        input = """x: integer = 2018;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        decr: function void(out n: integer, delta: integer) {
            n = n - delta;
        }
        main: function void() {
            delta: integer = fact(3_2);
            decr(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2018))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(decr, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(-, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(32)])), CallStmt(decr, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
    def test_359(self):
        input = """main: function void () {
            a: array [2, 2] of float;
            i, j: integer;
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 2, j + 1) {
                    a[i, j] = readFloat();
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(i, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i), Id(j)]), FuncCall(readFloat, []))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    def test_360(self):
        input = """main: function void () {
            a: array [2, 2] of float;
            i, j: integer;
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 2, j + 1) {
                    a[i, j] = readFloat();
                }
            }
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 2, j + 1) {
                    printFloat(a[i, j]);
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(i, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i), Id(j)]), FuncCall(readFloat, []))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printFloat, ArrayCell(a, [Id(i), Id(j)]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    def test_361(self):
        input = """x: integer = 2018;
        fibo: function integer (n: integer) {
            if (n <= 1) return 1;
            else return fibo(n - 1) + fibo(n - 2);
        }
        decr: function void(out n: integer, delta: integer) {
            n = n - delta;
        }
        main: function void() {
            delta: integer = fibo(100);
            decr(x, delta);
            printInteger(x);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(2018))
	FuncDecl(fibo, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(+, FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fibo, [BinExpr(-, Id(n), IntegerLit(2))]))))]))
	FuncDecl(decr, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(-, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fibo, [IntegerLit(100)])), CallStmt(decr, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
    def test_362(self):
        input = """main: function void() {
            a[0] = b[2, 3] + foo(2) + (b[0, 1] + goo(1));
            return;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(+, BinExpr(+, ArrayCell(b, [IntegerLit(2), IntegerLit(3)]), FuncCall(foo, [IntegerLit(2)])), BinExpr(+, ArrayCell(b, [IntegerLit(0), IntegerLit(1)]), FuncCall(goo, [IntegerLit(1)])))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    def test_363(self):
        input = """a: integer = 20;
                   b: float = a;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(20))
	VarDecl(b, FloatType, Id(a))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))
    def test_364(self):
        input = """x: array [3] of float = {1.0, 2.0, 3.0};
                   a: float = x[0] + x[1] + x[2];"""
        expect = """Program([
	VarDecl(x, ArrayType([3], FloatType), ArrayLit([FloatLit(1.0), FloatLit(2.0), FloatLit(3.0)]))
	VarDecl(a, FloatType, BinExpr(+, BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(x, [IntegerLit(1)])), ArrayCell(x, [IntegerLit(2)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
    def test_365(self):
        input = """x: array [2, 3] of integer = {{1, 5, 8}, {2, 9, 6}};
                   a: integer = x[0, 0] + x[0, 1] + x[0, 2] - x[1, 0] - x[1, 1] - x[1, 2];"""
        expect = """Program([
	VarDecl(x, ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(5), IntegerLit(8)]), ArrayLit([IntegerLit(2), IntegerLit(9), IntegerLit(6)])]))
	VarDecl(a, IntegerType, BinExpr(-, BinExpr(-, BinExpr(-, BinExpr(+, BinExpr(+, ArrayCell(x, [IntegerLit(0), IntegerLit(0)]), ArrayCell(x, [IntegerLit(0), IntegerLit(1)])), ArrayCell(x, [IntegerLit(0), IntegerLit(2)])), ArrayCell(x, [IntegerLit(1), IntegerLit(0)])), ArrayCell(x, [IntegerLit(1), IntegerLit(1)])), ArrayCell(x, [IntegerLit(1), IntegerLit(2)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    def test_366(self):
        input = """a: auto;"""
        expect = """Program([
	VarDecl(a, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
    def test_367(self):
        input = """x: integer;
        y: float;
        z: boolean;
        goo: function void(x: integer, y: float) {
        
        }
        t: array[10] of float;
        foo: function auto() {
            
        }
        a: string = \"Hello World\";"""
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, FloatType)
	VarDecl(z, BooleanType)
	FuncDecl(goo, VoidType, [Param(x, IntegerType), Param(y, FloatType)], None, BlockStmt([]))
	VarDecl(t, ArrayType([10], FloatType))
	FuncDecl(foo, AutoType, [], None, BlockStmt([]))
	VarDecl(a, StringType, StringLit(Hello World))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
    def test_368(self):
        input = """a, b, c: auto = 29, 1.25, true;"""
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(29))
	VarDecl(b, AutoType, FloatLit(1.25))
	VarDecl(c, AutoType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))
    def test_369(self):
        input = """foo1: function void(inherit out a: integer) inherit foo {
            super(x, y, z);
        }"""
        expect = """Program([
	FuncDecl(foo1, VoidType, [InheritOutParam(a, IntegerType)], foo, BlockStmt([CallStmt(super, Id(x), Id(y), Id(z))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
    def test_370(self):
        input = """x: integer = 20;
        y: integer = 2 * x + 1;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(20))
	VarDecl(y, IntegerType, BinExpr(+, BinExpr(*, IntegerLit(2), Id(x)), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
    def test_371(self):
        input = """x: auto = 20;
        y: auto = x * 0.25;"""
        expect = """Program([
	VarDecl(x, AutoType, IntegerLit(20))
	VarDecl(y, AutoType, BinExpr(*, Id(x), FloatLit(0.25)))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
    def test_372(self):
        input = """foo: function array [3] of integer(a: array [3] of integer) {
            return a;
        }"""
        expect = """Program([
	FuncDecl(foo, ArrayType([3], IntegerType), [Param(a, ArrayType([3], IntegerType))], None, BlockStmt([ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))
    def test_373(self):
        input = """foo: function boolean () {}"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
    def test_374(self):
        input = """x, y, z, t: auto = 2, false, true, 3.75e10;"""
        expect = """Program([
	VarDecl(x, AutoType, IntegerLit(2))
	VarDecl(y, AutoType, BooleanLit(False))
	VarDecl(z, AutoType, BooleanLit(True))
	VarDecl(t, AutoType, FloatLit(37500000000.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
    def test_375(self):
        input = """x, y, z, t, u: auto = 2, false, true, -.e23, \"Hello\";"""
        expect = """Program([
	VarDecl(x, AutoType, IntegerLit(2))
	VarDecl(y, AutoType, BooleanLit(False))
	VarDecl(z, AutoType, BooleanLit(True))
	VarDecl(t, AutoType, UnExpr(-, FloatLit(0.0)))
	VarDecl(u, AutoType, StringLit(Hello))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
    def test_376(self):
        input = """foo: function void (a: integer, b: integer, c: integer) {
            printInteger(a + 2 * b + 3 * c);
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType), Param(c, IntegerType)], None, BlockStmt([CallStmt(printInteger, BinExpr(+, BinExpr(+, Id(a), BinExpr(*, IntegerLit(2), Id(b))), BinExpr(*, IntegerLit(3), Id(c))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    def test_377(self):
        input = """foo: function void (a: integer, b: integer, c: integer) {
            printInteger(a + 2 * b + 3 * c);
        }
        main: function void() {
            foo(2, 3, 4);
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType), Param(c, IntegerType)], None, BlockStmt([CallStmt(printInteger, BinExpr(+, BinExpr(+, Id(a), BinExpr(*, IntegerLit(2), Id(b))), BinExpr(*, IntegerLit(3), Id(c))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(2), IntegerLit(3), IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
    def test_378(self):
        input = """foo: function void (a: integer, b: integer) {
            c: integer = 2018;
            printInteger(a + 2 * b + 3 * c);
        }
        main: function void() {
            foo(2, 3);
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([VarDecl(c, IntegerType, IntegerLit(2018)), CallStmt(printInteger, BinExpr(+, BinExpr(+, Id(a), BinExpr(*, IntegerLit(2), Id(b))), BinExpr(*, IntegerLit(3), Id(c))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, IntegerLit(2), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    def test_379(self):
        input = """foo: function void (a: integer, b: integer) {
            printInteger(a + b);
            return;
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([CallStmt(printInteger, BinExpr(+, Id(a), Id(b))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
    def test_380(self):
        input = """foo: function void (a: integer, b: integer) {
            i: integer;
            for (i = a, i <= b, i + 1) {
                c: integer = a + i;
                printInteger(c);
            }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), Id(a)), BinExpr(<=, Id(i), Id(b)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(c, IntegerType, BinExpr(+, Id(a), Id(i))), CallStmt(printInteger, Id(c))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
    def test_381(self):
        input = """foo: function void () {
            do
            {
                printInteger(1);
            }   
            while (true);
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([CallStmt(printInteger, IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))
    def test_382(self):
        input = """foo: function void () {
            while (true)
                break;
            return;
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BreakStmt()), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))
    def test_383(self):
        input = """foo: function void () {
            if (true) {
                if (!true) {
                    
                }
                else return;
            }
            return;
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([IfStmt(UnExpr(!, BooleanLit(True)), BlockStmt([]), ReturnStmt())])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
    def test_384(self):
        input = """foo: function void () {
            if (!true) {
                if (true) {
                    a: integer = 10;
                    a = a + 1;
                    return;
                }
                else
                    return;
            }
            else {
                a: integer = 1;
                while (a < 20)
                    a = a + 1;
                printInteger(a);
            }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(UnExpr(!, BooleanLit(True)), BlockStmt([IfStmt(BooleanLit(True), BlockStmt([VarDecl(a, IntegerType, IntegerLit(10)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), ReturnStmt()]), ReturnStmt())]), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), WhileStmt(BinExpr(<, Id(a), IntegerLit(20)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))), CallStmt(printInteger, Id(a))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
    def test_385(self):
        input = """foo: function array [10] of integer(a: array [10] of integer) {
            i: integer;
            for (i = 0, i < 10, i + 1) {
                a[i] = a[i] * 2 + 1;
            }
            return a;
        }"""
        expect = """Program([
	FuncDecl(foo, ArrayType([10], IntegerType), [Param(a, ArrayType([10], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(+, BinExpr(*, ArrayCell(a, [Id(i)]), IntegerLit(2)), IntegerLit(1)))])), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
    def test_386(self):
        input = """foo: function void (out N: integer, i: integer) {
            j: integer;
            for (j = 0, j < i, j + 1) {
                if (N % j == 0) {
                    N = N - j;
                }
            }
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [OutParam(N, IntegerType), Param(i, IntegerType)], None, BlockStmt([VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(N), Id(j)), IntegerLit(0)), BlockStmt([AssignStmt(Id(N), BinExpr(-, Id(N), Id(j)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
    def test_387(self):
        input = """foo1: function void (out N: integer, i: integer) {
            N = N * i;
        }
        main: function void() {
            N: integer = 2018;
            foo1(N, 3);
            printInteger(N);
        }"""
        expect = """Program([
	FuncDecl(foo1, VoidType, [OutParam(N, IntegerType), Param(i, IntegerType)], None, BlockStmt([AssignStmt(Id(N), BinExpr(*, Id(N), Id(i)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(N, IntegerType, IntegerLit(2018)), CallStmt(foo1, Id(N), IntegerLit(3)), CallStmt(printInteger, Id(N))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
    def test_388(self):
        input = """foo1: function void (out s: string, N: integer) {
            i: integer;
            for (i = 0, i < N, i + 1) {
                temp: string = s[N - i - 1];
                s[N - i - 1] = s[i];
                s[i] = temp;
            }
        }"""
        expect = """Program([
	FuncDecl(foo1, VoidType, [OutParam(s, StringType), Param(N, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(N)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(temp, StringType, ArrayCell(s, [BinExpr(-, BinExpr(-, Id(N), Id(i)), IntegerLit(1))])), AssignStmt(ArrayCell(s, [BinExpr(-, BinExpr(-, Id(N), Id(i)), IntegerLit(1))]), ArrayCell(s, [Id(i)])), AssignStmt(ArrayCell(s, [Id(i)]), Id(temp))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
    def test_389(self):
        input = """foo1: function void (s: string, N: integer) {
            i: integer;
            for (i = 0, i < N / 2, i + 1) {
                temp: string = s[N - i - 1];
                s[N - i - 1] = s[i];
                s[i] = temp;
            }
            printString(s);
        }
        main: function void() {
            foo1(\"Hello, this is me\", 17);
        }"""
        expect = """Program([
	FuncDecl(foo1, VoidType, [Param(s, StringType), Param(N, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(N), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(temp, StringType, ArrayCell(s, [BinExpr(-, BinExpr(-, Id(N), Id(i)), IntegerLit(1))])), AssignStmt(ArrayCell(s, [BinExpr(-, BinExpr(-, Id(N), Id(i)), IntegerLit(1))]), ArrayCell(s, [Id(i)])), AssignStmt(ArrayCell(s, [Id(i)]), Id(temp))])), CallStmt(printString, Id(s))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo1, StringLit(Hello, this is me), IntegerLit(17))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
    def test_390(self):
        input = """a: integer = foo(2018) + goo(2018);"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(2018)]), FuncCall(goo, [IntegerLit(2018)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    def test_391(self):
        input = """foo: function boolean (inherit out a: integer, b: float) inherit goo {}"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [InheritOutParam(a, IntegerType), Param(b, FloatType)], goo, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
    def test_392(self):
        input = """foo: function boolean (a: integer, b: float) {
            i: integer;
            for (i = 0, i < 5, i + 1) {
                x, y, z: integer = 10, 20, 30;
                return (x + a + y + b) > (y + a + z + b);
            }
        }"""
        expect = """Program([
	FuncDecl(foo, BooleanType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(x, IntegerType, IntegerLit(10)), VarDecl(y, IntegerType, IntegerLit(20)), VarDecl(z, IntegerType, IntegerLit(30)), ReturnStmt(BinExpr(>, BinExpr(+, BinExpr(+, BinExpr(+, Id(x), Id(a)), Id(y)), Id(b)), BinExpr(+, BinExpr(+, BinExpr(+, Id(y), Id(a)), Id(z)), Id(b))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))
    def test_393(self):
        input = """foo1: function void (a: integer, b: float) {
            c: float = a + b;
            printFloat(c);
        }"""
        expect = """Program([
	FuncDecl(foo1, VoidType, [Param(a, IntegerType), Param(b, FloatType)], None, BlockStmt([VarDecl(c, FloatType, BinExpr(+, Id(a), Id(b))), CallStmt(printFloat, Id(c))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
    def test_394(self):
        input = """foo2: function void (a: integer) {
            printString(\"Test\");
            a = a + 1;
            printInteger(a);
        }
        main: function void() {
            foo2(10);
        }"""
        expect = """Program([
	FuncDecl(foo2, VoidType, [Param(a, IntegerType)], None, BlockStmt([CallStmt(printString, StringLit(Test)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), CallStmt(printInteger, Id(a))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo2, IntegerLit(10))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
    def test_395(self):
        input = """a,b,c: boolean=true, false, true;"""
        expect = """Program([
	VarDecl(a, BooleanType, BooleanLit(True))
	VarDecl(b, BooleanType, BooleanLit(False))
	VarDecl(c, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
    def test_396(self):
        input = """foo: function void() {
            if (true)
            {
                a, b, c: integer = 10, 20, 30;
                printInteger(a + b + c);
            }
            else
            {
                x, y: float = 2.3e2, -2.3e2;
                printFloat(x + y);
            }   
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([VarDecl(a, IntegerType, IntegerLit(10)), VarDecl(b, IntegerType, IntegerLit(20)), VarDecl(c, IntegerType, IntegerLit(30)), CallStmt(printInteger, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)))]), BlockStmt([VarDecl(x, FloatType, FloatLit(230.0)), VarDecl(y, FloatType, UnExpr(-, FloatLit(230.0))), CallStmt(printFloat, BinExpr(+, Id(x), Id(y)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    def test_397(self):
        input = """a_20: boolean = (2 < 3) < 4;"""
        expect = """Program([
	VarDecl(a_20, BooleanType, BinExpr(<, BinExpr(<, IntegerLit(2), IntegerLit(3)), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
    def test_398(self):
        input = """foo: function string (a: string, b: integer) {
            return (a :: a[b]);
        }"""
        expect = """Program([
	FuncDecl(foo, StringType, [Param(a, StringType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(a), ArrayCell(a, [Id(b)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    def test_399(self):
        input = """x: integer = 65;
        y: function integer(x: integer) {
            return x + 1;
        }
        z: float = 65.20;
        t: function float(z: float) {
            return z * 2.0;
        }
        main: function void() {
            y: integer = y(x);
            t: float = t(z);
            printInteger(y);
            printFloat(t);
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(y, IntegerType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(x), IntegerLit(1)))]))
	VarDecl(z, FloatType, FloatLit(65.2))
	FuncDecl(t, FloatType, [Param(z, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(z), FloatLit(2.0)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(y, IntegerType, FuncCall(y, [Id(x)])), VarDecl(t, FloatType, FuncCall(t, [Id(z)])), CallStmt(printInteger, Id(y)), CallStmt(printFloat, Id(t))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

