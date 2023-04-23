import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400 (self):
        input = """
        foo1: function void (c: integer) inherit foo
        {
            super(b, c);
        }
        foo: function void (a: integer, inherit b: auto) {
        
        }
        foo2: function void (x: integer) inherit foo1
        {
            super(b);
        }
        main: function void() {
        
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 400))
    def test_401 (self):
        input = """
        a: integer = foo(1, 2) + 1;
        foo: function auto (a: auto, b: auto)
        {
            return a + b;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))
    def test_402 (self):
        input = input = """i, j, t: string = \"20\", \"30\", \"40\";
        main: function void()
        {
            k = j :: (i :: t);
            printString(k);
        }"""
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test_403 (self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test_404 (self):
        input = """
        foo: function integer (inherit x: integer, y: integer)
        {
            
        }
        foo1: function integer(z: string) inherit foo
        {
            super(x, y);
        }
        main: function void() {
        
        }"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test_405 (self):
        input = """x, y: boolean = true, foo(1, 2);
        foo: function auto (x: auto, y: integer)
        {
            return x == y;
        }
        goo: function void(a: auto)
        {
            
        }
        main: function void() {
            goo(2018);
            goo(3.75);
        }"""
        expect = "Type mismatch in statement: CallStmt(goo, FloatLit(3.75))"
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test_406 (self):
        input = """
        foo: function auto (a: auto, b: integer)
        {
            a = a + b;
            return a;
        }
        main: function void() {
            x: integer = foo(1.7, 2);
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, [FloatLit(1.7), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test_407 (self):
        input = """
        foo: function auto (a: auto, b: integer)
        {
            a = a + b;
            return a;
        }
        goo: function void()
        {
            x: integer = foo(1.7, 2);
        }
        main: function void() {
        
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, [FloatLit(1.7), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_408 (self):
        input = """
        foo: function auto (a: auto, b: integer)
        {
            a = a + b;
            return a;
        }
        goo: function void() inherit foo
        {
            a: integer = 1;
            super(1, 2);
        }
        main: function void() {
        
        }"""
        expect = "Invalid statement in function: goo"
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_409 (self):
        input = """
        inc : function void (out n : integer, a: float) inherit foo {} 
        foo : function auto (inherit n: float, n: integer){} 
        main: function void()
        {
        
        }"""
        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_410 (self):
        input = """
        foo: function void (inherit a: integer, a: float) inherit bar {}
        main: function void()
        {
        
        }"""
        expect = "Undeclared Function: bar"
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test_411 (self):
        input = """
        foo: function void() inherit foo1{
            super("HCMUT", true);
            x = 7;
        }
        foo1: function void (inherit x: string, inherit x: boolean) {}
        main: function void() {}"""
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test_412 (self):
        input = """
        foo: function integer() {
            foo: integer = 2018;
        }
        main: function void() {
	        foo: integer = foo();
        }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [])"
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test_413 (self):
        input = """
        foo: function auto (a: auto, b: integer)
        {
            return a + b;
        }
        a: integer = foo(1, 2) + 1;
        main: function void() {
            a = foo(1.1, 2);
        }"""
        expect = "Type mismatch in expression: FuncCall(foo, [FloatLit(1.1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test_414 (self):
        input = """
        x: auto = x + 4.7;
        foo: function void(a: integer) {}
        main: function void() {
            foo(x);
        }"""
        expect = "Type mismatch in statement: CallStmt(foo, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test_415 (self):
        input = """
        foo: function void(a: integer) {}
        foo: integer = 2;
        main: function void() {
        
        }"""
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input, expect, 415))
    def test_416 (self):
        input = """
        foo: function void (b: integer) inherit a {
            preventDefault();
        }
        a: function string (inherit c: string) {}
        a: integer = 1;
        main: function void() {}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 416))
    def test_417 (self):
        input = """
        foo: function auto (a: integer) {
            if (a < 10)
            {
                return a;
            }
            else
            {
                return 3.25;
            }
        }
        main: function void() {}
        """
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(3.25))"
        self.assertTrue(TestChecker.test(input, expect, 417))
    def test_418 (self):
        input = """
        main: function void(){
            a: integer = func1() + 2.2;
        }
        func1: function auto(){
            return "string";
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(StringLit(string))"
        self.assertTrue(TestChecker.test(input, expect, 418))
    def test_419 (self):
        input = """
        main: function void(){
            a: integer = func1() + 2;
        }
        func1: function auto() inherit foo {
            return 0;
        }
        foo: function integer(){
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))
    def test_420 (self):
        input = """
        func1: function auto() inherit foo {
            super(20);
            x: integer = 20;
        }
        foo: function integer(inherit x: integer) {
            
        }
        main: function void(){
            a: integer = func1() + 2;
        }"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 420))
    def test_421 (self):
        input = """
        func1: function auto(a: integer) inherit foo {
            super(20);
            return a;
        }
        foo: function integer(inherit x: integer) {
            
        }
        main: function void(){
            a: integer = func1() + 2;
        }"""
        expect = "Type mismatch in expression: FuncCall(func1, [])"
        self.assertTrue(TestChecker.test(input, expect, 421))
    def test_422 (self):
        input = """
        fact: function integer (n: integer) {
            fact(2018);
        }
        main: function void() {
            delta: integer = fact(3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
    def test_423 (self):
        input = """
        fact: function integer (n: integer) {
            if (n <= 1)
            {
                return 1;
            }
            return fact(n - 1) + fact(n - 2);
        }
        main: function void() {
            delta: integer = fact(3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test_424 (self):
        input = """
        foo: function auto () {
            return 2018;
        }
        main: function void() {
            delta: integer = foo();
            printInteger(delta);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test_425 (self):
        input = """
        x: boolean = true;
        foo: function auto () {
            return x;
        }
        main: function void() {
            delta: integer = foo();
            printInteger(delta);
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(delta, IntegerType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test_426 (self):
        input = """
        x: boolean = true;
        foo: function auto () {
            return x;
        }"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 426))
    def test_427 (self):
        input = """
        x: integer = 3;
        a: integer = readInteger();
        fact: function integer() 
        {
            
        }
        foo: function auto () {
            return a;
        }
        main: function void() {
            x = foo();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test_428 (self):
        input = """
        foo : function void (a : auto){}                  // Line 1
        main : function void () {
            foo(true);                                    // Line 3
            goo();                                        // Line 4
        }
        goo : function void (){                           // Line 6                    
            foo(3);                                       // Line 7
        } """
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 428))
    def test_429 (self):
        input = """
        foo: function void (a : auto) {}
        main: function void () {
            foo(2018);
            goo();
        }
        goo: function void (){                    
            foo(3);
        } """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test_430 (self):
        input = """
        foo: function void (a: auto) inherit goo {
            preventDefault();
        }
        main: function void () {
            foo(2018);
            goo(20);
        }
        goo: function void (inherit a: integer){                 
            foo(3);
        } """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_431 (self):
        input = """
        foo: function void (a: auto) inherit goo {
            preventDefault();
            b = b + 1;
        }
        main: function void () {
            foo(2018);
            goo(20, 1998);
        }
        goo: function void (inherit a: integer, inherit b: integer){                 
            foo(3);
        } """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test_432 (self):
        input = """
        a: array [3, 2] of integer = {{1, "2"}, {1, 2}, {1, 2}};
        main: function void () {
            
        }"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), StringLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_433 (self):
        input = """
        foo: function integer(a: auto)
        {
            if (a < 20)
            {
                return 1;
            }
            return 2.7;
        }
        main: function void () {
            
        }"""
        expect = "Type mismatch in statement: ReturnStmt(FloatLit(2.7))"
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_434 (self):
        input = """
        foo: function integer(a: auto) inherit foo1
        {
            preventDefault();
            if (a < 20)
            {
                x: integer = 5;
                return x;
            }
            return 3;
        }
        foo1: function integer(inherit x: integer)
        {
            preventDefault();
        }
        main: function void () {
            
        }"""
        expect = "Invalid statement in function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test_435 (self):
        input = """
        foo: function integer(a: auto) inherit foo1
        {
            preventDefault();
            x: integer = 20;
            if (a < 20)
            {
                x: integer = 5;
                return x;
            }
            return x;
        }
        foo1: function integer(inherit x: integer)
        {
            
        }
        main: function void () {
            
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test_436 (self):
        input = """
        main : function void() inherit foo {
            super(1.0, 2.0, 3.0);
            z: integer = foo(1, 2, 3) + 1;
            x = "abc";
            y = true;
        }
        foo : function auto(inherit x: auto, inherit y: auto, z: auto){
            return x + y + z;
        }"""
        expect = "Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test_437 (self):
        input = """
        main:function void() inherit foo {
            super(12);
            x:auto = foo(1);
            foo2();
            arr: array[2,2] of integer = {{1, 2.7}, {1,2}};
            arr[1,2] = 1;
        }
        foo:function float (x: integer){
            return x + 1.2;
        }
        foo2: function void(){}"""
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), FloatLit(2.7)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_438 (self):
        input = """
        foo : function void() {}
        foo : function auto ( a : integer , b : integer ) inherit bar {}
        main: function void() {}"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_439 (self):
        input = """
        a: auto = foo(1, 2);
        foo: function auto() { }
        main: function void() {}"""
        expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test_440 (self):
        input = """
        x: auto = {4,5,6};
        y: auto = x[1,2];
        main: function void() {}"""
        expect = "Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_441 (self):
        input = """
        foo: function float (out z: auto, t: auto)
        {
            z = 5;
            return z + t;
        }
        main: function void() {
            a: auto = foo(2.0, 2);
            b: auto = foo(3.0, 1);
            c: float = a + b;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test_442 (self):
        input = """
        foo: function boolean (n: integer)
        {
            if (n < 2)
            {
                return false;
            }
            if (n % 2 == 0)
            {
                return n == 2;
            }
            i: integer;
            for (i = 2, i * i <= n, 1)
            {
                if (n % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
        main: function void() {
            n: integer = readInteger();
            printBoolean(foo(n));
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test_443 (self):
        input = """
        main: function void() {
            n: integer = readInteger();
            printBoolean(foo(n));
        }
        foo: function void(n: integer) {}"""
        expect = "Type mismatch in expression: FuncCall(foo, [Id(n)])"
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_444 (self):
        input = """
        main: function void() {
            n: integer = readInteger();
            if (foo(n))
            {
                printInteger(n);
            }
            else
            {
                printInteger(1 + n);
            }
        }
        foo: function boolean(n: integer) {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_445 (self):
        input = """
        main: function void() {
            n: float = readInteger();
            if (foo(n) && foo(n + 1))
            {
                printInteger(n);
            }
            else
            {
                printInteger(1 + n);
            }
        }
        foo: function boolean(n: float) {}"""
        expect = "Type mismatch in statement: CallStmt(printInteger, Id(n))"
        self.assertTrue(TestChecker.test(input, expect, 445))
    def test_446 (self):
        input = """
        foo: function auto(a: auto, b: string) inherit bar {
            super(1, a, bar()); // 1
        }
        bar: function auto (x: auto, y: boolean, z: float) {}
        main: function void() {}"""
        expect = "Type mismatch in expression: FuncCall(bar, [])"
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_447 (self):
        input = """
        foo: integer = 2018;
        foo1: function auto()
        {
            return foo;
        }
        main: function void()
        {
            foo: auto = foo1();
            printBoolean(foo);
        }"""
        expect = "Type mismatch in statement: CallStmt(printBoolean, Id(foo))"
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_448(self):
        input = """i, j, k: integer = 20, 30, 40;
        main: function void()
        {
            i = j + k;
            printInteger(i);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_449(self):
        input = """i, j, k: float = 2.75, 1.98, 3.17;
        main: function void()
        {
            t = i + j + k;
            printFloat(t);
        }"""
        expect = """Undeclared Identifier: t"""
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_450(self):
        input = """i, j: string = \"Baba\", \"Mama\";
        main: function void()
        {
            k = j :: i;
            t = (k :: j) :: i;
            l = k :: (j :: i);
            printString(t);
            printString(l);
        }"""
        expect = """Undeclared Identifier: k"""
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test_451(self):
        input = """main: function void(){
            a[3 + 5, 2 * x] = y[4] - 7;
            return;
        }"""
        expect = """Undeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_452(self):
        input = """
        a: integer = 20;
        a: function void() {
            x: integer = 3;
        }"""
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test_453(self):
        input = """main: function void(){
            i: integer = 3;
            do
            {
                i = i + 1;
            }   
            while (i < 200);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_454(self):
        input = """main: function void(){
            i: integer = 3;
            do {
                i = i + 1;
            } while (i < 20);
            printInteger(i);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test_455(self):
        input = """a: array[3] of float = {1, 2, 3};
        main: function void() {
            
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_456(self):
        input = """foo: function void () inherit bar {
            if (a < b)
                if (c < d)
                    printString("True");
                else
                    printString("False");
        }
        main: function void() {}
        bar: integer = 2;"""
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test_457(self):
        input = """main: function auto () { return; }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test_458(self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test_459(self):
        input = """main: function void () {
            a: array [2, 2] of float;
            i, j: integer;
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 2, j + 1) {
                    a[i, j] = readFloat();
                }
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test_460(self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test_461(self):
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
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test_462(self):
        input = """main: function void() {
            a[0] = b[2, 3] + foo(2) + (b[0, 1] + goo(1));
            return;
        }"""
        expect = """Undeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test_463(self):
        input = """a: integer = foo();
        foo: function string() { }
        main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test_464(self):
        input = """a : integer = foo(1, 2);
        foo : function float (a : auto, b: auto) {
            a = "abc";
            b = "bcd";
            return a + b;
        }
        main: function void() {}"""
        expect = """Type mismatch in statement: AssignStmt(Id(a), StringLit(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test_465(self):
        input = """a : integer = foo(1, 2);
        foo : function integer (a : auto, b: auto) {
            x: auto = a + b;
            return x;
        }
        main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test_466(self):
        input = """a: auto;
        main: function void() {}"""
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 466))
    def test_467(self):
        input = """x: integer;
        y: float;
        z: boolean;
        goo: function void(x: integer, y: float) {
        
        }
        t: array[10] of float;
        foo: function auto() {
            
        }
        a: string = \"Hello World\";"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 467))
    def test_468(self):
        input = """
        x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
        y: auto = x[0, 1+1-0];
        main: function void() {
            
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
    def test_469(self):
        input = """
        goo: function void(a: auto, b: auto)
        {
            x: string = a + b;
        }
        main: function void() {}
        foo1: function void(inherit out a: integer) inherit foo {
            super(x, y, z);
        }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, BinExpr(+, Id(a), Id(b)))"""
        self.assertTrue(TestChecker.test(input, expect, 469))
    def test_470(self):
        input = """foo: function integer () {return 1;}
        x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
        y: auto = x[1, foo()];"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test_471(self):
        input = """x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
        y: auto = x[2 < 3];
        main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(<, IntegerLit(2), IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test_472(self):
        input = """
        a: function integer (a: integer)
        {
            if (a <= 1)
            {
                return a;
            }
            return a(a - 1) + a(a - 2);
        }
        main: function void()
        {
            printInteger(a(2018));
        }"""
        expect = """Type mismatch in expression: FuncCall(a, [BinExpr(-, Id(a), IntegerLit(1))])"""
        self.assertTrue(TestChecker.test(input, expect, 472))
    def test_473(self):
        input = """
        a: float = foo(1, 2) + 1.5;
        foo: function auto(a: integer, b: integer) {
            return a + b; 
        }
        main: function void() {}"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test_474(self):
        input = """
        main: function void () {
            a: integer = foo();//1
            b: float = "Error";//2
        }
        foo: function auto() {
            c: float = "Error";//3
            if("Error")//4
                return 123;//5
            else
                return 456;//6
            return "123"; //7
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(c, FloatType, StringLit(Error))"
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test_475(self):
        input = """
        func1: function auto (d: integer, c: integer, e: auto) {
            g: integer = -e;
            f: integer = e;
        }
        main: function void () {
            a: integer = func1(2, 3, 2.9);
        }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(g, IntegerType, UnExpr(-, Id(e)))"""
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test_476(self):
        input = """foo: function void(b: auto, c: auto)
        {
            a: integer = b + c == c;
        }
        main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(==, BinExpr(+, Id(b), Id(c)), Id(c)))"""
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test_477(self):
        input = """foo: function void (a: integer, b: integer, c: integer) {
            printInteger(a + 2 * b + 3 * c);
        }
        main: function void() {
            foo(2, 3, 4);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test_478(self):
        input = """foo: function void (a: integer, b: integer) {
            c: integer = 2018;
            printInteger(a + 2 * b + 3 * c);
        }
        main: function void() {
            foo(2, 3);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test_479(self):
        input = """
        foo: function auto (b: integer, b: float) { 
	        return 3;
	        return "hello";
	        a: string = 123;
        }
        main: function void() {}"""
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test_480(self):
        input = """foo: function void (a: integer, b: integer) {
            i: integer;
            for (i = a, i <= b, i + 1) {
                c: integer = a + i;
                printInteger(c);
            }
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 480))
    def test_481(self):
        input = """foo: function void () {
            do
            {
                printInteger(1);
            }   
            while (true);
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 481))
    def test_482(self):
        input = """foo: function void () {
            while (true)
                break;
            return;
        }
        main: function void() {
            
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
    def test_483(self):
        input = """foo: function void () {
            if (true) {
                if (!true) {
                    
                }
                else return;
            }
            return;
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 483))
    def test_484(self):
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
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 484))
    def test_485(self):
        input = """foo: function array [10] of integer(a: array [10] of integer) {
            i: integer;
            for (i = 0, i < 10, i + 1) {
                a[i] = a[i] * 2 + 1;
            }
            return a;
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 485))
    def test_486(self):
        input = """foo: function void (out N: integer, i: integer) {
            j: integer;
            for (j = 0, j < i, j + 1) {
                if (N % j == 0) {
                    N = N - j;
                }
            }
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 486))
    def test_487(self):
        input = """foo1: function void (out N: integer, i: integer) {
            N = N * i;
        }
        main: function void() {
            N: integer = 2018;
            foo1(N, 3);
            printInteger(N);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))
    def test_488(self):
        input = """foo1: function void (out s: string, N: integer) {
            i: integer;
            for (i = 0, i < N, i + 1) {
                temp: string = s[N - i - 1];
                s[N - i - 1] = s[i];
                s[i] = temp;
            }
        }
        main: function void() {}"""
        expect = """Type mismatch in expression: ArrayCell(s, [BinExpr(-, BinExpr(-, Id(N), Id(i)), IntegerLit(1))])"""
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test_489(self):
        input = """
        inc : function void (a : integer) inherit foo{
            super("aa",2);
            a = 1::2;
        }
        foo : function auto (inherit n: float, inherit n: integer){

        }
        main: function void() {
            
        }"""
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input, expect, 489))
    def test_490(self):
        input = """
        test1 : function string(y : auto) {
            y = 2; // line 2
            return "";
        }
        main: function void () {
            x: string = test1(true); // line 6
        }"""
        expect = """Type mismatch in statement: AssignStmt(Id(y), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test_491(self):
        input = """foo: function boolean (inherit out a: integer, b: float) inherit goo {}
        main: function void() {}"""
        expect = """Undeclared Function: goo"""
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test_492(self):
        input = """foo: function boolean (a: integer, b: float) {
            i: integer;
            for (i = 0, i < 5, i + 1) {
                x, y, z: integer = 10, 20, 30;
                return (x + a + y + b) > (y + a + z + b);
            }
        }
        main: function void() {
            
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test_493(self):
        input = """foo1: function void (a: integer, b: float) {
            c: float = a + b;
            printFloat(c);
        }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test_494(self):
        input = """foo2: function void (a: integer) {
            printString(\"Test\");
            a = a + 1;
            printInteger(a);
        }
        main: function void() {
            foo2(10);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_495(self):
        input = """a,b,c: boolean = true, false, true;
        main: function void() {
            a = b && c;
            printBoolean(a);
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test_496(self):
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
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 496))
    def test_497(self):
        input = """a_20: boolean = (2 < 3) < 4;
        main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(<, BinExpr(<, IntegerLit(2), IntegerLit(3)), IntegerLit(4))"""
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test_498(self):
        input = """foo: function string (a: string, b: integer) {
            return (a :: a[b]);
        }
        main: function void() {}"""
        expect = """Type mismatch in expression: ArrayCell(a, [Id(b)])"""
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test_499(self):
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
        expect = """Type mismatch in expression: FuncCall(y, [Id(x)])"""
        self.assertTrue(TestChecker.test(input, expect, 499))