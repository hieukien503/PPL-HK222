import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_500 (self):
    #     input = """
    #     main: function void()
    #     {
    #         x: integer = readInteger(); // Input 39
    #         printInteger(x);
    #     }"""
    #     expect = "39\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 500))
    # def test_501 (self):
    #     input = """
    #     foo: function auto (a: auto, b: auto)
    #     {
    #         return a + b;
    #     }
    #     a: float = foo(1.9, 2.1) + 1.5;
    #     main: function void()
    #     {
    #         printFloat(a);
    #     }"""
    #     expect = "5.5\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))
    # def test_502 (self):
    #     input = """
    #     foo: function integer (n: integer)
    #     {
    #         if (n <= 1)
    #         {
    #             return 1;
    #         }
    #         return foo(n - 1) + foo(n - 2);
    #     }
    #     main: function void()
    #     {
    #         printInteger(foo(10));
    #     }"""
    #     expect = "89\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))
    # def test_503 (self):
    #     input = """
    #     foo: function integer (a: array [5] of integer, n: integer)
    #     {
    #         if (n == 1)
    #         {
    #             return a[0];
    #         }
    #         k: integer = foo(a, n - 1);
    #         if (a[n - 1] > k)
    #         {
    #             return a[n - 1];
    #         }
    #         else
    #         {
    #             return k;
    #         }
    #     }
    #     main: function void()
    #     {
    #         a: array [5] of integer = {3, 9, -1, 2, 6};
    #         printInteger(foo(a, 5));
    #     }"""
    #     expect = "9\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))
    # def test_504 (self):
    #     input = """
    #     foo: function integer (n: integer)
    #     {
    #         if (n == 20)
    #         {
    #             return n;
    #         }
    #         else
    #         {
    #             return 20;
    #         }
    #     }
    #     main: function void()
    #     {
    #         printInteger(foo(7));
    #     }"""
    #     expect = "20\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))
    # def test_505 (self):
    #     input = """
    #     foo: function boolean (n: integer)
    #     {
    #         i: integer;
    #         for (i = 1, i < n, 1)
    #         {
    #             flag: boolean = false;
    #             j: integer;
    #             for (j = n - 1, j >= 1, -1)
    #             {
    #                 if (n % (i * j) == 0)
    #                 {
    #                     flag = true;
    #                     break;
    #                 }
    #             }
    #             if (flag == true)
    #             {
    #                 return flag;
    #             }
    #             printInteger(i);
    #         }
    #         return false;
    #     }
    #     main: function void()
    #     {
    #         printBoolean(foo(7));
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))
    # def test_506 (self):
    #     input = """
    #     main: function void()
    #     {
    #         i: integer = 0;
    #         do
    #         {
    #             if (i == 5)
    #             {
    #                 i = i + 1;
    #                 continue;
    #             }
    #             printInteger(i);
    #             i = i + 1;
    #         } while (i < 10);
    #     }"""
    #     expect = "0\n1\n2\n3\n4\n6\n7\n8\n9\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))
    # def test_507 (self):
    #     input = """
    #     foo: function void(n: integer)
    #     {
    #         printInteger(n);
    #         if (n == 1)
    #         {
    #             return;
    #         }
    #         if (n % 2 == 0)
    #         {
    #             foo(n / 2);
    #         }
    #         else
    #         {
    #             foo(3 * n + 1);
    #         }
    #     }
    #     main: function void()
    #     {
    #         foo(29);
    #     }"""
    #     expect = "29\n88\n44\n22\n11\n34\n17\n52\n26\n13\n40\n20\n10\n5\n16\n8\n4\n2\n1\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))
    # def test_508 (self):
    #     input = """
    #     main: function void()
    #     {
    #         a: integer = 0;
    #         printBoolean((a == 0) || (1 / a > 0));
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))
    # def test_509 (self):
    #     input = """
    #     main: function void()
    #     {
    #         a: integer = 0;
    #         if ((a == 0) || (1 / a > 0))
    #         {
    #             printInteger(1);
    #         }
    #         else
    #         {
    #             printInteger(0);
    #         }
    #     }"""
    #     expect = "1\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))
    # def test_510 (self):
    #     input = """
    #     foo: function void(inherit a: integer)
    #     {
    #         a = a + 1;
    #     }
    #     foo1: function void(b: integer) inherit foo
    #     {
    #         super(2);
    #         a = 2 + b;
    #         printInteger(a);
    #     }
    #     main: function void()
    #     {
    #         foo1(8);
    #     }"""
    #     expect = "10\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))
    # def test_511 (self):
    #     input = """
    #     foo: function void(inherit a: integer)
    #     {
    #         a = a + 1;
    #     }
    #     foo1: function void(b: integer) inherit foo
    #     {
    #         preventDefault();
    #         a: integer = 4 + b;
    #         if (a > 10)
    #         {
    #             printInteger(a);
    #         }
    #         else
    #         {
    #             printInteger(b);
    #         }
    #     }
    #     main: function void()
    #     {
    #         foo1(8);
    #     }"""
    #     expect = "12\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))
    # def test_512 (self):
    #     input = """
    #     gcd: function integer(a: integer, b: integer)
    #     {
    #         if (b == 0)
    #         {
    #             return a;
    #         }
    #         return gcd(b, a % b);
    #     }
    #     lcm: function integer(a: integer, b: integer)
    #     {
    #         return a * b / gcd(a, b);
    #     }
    #     main: function void()
    #     {
    #         a, b: integer = 196, 14;
    #         printInteger(gcd(a, b) + lcm(a, b));
    #     }"""
    #     expect = "210\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))
    # def test_513 (self):
    #     input = """
    #     gcd: function integer(a: integer, b: integer)
    #     {
    #         if (b == 0)
    #         {
    #             return a;
    #         }
    #         return gcd(b, a % b);
    #     }
    #     lcm: function integer(a: integer, b: integer, m: integer)
    #     {
    #         if ((m % a == 0) && (m % b == 0) && (m != 0))
    #         {
    #             return m;
    #         }
    #         return lcm(a, b, m + a);
    #     }
    #     main: function void()
    #     {
    #         a, b: integer = 196, 14;
    #         printInteger(gcd(a, b) + lcm(a, b, 0));
    #     }"""
    #     expect = "210\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))
    # def test_514 (self):
    #     input = """
    #     foo: function float(a: auto, b: auto)
    #     {
    #         return a + b;
    #     }
    #     main: function void()
    #     {
    #         printFloat(foo(2.5, 3.5));
    #     }"""
    #     expect = "6.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))
    # def test_515 (self):
    #     input = """
    #     foo: function auto(a: auto, b: auto)
    #     {
    #         if (b == true)
    #         {
    #             return a + 1;
    #         }
    #         return a;
    #     }
    #     main: function void()
    #     {
    #         printInteger(foo(2, true));
    #     }"""
    #     expect = "3\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))
    # def test_516 (self):
    #     input = """
    #     main: function void()
    #     {
    #         a: integer = readInteger(); // Input 3
    #         if (a == 3)
    #         {
    #             a: integer = 10;
    #             printInteger(a);
    #         }
    #         else
    #         {
    #             printInteger(a);
    #         }
    #     }"""
    #     expect = "10\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))
    # def test_517 (self):
    #     input = """
    #     a: float = foo(1, 2) + 1;
    #     foo: function auto(a: integer, b: auto)
    #     {
    #         return a * b;
    #     }
    #     main: function void()
    #     {
    #         printFloat(a);
    #     }"""
    #     expect = "3.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))
    # def test_518 (self):
    #     input = """
    #     foo: function auto(a: integer, b: integer)
    #     {
    #         return a * b;
    #     }
    #     a: float = foo(1, 2) + 1;
    #     main: function void()
    #     {
    #         printFloat(a);
    #     }"""
    #     expect = "3.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))
    # def test_519 (self):
    #     input = """
    #     foo: function integer(n: integer)
    #     {
    #         if (n <= 1)
    #         {
    #             return n;
    #         }
    #         a: array [100] of integer;
    #         a[0] = 0;
    #         a[1] = 1;
    #         i: integer;
    #         for(i = 2, i <= n, 1)
    #         {
    #             a[i] = a[i - 1] + a[i - 2];
    #         }
    #         return a[n];
    #     }
    #     main: function void()
    #     {
    #         printInteger(foo(20));
    #     }"""
    #     expect = "6765\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))
    # def test_520 (self):
    #     input = """
    #     main: function void()
    #     {
    #         i, j: integer;
    #         for (i = 0, i < 3, 1)
    #         {
    #             if (i == 1)
    #             {
    #                 continue;
    #             }
    #             printInteger(i);
    #         }
    #     }"""
    #     expect = "0\n2\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))
    # def test_521 (self):
    #     input = """
    #     main: function void()
    #     {
    #         i, j: integer;
    #         for (i = 0, i < 10, 1)
    #         {
    #             if (i == 5)
    #             {
    #                 continue;
    #             }
    #             printInteger(i);
    #             for (j = 0, j < 10, 1)
    #             {
    #                 if (j == 5)
    #                 {
    #                     printInteger(j);
    #                     continue;
    #                 }
    #             }
    #         }
    #     }"""
    #     expect = "0\n5\n1\n5\n2\n5\n3\n5\n4\n5\n6\n5\n7\n5\n8\n5\n9\n5\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))
    # def test_522 (self):
    #     input = """
    #     a: integer;
    #     foo: function void()
    #     {
    #         a: integer = 10;
    #         printInteger(a);
    #     }
    #     main: function void()
    #     {
    #         a: integer = 5;
    #         printInteger(a);
    #         foo();
    #     }"""
    #     expect = "5\n10\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))
    # def test_523 (self):
    #     input = """
    #     main: function void()
    #     {
    #         printBoolean((0 == 0) || (1 / 0 > 0));
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))
    # def test_524 (self):
    #     input = """
    #     main: function void()
    #     {
    #         printBoolean((0 == 1) && (1 / 0 > 0));
    #     }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))
    # def test_525 (self):
    #     input = """
    #     main: function void()
    #     {
    #         x: string = readString(); // Input "Hello"
    #         y: string = readString(); // Input "World"
    #         z: string = (x :: " ") :: y;
    #         printString(z);
    #     }"""
    #     expect = "Hello World\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))
    # def test_526 (self):
    #     input = """
    #     foo: function integer (out a: integer, b: integer)
    #     {
    #         a = a + 1;
    #         return a + b;
    #     }
    #     main: function void()
    #     {
    #         a: integer = 4;
    #         b: integer = 5;
    #         c: integer = foo(a, b);
    #         printInteger(a);
    #         printInteger(c);
    #     }"""
    #     expect = "5\n10\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))
    # def test_527 (self):
    #     input = """
    #     foo: function integer (out a: integer, out b: integer)
    #     {
    #         a = a + 1;
    #         b = b + 1;
    #         return a + b;
    #     }
    #     a: integer = 3;
    #     b: integer = 4;
    #     c: integer = foo(a, b);
    #     main: function void()
    #     {
    #         printInteger(a);
    #         printInteger(b);
    #         printInteger(c);
    #     }"""
    #     expect = "4\n5\n9\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))
    # def test_528 (self):
    #     input = """
    #     foo: function void(inherit out a: integer)
    #     {
    #         a = a + 1;
    #     }
    #     foo1: function integer(out b: integer) inherit foo
    #     {
    #         super(b);
    #         a = 28;
    #         return a + b;
    #     }
    #     main: function void()
    #     {
    #         a: integer = 3;
    #         printInteger(foo1(a));
    #         printInteger(a);
    #     }"""
    #     expect = "32\n4\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))
    # def test_529 (self):
    #     input = """
    #     a: integer = -2147483648;
    #     main: function void()
    #     {
    #         printInteger(a);
    #     }"""
    #     expect = "-2147483648\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))
    # def test_530 (self):
    #     input = """
    #     fact: function integer(a: integer)
    #     {
    #         if (a <= 1)
    #         {
    #             return 1;
    #         }
    #         return a * fact(a - 1);
    #     }
    #     main: function void()
    #     {
    #         a: integer = 11;
    #         printInteger(fact(a));
    #     }"""
    #     expect = "39916800\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))
    # def test_531 (self):
    #     input = """
    #     perfectNum: function boolean(n: integer)
    #     {
    #         if ((n == 6) || (n == 28) || (n == 496) || (n == 8128) || (n == 33550336))
    #         {
    #             return true;
    #         }
    #         return false;
    #     }
    #     main: function void()
    #     {
    #         a: integer = 28;
    #         printBoolean(perfectNum(a));
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))
    # def test_532 (self):
    #     input = """
    #     sqrt: function integer(n: integer)
    #     {
    #         i: integer;
    #         for (i = 0, i * i <= n, 1)
    #         {
    #             continue;
    #         }
    #         return i - 1;
    #     }
    #     main: function void()
    #     {
    #         a: integer = 28;
    #         printInteger(sqrt(a));
    #     }"""
    #     expect = "5\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))
    # def test_533 (self):
    #     input = """
    #     sqr: function float(a: float)
    #     {
    #         return a * a;
    #     }
    #     main: function void()
    #     {
    #         a: integer = 28;
    #         printFloat(sqr(a));
    #     }"""
    #     expect = "784.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))
    # def test_534 (self):
    #     input = """
    #     foo: function void(a: integer) inherit bar
    #     {
    #         super(a);
    #         b = 2 * a + 1;
    #         printInteger(b);
    #     }
    #     bar: function void(inherit out b: integer)
    #     {
    #         b = b + 1;
    #     }
    #     main: function void()
    #     {
    #         foo(27);
    #     }"""
    #     expect = "57\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))
    # def test_535(self):
    #     input = """foo: function void (a: integer, b: integer, c: integer) {
    #         printInteger(a + 2 * b + 3 * c);
    #     }
    #     main: function void() {
    #         foo(2, 3, 4);
    #     }"""
    #     expect = "20\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))
    # def test_536(self):
    #     input = """foo: function void (a: integer, b: integer) {
    #         c: integer = 2018;
    #         printInteger(a + 2 * b + 3 * c);
    #     }
    #     main: function void() {
    #         foo(2, 3);
    #     }"""
    #     expect = "6062\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))
    # def test_537(self):
    #     input = """
    #     a, b, c: boolean = true, true, false;
    #     main: function void() {
    #         a = b && c;
    #         printBoolean(a);
    #     }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))
    # def test_538(self):
    #     input = """
    #     a, b, c: boolean = true, true, false;
    #     main: function void() {
    #         printBoolean(b && c);
    #     }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))
    # def test_539(self):
    #     input = """
    #     foo: function void(x: auto)
    #     {
    #         printFloat(x);
    #     }
    #     main: function void()
    #     {
    #         foo(2e-3);
    #         foo(1);
    #     }"""
    #     expect = "0.002\n1.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 539))
    # def test_540(self):
    #     input = """
    #     foo: function void(out x: auto, out y: auto)
    #     {
    #         x = x + 1;
    #         y = y + 1;
    #         printFloat(x + y);
    #     }
    #     main: function void()
    #     {
    #         a, b: float = 1.0, 2.0;
    #         foo(a, b);
    #         printFloat(a);
    #         printFloat(b);
    #     }"""
    #     expect = "5.0\n2.0\n3.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 540))
    # def test_541(self):
    #     input = """
    #     foo: function void(out a: integer, out b: integer, c: integer)
    #     {
    #         b = b + 5;
    #         b = a + c + 4;
    #         printInteger(a);
    #         printInteger(b);
    #         printInteger(c);
    #     }
    #     main: function void()
    #     {
    #         j, k: integer = 10, 15;
    #         foo(j, j, j + k);
    #         printInteger(j);
    #         printInteger(k);
    #     }"""
    #     expect = "10\n39\n25\n39\n15\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 541))
    # def test_542 (self):
    #     input = """
    #     a: integer = foo(1, 2) + 1;
    #     foo: function integer(a: integer, b: integer)
    #     {
    #         return a + b;
    #     }
    #     main: function void()
    #     {
    #         printInteger(a);
    #     }"""
    #     expect = "4\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 542))
    # def test_543 (self):
    #     input = """
    #     a: integer = foo(1, 2) + 1;
    #     foo: function auto(a: auto, b: auto)
    #     {
    #         return a + b;
    #     }
    #     main: function void()
    #     {
    #         b: integer = foo(a, a + 1);
    #         printInteger(a);
    #         printInteger(b);
    #     }"""
    #     expect = "4\n9\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 543))
    # def test_544 (self):
    #     input = """
    #     foo: function void (inherit out a: integer)
    #     {
    #         if (a % 2 == 1)
    #         {
    #             a = 3 * a + 1;
    #         }
    #         else
    #         {
    #             a = a / 2;
    #         }
    #     }
    #     bar: function integer(out b: integer) inherit foo
    #     {
    #         super(b);
    #         return a + b;
    #     }
    #     main: function void()
    #     {
    #         b: integer = 27;
    #         printInteger(bar(b));
    #     }"""
    #     expect = "164\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 544))
    # def test_545 (self):
    #     input = """
    #     a: integer = 3;
    #     b: integer = 4;
    #     c: boolean = a * a + b * b == 25;
    #     main: function void()
    #     {
    #         printBoolean(c);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 545))
    # def test_546 (self):
    #     input = """
    #     a: integer = readInteger(); // Input 3
    #     b: integer = readInteger(); // Input 0
    #     c: boolean = (b == 0) || (a / b >= 0);
    #     main: function void()
    #     {
    #         printBoolean(c);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 546))
    # def test_547 (self):
    #     input = """
    #     a: integer = readInteger(); // Input 3
    #     b: integer = readInteger(); // Input 10
    #     c: boolean = (b < 0) && (a * b >= 0);
    #     main: function void()
    #     {
    #         printBoolean(c);
    #     }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 547))
    # def test_548 (self):
    #     input = """
    #     foo: function boolean(a: boolean, b: boolean)
    #     {
    #         return (a && b) || (a || b);
    #     }
    #     main: function void()
    #     {
    #         a, b: boolean = readBoolean(), readBoolean(); // Input false, false
    #         printBoolean(foo(a, b));
    #     }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 548))
    # def test_549 (self):
    #     input = """
    #     foo: function boolean(a: boolean, b: boolean)
    #     {
    #         return (a && b) && (a || b);
    #     }
    #     main: function void()
    #     {
    #         a, b: boolean = true, false;
    #         printBoolean(foo(a, b));
    #     }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 549))
    # def test_550 (self):
    #     input = """
    #     foo: function boolean(a: boolean, b: boolean)
    #     {
    #         return (a && (!a || b)) && ((a || !b) || b);
    #     }
    #     main: function void()
    #     {
    #         a, b: boolean = true, true;
    #         printBoolean(foo(a, b));
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 550))
    # def test_551 (self):
    #     input = """
    #     foo: function void (out a: integer, out b: integer, c: integer)
    #     {
    #         b = b + 10;
    #         a = a + c + 20;
    #         printInteger(a);
    #         printInteger(b);
    #         printInteger(c);
    #     }
    #     main: function void()
    #     {
    #         j, k: boolean = 10, 15;
    #         foo(j, j, k);
    #         printInteger(j);
    #         printInteger(k);
    #     }"""
    #     expect = "45\n20\n15\n20\n15\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 551))
    # def test_552 (self):
    #     input = """
    #     min: function integer (a: integer, b: integer)
    #     {
    #         if (a < b)
    #         {
    #             return a;
    #         }
    #         return b;
    #     }
    #     main: function void()
    #     {
    #         a, b, c, d: integer = readInteger(), readInteger(), readInteger(), readInteger(); // Input 3 -1 10 6
    #         printInteger(min(min(min(a, b), c), d));
    #     }"""
    #     expect = "-1\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 552))
    # def test_553 (self):
    #     input = """
    #     foo: function boolean(a: boolean, b: boolean)
    #     {
    #         if((a && (!a || b)) && ((a || !b) || b))
    #         {
    #             return true;
    #         }
    #         return false;
    #     }
    #     main: function void()
    #     {
    #         a, b: boolean = true, true;
    #         printBoolean(foo(a, b));
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 553))
    # def test_554 (self):
    #     input = """
    #     max: function integer(a: integer, b: integer)
    #     {
    #         if (a > b)
    #         {
    #             return a;
    #         }
    #         return b;
    #     }
    #     maxEle: function integer(arr: array [10] of integer, n: integer)
    #     {
    #         if (n == 1)
    #         {
    #             return arr[0];
    #         }
    #         k: integer = max(arr[n - 1], maxEle(arr, n - 1));
    #         return k;
    #     }
    #     main: function void()
    #     {
    #         arr: array[10] of integer = {-1, 3, 9, 6, 7, 8, 2, 0, 1, 4};
    #         n: integer = 10;
    #         printInteger(maxEle(arr, n));
    #     }"""
    #     expect = "9\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 554))
    # def test_555 (self):
    #     input = """
    #     findEle: function integer (arr: array[20] of integer, low: integer, high: integer, target: integer)
    #     {
    #         if (low <= high)
    #         {
    #             mid: integer = low + (high - low) / 2;
    #             if (arr[mid] == target)
    #             {
    #                 return mid;
    #             }
    #             if (arr[mid] < target)
    #             {
    #                 return findEle(arr, mid + 1, high, target);
    #             }
    #             return findEle(arr, 0, mid - 1, target);
    #         }
    #         return -1;
    #     }
    #     main: function void()
    #     {
    #         arr: array[20] of integer = {-26, -15, -8, -3, 0, 4, 10, 21, 30, 45, 49, 51, 59, 67, 70, 71, 78, 89, 94, 100};
    #         printInteger(findEle(arr, 0, 19, 94));
    #     }"""
    #     expect = "18\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 555))
    # def test_556 (self):
    #     input = """
    #     swapNumber: function void(out a: integer, out b: integer)
    #     {
    #         temp: integer = a;
    #         a = b;
    #         b = temp;
    #     }
    #     sort: function void (arr: array[20] of integer, low: integer, high: integer)
    #     {
    #         if (low < high)
    #         {
    #             idx: integer = partition(arr, low, high);
    #             sort(arr, low, idx - 1);
    #             sort(arr, idx + 1, high);
    #         }
    #     }
    #     partition: function integer(arr: array[20] of integer, low: integer, high: integer)
    #     {
    #         pivot, left, right: integer = arr[high], low, high - 1;
    #         while (true)
    #         {
    #             while ((left <= right) && (arr[left] < pivot))
    #             {
    #                 left = left + 1;
    #             }
    #             while ((right >= left) && (arr[right] > pivot))
    #             {
    #                 right = right - 1;
    #             }
    #             if (left >= right)
    #             {
    #                 break;
    #             }
    #             swapNumber(arr[left], arr[right]);
    #             left = left + 1;
    #             right = right - 1;
    #         }
    #         swapNumber(arr[left], arr[high]);
    #         return left;
    #     }
    #     main: function void()
    #     {
    #         arr: array[20] of integer = {-26, 15, 8, -3, 0, 4, -10, 21, 30, 10, 49, -51, 59, 67, -70, 71, 33, -89, 27, 100};
    #         sort(arr, 0, 19);
    #         i: integer;
    #         for (i = 0, i < 20, 1)
    #         {
    #             printInteger(arr[i]);
    #         }
    #     }"""
    #     expect = "-89\n-70\n-51\n-26\n-10\n-3\n0\n4\n8\n10\n15\n21\n27\n30\n33\n49\n59\n67\n71\n100\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 556))
    # def test_557 (self):
    #     input = """
    #     main: function void()
    #     {
    #         arr: array[5] of integer = {-3, 9, 0, 1, 8};
    #         i: integer;
    #         for (i = 0, i <= 2, 1)
    #         {
    #             temp: integer = arr[i];
    #             arr[i] = arr[4 - i];
    #             arr[4 - i] = temp;
    #         }
    #         for(i = 0, i < 5, 1)
    #         {
    #             printInteger(arr[i]);
    #         }
    #     }"""
    #     expect = "8\n1\n0\n9\n-3\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 557))
    # def test_558 (self):
    #     input = """
    #     swapNum: function void(out a: integer, out b: integer)
    #     {
    #         temp: integer = a;
    #         a = b;
    #         b = temp;
    #     }
    #     main: function void()
    #     {
    #         printString(\"Before swapping:\");
    #         a, b: integer = 4, 7;
    #         printInteger(a);
    #         printInteger(b);
    #         swapNum(a, b);
    #         printString(\"After swapping:\");
    #         printInteger(a);
    #         printInteger(b);
    #     }"""
    #     expect = "Before swapping:\n4\n7\nAfter swapping:\n7\n4\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 558))
    # def test_559 (self):
    #     input = """x: integer = 65;
    #     fact: function integer (n: integer) {
    #         if (n == 0) return 1;
    #         else return n * fact(n - 1);
    #     }
    #     inc: function void(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = fact(3);
    #         inc(x, delta);
    #         printInteger(x);
    #     }"""
    #     expect = "71\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 559))
    # def test_560 (self):
    #     input = """
    #     swap: function void(a: integer, b: integer)
    #     {
    #         temp: integer = a;
    #         a = b;
    #         b = temp;
    #     }
    #     main: function void() {
    #         a, b: integer = 4, 7;
    #         swap(a, b);
    #         printInteger(a);
    #         printInteger(b);
    #     }"""
    #     expect = "4\n7\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 560))
    # def test_561 (self):
    #     input = """
    #     foo: function float (a: integer, b: integer)
    #     {
    #         if (b == 0)
    #         {
    #             return 0;
    #         }
    #         return (a * 1.0) / b;
    #     }
    #     main: function void() {
    #         a, b: integer = 4, 7;
    #         printFloat(foo(a, b));
    #     }"""
    #     expect = "0.5714286\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 561))
    # def test_562 (self):
    #     input = """
    #     a: auto = foo(1, 2) + 1;
    #     foo: function auto (a: auto, b: auto)
    #     {
    #         return a + b;
    #     }
    #     main: function void() {
    #         printInteger(a);
    #     }"""
    #     expect = "4\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 562))
    # def test_563 (self):
    #     input = """
    #     a, b, c: integer = 3, 4, 5;
    #     x: auto = a * a + b * b == c * c;
    #     main: function void() {
    #         printBoolean(x);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 563))
    # def test_564 (self):
    #     input = """
    #     a: array [10] of integer = {3, 9, 1, 0, 6, 4, 5, 8, 7, 2};
    #     max: function integer(a: integer, b: integer)
    #     {
    #         if (a > b)
    #         {
    #             return a;
    #         }
    #         return b;
    #     }
    #     maxEle: function integer(arr: array [10] of integer, n: integer)
    #     {
    #         if (n == 1)
    #         {
    #             return arr[0];
    #         }
    #         k: integer = max(arr[n - 1], maxEle(arr, n - 1));
    #         return k;
    #     }
    #     main: function void() {
    #         printInteger(maxEle(a, 10));
    #     }"""
    #     expect = "9\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 564))
    # def test_565 (self):
    #     input = """
    #     a: array [10] of integer = {3, 9, 1, 0, 6, 4, 5, 8, 7, 2};
    #     main: function void() {
    #         i: integer;
    #         for(i = 0, i < 5, 1)
    #         {
    #             temp: integer = a[i];
    #             a[i] = a[9 - i];
    #             a[9 - i] = temp;
    #         }
    #         for(i = 0, i < 10, 1)
    #         {
    #             printInteger(a[i]);
    #         }
    #     }"""
    #     expect = "2\n7\n8\n5\n4\n6\n0\n1\n9\n3\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 565))
    # def test_566 (self):
    #     input = """
    #     a, b, c: string = "Hello", "World", (a :: " ") :: (b :: "!");
    #     main: function void() {
    #         printString(c);
    #     }"""
    #     expect = "Hello World!\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 566))
    # def test_567 (self):
    #     input = """
    #     main: function void() {
    #         printString("Hello " :: "World!");
    #     }"""
    #     expect = "Hello World!\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 567))
    # def test_568 (self):
    #     input = """
    #     main: function void() {
    #         c: integer = 1 + 2;
    #         d: float = 1.5 + 2;
    #         e: float = 3.7 + 9.1;
    #         printInteger(c);
    #         printFloat(d);
    #         printFloat(e);
    #     }"""
    #     expect = "3\n3.5\n12.8\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 568))
    # def test_569 (self):
    #     input = """
    #     powMod: function integer (a: integer, b: integer, m: integer)
    #     {
    #         if (b == 0)
    #         {
    #             return 1;
    #         }
    #         p: integer = ((powMod(a, b / 2, m) % m) * (powMod(a, b / 2, m) % m)) % m;
    #         if (b % 2 == 0)
    #         {
    #             return p;
    #         }
    #         return (p * (a % m)) % m;
    #     }
    #     main: function void() {
    #         x, y, m: integer = 3, 29, 1337;
    #         printInteger(powMod(x, y, m));
    #     }"""
    #     expect = "978\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 569))
    # def test_570 (self):
    #     input = """
    #     factorial: function integer(n: integer, m: integer)
    #     {
    #         res, i: integer = 1, 1;
    #         for(i = 1, i <= n, 1)
    #         {
    #             res = ((res % m) * (i % m)) % m;
    #         }
    #         return res;
    #     }
    #     main: function void() {
    #         n, m: integer = 100, 1337;
    #         printInteger(factorial(n, m));
    #     }"""
    #     expect = "1015\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 570))
    # def test_571 (self):
    #     input = """
    #     sumDigit: function integer(n: integer)
    #     {
    #         sum: integer = 0;
    #         while(n > 0)
    #         {
    #             sum = sum + (n % 10);
    #             n = n / 10;
    #         }
    #         return sum;
    #     }
    #     primes: function boolean(n: integer)
    #     {
    #         i: integer;
    #         for(i = 2, i * i <= n, 1)
    #         {
    #             if (n % i == 0)
    #             {
    #                 return false;
    #             }
    #         }
    #         return n > 1;
    #     }
    #     main: function void() {
    #         n: integer = readInteger(); // Input 28
    #         i: integer;
    #         flag: boolean = false;
    #         for (i = n, i >= 10, -1)
    #         {
    #             if (primes(i) && primes(sumDigit(i)))
    #             {
    #                 printInteger(i);
    #                 flag = true;
    #                 break;
    #             }
    #         }
    #         if (!flag)
    #         {
    #             printInteger(0);
    #         }
    #     }"""
    #     expect = "23\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 571))
    # def test_572 (self):
    #     input = """
    #     reverse: function integer (n: integer)
    #     {
    #         result, temp: integer = 0, n;
    #         if (temp < 0)
    #         {
    #             n = -n;
    #         }
    #         while (n > 0)
    #         {
    #             result = 10 * result + (n % 10);
    #             n = n / 10;
    #         }
    #         if (temp < 0)
    #         {
    #             return -result;
    #         }
    #         return result;
    #     }
    #     main: function void() {
    #         n: integer = readInteger(); // Input -28
    #         printInteger(reverse(n));
    #     }"""
    #     expect = "-82\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 572))
    # def test_573 (self):
    #     input = """
    #     main: function void() {
    #         a: integer = 8;
    #         b: array [3] of integer = {1, 2, 3};
    #         b[2] = a;
    #         printInteger(b[2]);
    #     }"""
    #     expect = "8\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 573))
    # def test_574 (self):
    #     input = """
    #     main: function void() {
    #         printInteger(foo(3, 9));
    #     }
    #     foo: function integer(a: integer, b: integer)
    #     {
    #         if (a < b)
    #         {
    #             return b;
    #         }
    #         return a;
    #     }"""
    #     expect = "9\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 574))
    # def test_575 (self):
    #     input = """
    #     main: function void() {
    #         a, b: integer = 3, 4;
    #         swap(a, b);
    #         printInteger(a);
    #         printInteger(b);
    #     }
    #     swap: function void(out a: integer, out b: integer)
    #     {
    #         temp: integer = a;
    #         a = b;
    #         b = temp;
    #     }"""
    #     expect = "4\n3\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 575))
    # def test_576 (self):
    #     input = """
    #     bar: function void (a: integer, out b: integer, c: integer)
    #     {
    #         a = a + 10;
    #         b = a + c + 4;
    #         printInteger(a);
    #         printInteger(b);
    #         printInteger(c);
    #     }
    #     main: function void() {
    #         j, k: integer = 10, 15;
    #         bar(j, j, j + k);
    #         printInteger(j);
    #         printInteger(k);
    #     }"""
    #     expect = "20\n49\n25\n49\n15\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 576))
    # def test_577 (self):
    #     input = """
    #     concat: function string (a: string, b: string)
    #     {
    #         return a :: b;
    #     }
    #     main: function void() {
    #         a, b: string = "Hello ", "World!";
    #         printString(concat(a, b));
    #     }"""
    #     expect = "Hello World!\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 577))
    # def test_578 (self):
    #     input = """
    #     accumulate: function integer (arr: array [10] of integer, low: integer, high: integer, init: integer)
    #     {
    #         if ((low > high) || (low < 0) || (low > 9) || (high <= 0) || (high > 10))
    #         {
    #             return init;
    #         }
    #         i: integer;
    #         for(i = low, i < high, 1)
    #         {
    #             init = init + arr[i];
    #         }
    #         return init;
    #     }
    #     main: function void() {
    #         arr: array [10] of integer = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    #         printInteger(accumulate(arr, 0, 10, 55));
    #     }"""
    #     expect = "110\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 578))
    # def test_579 (self):
    #     input = """
    #     removeMin: function void(arr: array [10] of integer, out n: integer)
    #     {
    #         i: integer;
    #         min: integer = arr[0];
    #         for(i = 1, i < n, 1)
    #         {
    #             if (min > arr[i])
    #             {
    #                 min = arr[i];
    #             }
    #         }
    #         for(i = 0, i < n, 1)
    #         {
    #             if (arr[i] == min)
    #             {
    #                 n = n - 1;
    #                 j: integer;
    #                 for (j = i, j < n, 1)
    #                 {
    #                     arr[j] = arr[j + 1];
    #                 }
    #                 i = i - 1;
    #             }
    #         }
    #     }
    #     main: function void() {
    #         arr: array [10] of integer = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1};
    #         n: integer = 10;
    #         removeMin(arr, n);
    #         i: integer;
    #         for(i = 0, i < n, 1)
    #         {
    #             printInteger(arr[i]);
    #         }
    #     }"""
    #     expect = "2\n3\n4\n5\n6\n7\n8\n9\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 579))
    # def test_580 (self):
    #     input = """
    #     main: function void() {
    #         printString("Hello World!");
    #     }"""
    #     expect = "Hello World!\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 580))
    # def test_581 (self):
    #     input = """
    #     foo: function void(inherit a: integer, b: integer)
    #     {
    #         return;
    #     }
    #     bar: function void(c: integer) inherit foo
    #     {
    #         super(2, 1);
    #         printInteger(a);
    #     }
    #     main: function void() {
    #         bar(2);
    #     }"""
    #     expect = "2\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 581))
    def test_582 (self):
        input = """
        main: function void() {
            i: integer = 0;
            while(true)
            {
                if (i == 20)
                {
                    break;
                }
                i = i + 1;
            }
            printInteger(i);
        }"""
        expect = "20\n"
        self.assertTrue(TestCodeGen.test(input, expect, 582))
    # def test_583 (self):
    #     input = """
    #     main: function void() {
    #         i: integer;
    #         for(i = 0, i < 10, i + 1)
    #         {
    #             printInteger(i);
    #         }
    #     }"""
    #     expect = "0\n1\n3\n7\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 583))
    # def test_584 (self):
    #     input = """
    #     isAmstrong: function boolean (n: integer)
    #     {
    #         sum, temp: integer = 0, n;
    #         while (temp > 0)
    #         {
    #             digit: integer = temp % 10;
    #             sum = sum + digit * digit * digit;
    #             temp = temp / 10;
    #         }
    #         return sum == n;
    #     }
    #     main: function void() {
    #         a: integer = 153;
    #         printBoolean(isAmstrong(a));
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 584))
    # def test_585 (self):
    #     input = """
    #     foo: function void (out a: integer)
    #     {
    #         if (a % 2 == 0)
    #         {
    #             a = a / 2;
    #         }
    #         else
    #         {
    #             a = 3 * a + 1;
    #         }
    #     }
    #     main: function void() {
    #         a: integer = 153;
    #         foo(a);
    #         printInteger(a);
    #     }"""
    #     expect = "460\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 585))
    # def test_586 (self):
    #     input = """
    #     fibo: function integer(n: integer)
    #     {
    #         if (n <= 1)
    #         {
    #             return n;
    #         }
    #         return fibo(n - 1) + fibo(n - 2);
    #     }
    #     main: function void() {
    #         a: integer = 46;
    #         printInteger(fibo(a));
    #     }"""
    #     expect = "1836311903\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 586))
    # def test_587 (self):
    #     input = """
    #     main: function void() {
    #         a, b, c: integer = 3, 4, 5;
    #         d: boolean = (a < 0) || (a * a + b * b == c * c) || (b < 0) || (c < 0);
    #         printBoolean(d);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 587))
    # def test_588 (self):
    #     input = """
    #     main: function void() {
    #         a, b, c: integer = 3, 4, 5;
    #         d: boolean = a + b >= c;
    #         printBoolean(d);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 588))
    # def test_589 (self):
    #     input = """
    #     main: function void() {
    #         a, b, c: integer = 3, 4, 5;
    #         d: boolean = !((a == b) || (b == c) || (c == a));
    #         printBoolean(d);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 589))
    # def test_590 (self):
    #     input = """
    #     abs: function float (a: float)
    #     {
    #         if (a < 0)
    #         {
    #             return -a;
    #         }
    #         return a;
    #     }
    #     foo: function boolean(a: float, b: float)
    #     {
    #         return abs(a) + abs(b) >= abs(a + b);
    #     }
    #     main: function void() {
    #         printBoolean(foo(2.1, -1.9));
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 590))
    # def test_591 (self):
    #     input = """
    #     foo: function auto (a: integer, b: integer)
    #     {
    #         return a + b + 1.5;
    #     }
    #     main: function void() {
    #         x: float = foo(1, 2) + 0.5;
    #         printFloat(x);
    #     }"""
    #     expect = "5.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 591))
    # def test_592 (self):
    #     input = """
    #     x: integer = 65;
    #     inc: function void(out n: integer, delta: integer, dec: boolean)
    #     {
    #         if (dec == true)
    #         {
    #             n = n - delta;
    #         }
    #         else
    #         {
    #             n = n + delta;
    #         }
    #     }
    #     main: function void() {
    #         inc(x, 3, false);
    #         printFloat(x);
    #     }"""
    #     expect = "68.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 592))
    # def test_593 (self):
    #     input = """
    #     x: integer = 65;
    #     foo: function float (a: integer, b: integer)
    #     {
    #         if (b == 0)
    #         {
    #             return 0.0;
    #         }
    #         return (a * 1.0) / b;
    #     }
    #     main: function void() {
    #         a: float = foo(x - 4, 5);
    #         printFloat(a);
    #     }"""
    #     expect = "12.2\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 593))
    # def test_594 (self):
    #     input = """
    #     x, y: integer = 65, 97;
    #     main: function void() {
    #         a: float = x + y;
    #         printFloat(a);
    #     }"""
    #     expect = "162.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 594))
    # def test_595 (self):
    #     input = """
    #     x, y, z: integer = 65, 97, x + y;
    #     main: function void() {
    #         a: float = z + 2e3;
    #         printFloat(a);
    #     }"""
    #     expect = "2162.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 595))
    # def test_596 (self):
    #     input = """
    #     foo: function void(x: integer, y: integer, z: float)
    #     {
    #         a: integer = x % y;
    #         printFloat(a + z);
    #     }
    #     main: function void() {
    #         foo(20, 5, 0.99);
    #     }"""
    #     expect = "0.99\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 596))
    # def test_597 (self):
    #     input = """
    #     main: function void() {
    #         a: array [1, 2] of integer = {{1, 2}};
    #         a[0, 0] = 3;
    #         a[0, 1] = a[0, 0] + a[0, 1];
    #         printInteger(a[0, 1]);
    #     }"""
    #     expect = "5\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 597))
    # def test_598 (self):
    #     input = """
    #     main: function void() {
    #         a: array [10] of integer;
    #         i: integer;
    #         for(i = 0, i < 10, 1)
    #         {
    #             printInteger(a[i]);
    #         }
    #     }"""
    #     expect = "0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 598))
    # def test_599 (self):
    #     input = """
    #     main: function void() {
    #         a: array [2, 3] of boolean;
    #         i, j: integer;
    #         for(i = 0, i < 2, 1)
    #         {
    #             for(j = 0, j < 3, 1)
    #             {
    #                 printBoolean(a[i, j]);
    #             }
    #         }
    #     }"""
    #     expect = "false\nfalse\nfalse\nfalse\nfalse\nfalse\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 599))
