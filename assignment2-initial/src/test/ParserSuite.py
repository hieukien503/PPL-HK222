import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_200(self):
        input = """i, j: string = \"20\", \"30\", \"40\";
        main: function void()
        {
            k = j :: i;
            printString(k);
        }"""
        expect = "Error on line 1 col 25: ,"
        self.assertTrue(TestParser.test(input, expect, 200))
    def test_201(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_202(self):
        input = """a, b, c, d: integer = 3, 4, 10;"""
        expect = "Error on line 1 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_203(self):
        input = """a: string = \"Hello, World\";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_204(self):
        input = """a: float = .25e+3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_205(self):
        input = """a: integer = -123456789;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_206(self):
        input = """main: function void() {
            a, b: string = "Hello", ", world!";
            c: string = a::b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_207(self):
        input = """foo: function void(out n: integer, delta: integer) {
            n = n + delta;
            return
        }"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_208(self):
        input = """fibo: function integer(n: integer) {
            if (n <= 2) return 1;
            else return fibo(n - 1) + fibo(n - 2);
        }
            main: function void( {} ) {
                printInteger(fibo(20));
        }"""
        expect = "Error on line 5 col 33: {"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_209(self):
        input = """3abc: integer;"""
        expect = "Error on line 1 col 0: 3"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_210(self):
        input = """a: array [2, 3] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_211(self):
        input = """a, b: integer = 1, 2, 3;"""
        expect = "Error on line 1 col 20: ,"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_212(self):
        input = """int i = 20;"""
        expect = "Error on line 1 col 4: i"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_213(self):
        input = """foo: function void() inherit fact { return; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_214(self):
        input = """a, for: integer;"""
        expect = "Error on line 1 col 3: for"
        self.assertTrue(TestParser.test(input, expect, 214))
    def test_215(self):
        input = """a: boolean = true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_216(self):
        input = """main: function void () {
            a: integer = 1;
            do {
                if (a > 10) {
                    break;
                }
                a = a + 1;
            }
            while (true);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_217(self):
        input = """a: array [1] of integer = {};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test_218(self):
        input = """a, b: integer = 1 / 2, 20 + 30, 30 * 20;"""
        expect = "Error on line 1 col 30: ,"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test_219(self):
        input = """a, b, c: integer = 20;"""
        expect = "Error on line 1 col 21: ;"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_220(self):
        input = """foo: function integer (inherit out a: integer) inherit foo1 {
            preventDefault();
            return a + (-2018);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    def test_221(self):
        input = """perfectNum: function boolean (N: integer) {
            if ((N == 6) || (N == 28) || (N == 496) || (N == 8128) || (N == 33550336)
            {
                return true;
            }
            return false;
        }"""
        expect = "Error on line 3 col 12: {"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test_222(self):
        input = """foo: function integer (a: integer) {
            a = a + (-2018);
            return a;
        }
        main: function void() {
            a: integer = 2018;
            a = a + foo(a);
            readInteger(a);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_223(self):
        input = """x: float;
        foo: function integer() { 
            return 0;
        }
        a: integer = 10;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_224(self):
        input = """x: float;
        foo: function integer() { 
            return 0;
        }
        goo: function void() {
            i: string;
        }
        x = 20;"""
        expect = "Error on line 8 col 10: ="
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_225(self):
        input = """x: integer = 10 - (2 + 3 * 4) / 7;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_226(self):
        input = """x: boolean = !((2 < 3) && (3 < 4));"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_227(self):
        input = """fact: function void(a: integer) {
            printInteger(a + 2018);
        }
        main: function void() {
            fact(2018)
        }"""
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_228(self):
        input = """goo: function void(a: integer, b: float) {
            c: auto = a + 2 * b;
            printInteger(c);
        }
        main: function void() {
            goo(3, 2.7);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_229(self):
        input = """goo: function string(a: array [100] of string, N: integer) {
            i: integer;
            s: string = "";
            for (i = 0, i < N, i + 1) {
                s = s :: a[i];
            }
            return s;
        }
        main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_230(self):
        input = """abc: function auto(a: integer, b: float) {
            c: auto = 2 * a + b;
            printInteger(c);
        }
        main: function void(a: float) {
            abc(1, 2.0);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_231(self):
        input = """main: function integer() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_232(self):
        input = """a29872: boolean = !(2 < 3 < 4);"""
        expect = "Error on line 1 col 26: <"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_233(self):
        input = """a, b: array [5_1, 9_6,78] of integer;
                   x: float;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_234(self):
        input = """a, b: array [5_1 / 17, 96 / 8, 78 / 39] of integer;
                   x: float = -2.95;"""
        expect = "Error on line 1 col 17: /"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_235(self):
        input = """a, b: array [2] of integer;
        main: function void() {
            a[0] = 2018;
            a[1] = -2018;
            b[0] = a[0] + a[1];
            b[1] = a[0] - a[1];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_236(self):
        input = """a: array [4] of integer;
        main: function void() {
            i: integer;
            for (i = 0, i < 4, i + 1) {
                a[i] = readInteger();
                printInteger(a[i])
            }
        }"""
        expect = "Error on line 7 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 236))
    def test_237(self):
        input = """a: array [4] of integer;
        main: function void() {
            i: integer;
            for (i = 0, i < 4, i + 1) {
                a[i] = 3 * readInteger();
                printInteger(a[i]);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_238(self):
        input = """i, j, k: integer = 20, 30;"""
        expect = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.test(input, expect, 238))
    def test_239(self):
        input = """i, j: integer = 20, 30, 40;"""
        expect = "Error on line 1 col 22: ,"
        self.assertTrue(TestParser.test(input, expect, 239))
    def test_240(self):
        input = """x: integer = 20;
        a: auto = x + 3.7;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
    def test_241(self):
        input = """void main() {}"""
        expect = "Error on line 1 col 0: void"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_242(self):
        input = """true: boolean = false;"""
        expect = "Error on line 1 col 0: true"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_243(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_244(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_245(self):
        input = """a_int: integer = 20;
        foo: function void (out a: integer) {
            a = a + 10;
        }
        main: function void() {
            foo(a_int)
            printInteger(a_int);
        }"""
        expect = "Error on line 7 col 12: printInteger"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_246(self):
        input = """foo: function array[10] of integer(a: array [10] of integer) {
            return a;
        }
        b: integer = 20;
        main: function void() { return; }
        }"""
        expect = "Error on line 6 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_247(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    def test_248(self):
        input = """i, j, k: integer = 20, 30, 40;
        main: function void()
        {
            i = j + k;
            printInteger(i);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
    def test_249(self):
        input = """i, j, k: integer = 20, 30, 40, 60;
        main: function void()
        {
            i = j + k;
            printInteger(i);
        }"""
        expect = "Error on line 1 col 29: ,"
        self.assertTrue(TestParser.test(input, expect, 249))
    def test_250(self):
        input = """i, j: string = \"Baba\", \"Mama\"
        main: function void()
        {
            k = j :: i;
            t = (k :: j) :: i;
            l = k :: (j :: i);
            printString(t);
            printString(l);
        }"""
        expect = "Error on line 2 col 8: main"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_251(self):
        input = """main: function void(){
            a[3 + 5, 2 * x] = y[4] - 7;
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))
    def test_252(self):
        input = """main: function void(){
            a[0] = foo(2018) + goo(3);
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_253(self):
        input = """main: function void(){
            i: integer = 3;
            do
            {
                i = i + 1;
            }   
            return;
        }"""
        expect = "Error on line 7 col 12: return"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_254(self):
        input = """main: function void(){
            i: integer = 3;
            do {
                i = i + 1
            } while (i < 20);
            printInteger(i);
        }"""
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_255(self):
        input = """i, j, k: float = 1_23.45, 287.E20;"""
        expect = "Error on line 1 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 255))
    def test_256(self):
        input = """main: void function () {}"""
        expect = "Error on line 1 col 6: void"
        self.assertTrue(TestParser.test(input, expect, 256))
    def test_257(self):
        input = """main: function () {}"""
        expect = "Error on line 1 col 15: ("
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_258(self):
        input = """x: integer = 2018;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        decr: function void(out n: integer, delta: integer) {
            n = n - delta;
        }
        main: function void() {
            delta: integer = fact(3_2);
            decr(x, delta);
            printInteger(x);
        }"""
        expect = "Error on line 5 col 14: function"
        self.assertTrue(TestParser.test(input, expect, 258))
    def test_259(self):
        input = """main: function void () {
            a: array [2, 2] of float;
            i, j: integer;
            for (i = 0, i < 2, i + 1) {
                for (j = 0, j < 2, j + 1) {
                    a[i, j] = readFloat();
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
    def test_260(self):
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
                    printFloat(a[i, j])
                }
            }
        }"""
        expect = "Error on line 12 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_261(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_262(self):
        input = """main: function void() {
            a[0] = b[2, 3] + foo(2) + (b[0, 1] + goo(1));
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_263(self):
        input = """a: integer = 20;
                   b: float = a;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    def test_264(self):
        input = """x: array [3] of float = {1.0, 2.0, 3.0};
                   a: float = x[0] + x[1] + x[2];"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_265(self):
        input = """x: array [2, 3] of integer = {{1, 5, 8}, {2, 9, 6}};
                   a: integer = x[0, 0] + x[0, 1] + x[0, 2] - x[1, 0] - x[1, 1] - x[1, 2];"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))
    def test_266(self):
        input = """a: auto;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
    def test_267(self):
        input = """x: integer;
        y: float;
        z: boolean;
        goo: function void(x: integer, y: float) {
        
        }
        t: array[10] of float;
        foo: function auto() {
            
        }
        a: string = \"Hello World\";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_268(self):
        input = """a, b, c: auto = 29, 1.25, true, false;"""
        expect = "Error on line 1 col 30: ,"
        self.assertTrue(TestParser.test(input, expect, 268))
    def test_269(self):
        input = """foo1: function void(inherit out a: integer) inherit foo {
            super(x, y, z);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    def test_270(self):
        input = """x: integer = 20;
        y: integer = 2 * x + 1;
        printInteger(y);"""
        expect = "Error on line 3 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_271(self):
        input = """x: auto = 20;
        y: auto = x * 0.25;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
    def test_272(self):
        input = """foo: function array [3] of integer(a: array [3] of integer) {
            return a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    def test_273(self):
        input = """foo: function boolean () {"""
        expect = "Error on line 1 col 26: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 273))
    def test_274(self):
        input = """x, y, z, t: auto = 2, false, true;"""
        expect = "Error on line 1 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_275(self):
        input = """x, y, z, t, u: auto = 2, false, true, 3.75, \"Hello\", 10_23;"""
        expect = "Error on line 1 col 51: ,"
        self.assertTrue(TestParser.test(input, expect, 275))
    def test_276(self):
        input = """foo: function void (a: integer, b: integer, c: integer) {
            printInteger(a + 2 * b + 3 * c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_277(self):
        input = """foo: function void (a: integer, b: integer, c: integer) {
            printInteger(a + 2 * b + 3 * c);
        }
        main: function void() {
            foo(2, 3, 4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    def test_278(self):
        input = """foo: function void (a: integer, b: integer) {
            c: integer = 2018;
            printInteger(a + 2 * b + 3 * c)
        }
        main: function void() {
            foo(2, 3);
        }"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 278))
    def test_279(self):
        input = """foo: function void (a: integer, b: integer) {
            goo: function void() {
                return;
            }
            return;
        }"""
        expect = "Error on line 2 col 17: function"
        self.assertTrue(TestParser.test(input, expect, 279))
    def test_280(self):
        input = """foo: function void (a: integer, b: integer) {
            i: integer;
            for (i = a, i <= b, i + 1) {
                c: integer = a + i;
                printInteger(c);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_281(self):
        input = """foo: function void () {
            do
            {
                a: integer;
            }  
            while (true);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    def test_282(self):
        input = """foo: function void () {
            while (true)
                abc: float = 20;
            return;
        }"""
        expect = "Error on line 3 col 19: :"
        self.assertTrue(TestParser.test(input, expect, 282))
    def test_283(self):
        input = """foo: function void () {
            if (true) {
                if (!true) {
                    
                }
                else return;
            }
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_284(self):
        input = """foo: function void () {
            if (!true) {
                if (true) {
                    a: integer = 10;
                    a = a + 1;
                    return;
                }
                else
                    a: float = 20;
            }
            else {
                a: integer = 1;
                while (a < 20)
                    a = a + 1;
                printInteger(a);
            }
        }"""
        expect = "Error on line 9 col 21: :"
        self.assertTrue(TestParser.test(input, expect, 284))
    def test_285(self):
        input = """foo: function array [10] of integer(a: array [10] of integer) {
            i: integer;
            for (i = 0, i < 10, i + 1) {
                a[i] = a[i] * 2 + 1;
            }
            return a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    def test_286(self):
        input = """foo: function void (out N: integer, i: integer) {
            j: integer;
            for (j = 0, j < i, j + 1) {
                if (N % j == 0) {
                    N = N - j;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
    def test_287(self):
        input = """foo1: function void (out N: integer, i: integer) {
            N = N * i;
        }
        main: function void() {
            N: integer = 2018;
            foo1(N, 3);
            printInteger(N);"""
        expect = "Error on line 7 col 28: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_288(self):
        input = """foo1: function void (out s: string, N: integer) {
            i: integer;
            for (i = 0, i < N; i + 1) {
                temp: string = s[N - i - 1];
                s[N - i - 1] = s[i];
                s[i] = temp;
            }
        }"""
        expect = "Error on line 3 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 288))
    def test_289(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    def test_290(self):
        input = """a: integer = foo(2018) + goo(2018);
        }"""
        expect = "Error on line 2 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_291(self):
        input = """foo: function boolean (a) {}"""
        expect = "Error on line 1 col 24: )"
        self.assertTrue(TestParser.test(input, expect, 291))
    def test_292(self):
        input = """foo: function boolean (a: integer; b: float) {}"""
        expect = "Error on line 1 col 33: ;"
        self.assertTrue(TestParser.test(input, expect, 292))
    def test_293(self):
        input = """foo1: function void (a: integer, b: float) {
            c: float = a + b;
            printFloat(c);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))
    def test_294(self):
        input = """foo2: function void (a: integer) {
            printString(\"Test\");
            a = a + 1;
            printInteger(a);
        }
        main: function void() {
            foo2(10);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))
    def test_295(self):
        input = """a, b, c: integer = 20_17, 2_107, 2_13_196, 0;"""
        expect = "Error on line 1 col 41: ,"
        self.assertTrue(TestParser.test(input, expect, 295))
    def test_296(self):
        input = """a: integer = 2.196;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
    def test_297(self):
        input = """a_20: boolean = (2 < 3) < 4;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_298(self):
        input = """foo: function string (a: string, b: integer) {
            return (a :: a[b]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))
    def test_299(self):
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))