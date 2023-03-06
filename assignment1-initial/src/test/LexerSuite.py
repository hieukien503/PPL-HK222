import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_100(self):
        self.assertTrue(TestLexer.test("a_bcd_ef", "a_bcd_ef,<EOF>", 100))
    def test_101(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    def test_102(self):
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 102))
    def test_103(self):
        self.assertTrue(TestLexer.test(""" "abc\t" """, "abc\t,<EOF>", 103))
    def test_104(self):
        input = """ "He asked me: \\"Where is John?\\"" """
        expect = """He asked me: \\"Where is John?\\",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 104))
    def test_105(self):
        self.assertTrue(TestLexer.test("""\"abc\n\"""", "Unclosed String: abc\n", 105))
    def test_106(self):
        self.assertTrue(TestLexer.test("1_234.567E-10", "1234.567E-10,<EOF>", 106))
    def test_107(self):
        self.assertTrue(TestLexer.test(""" \"Hello""", "Unclosed String: Hello", 107))
    def test_108(self):
        self.assertTrue(TestLexer.test("@198016abc", "Error Token @", 108))
    def test_109(self):
        self.assertTrue(TestLexer.test("astgen", "astgen,<EOF>", 109))
    def test_110(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab:\t" """, "This is a string containing tab:\t,<EOF>", 110))
    def test_111(self):
        self.assertTrue(TestLexer.test(".25e+3", ".25e+3,<EOF>", 111))
    def test_112(self):
        self.assertTrue(TestLexer.test("0.25", "0.25,<EOF>", 112))
    def test_113(self):
        self.assertTrue(TestLexer.test("1_23", "123,<EOF>", 113))
    def test_114(self):
        self.assertTrue(TestLexer.test("_this_is_id", "_this_is_id,<EOF>", 114))
    def test_115(self):
        self.assertTrue(TestLexer.test(""" "Hello!" """, "Hello!,<EOF>", 115))
    def test_116(self):
        self.assertTrue(TestLexer.test("197_236.015e7", "197236.015e7,<EOF>", 116))
    def test_117(self):
        self.assertTrue(TestLexer.test("abc_198_ef", "abc_198_ef,<EOF>", 117))
    def test_118(self):
        self.assertTrue(TestLexer.test("?abc1982", "Error Token ?", 118))
    def test_119(self):
        self.assertTrue(TestLexer.test(""" a: string = \"Hello;""", "a,:,string,=,Unclosed String: Hello;", 119))
    def test_120(self):
        self.assertTrue(TestLexer.test("main: function void() {}", "main,:,function,void,(,),{,},<EOF>", 120))
    def test_121(self):
        self.assertTrue(TestLexer.test("a, b, c: integer = 10, 4;", "a,,,b,,,c,:,integer,=,10,,,4,;,<EOF>", 121))
    def test_122(self):
        self.assertTrue(TestLexer.test("a: float = .25e+20;", "a,:,float,=,.25e+20,;,<EOF>", 122))
    def test_123(self):
        self.assertTrue(TestLexer.test("_ptr", "_ptr,<EOF>", 123))
    def test_124(self):
        self.assertTrue(TestLexer.test(""" \"Hello, this is me\n\" """, "Unclosed String: Hello, this is me\n", 124))
    def test_125(self):
        self.assertTrue(TestLexer.test("a: boolean = true;", "a,:,boolean,=,true,;,<EOF>", 125))
    def test_126(self):
        self.assertTrue(TestLexer.test("a, b: integer = 69, 10 * 9;", "a,,,b,:,integer,=,69,,,10,*,9,;,<EOF>", 126))
    def test_127(self):
        self.assertTrue(TestLexer.test("foo: function void() inherit fact { return; }", "foo,:,function,void,(,),inherit,fact,{,return,;,},<EOF>", 127))
    def test_128(self):
        self.assertTrue(TestLexer.test("1_000_234", "1000234,<EOF>", 128))
    def test_129(self):
        self.assertTrue(TestLexer.test("1_23", "123,<EOF>", 129))
    def test_130(self):
        self.assertTrue(TestLexer.test("myFunc", "myFunc,<EOF>", 130))
    def test_131(self):
        self.assertTrue(TestLexer.test("abc^1970", "abc,Error Token ^", 131))
    def test_132(self):
        self.assertTrue(TestLexer.test(""" \"Hello\n, this is me\" """, "Unclosed String: Hello\n", 132))
    def test_133(self):
        self.assertTrue(TestLexer.test("a: integer = foo(1, 2);", "a,:,integer,=,foo,(,1,,,2,),;,<EOF>", 133))
    def test_134(self):
        self.assertTrue(TestLexer.test(""" \"PPL\'\" """, "PPL\',<EOF>", 134))
    def test_135(self):
        self.assertTrue(TestLexer.test("a: float = 1_23e96;", "a,:,float,=,123e96,;,<EOF>", 135))
    def test_136(self):
        self.assertTrue(TestLexer.test("abc_198@", "abc_198,Error Token @", 136))
    def test_137(self):
        self.assertTrue(TestLexer.test("x: integer = 1;", "x,:,integer,=,1,;,<EOF>", 137))
    def test_138(self):
        self.assertTrue(TestLexer.test("a: array [2, 3] of integer;", "a,:,array,[,2,,,3,],of,integer,;,<EOF>", 138))
    def test_139(self):
        self.assertTrue(TestLexer.test(""" \"abcd\b\" """, "abcd\b,<EOF>", 139))
    def test_140(self):
        self.assertTrue(TestLexer.test("123.E+7", "123.E+7,<EOF>", 140))
    def test_141(self):
        self.assertTrue(TestLexer.test("a$2896", "a,Error Token $", 141))
    def test_142(self):
        self.assertTrue(TestLexer.test("_PPLonFire", "_PPLonFire,<EOF>", 142))
    def test_143(self):
        input = """fact: function float(out a: integer, delta: float) {}"""
        expect = "fact,:,function,float,(,out,a,:,integer,,,delta,:,float,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))
    def test_144(self):
        input = """ \"He said: \\"What time is it?\\" """
        expect = """Unclosed String: He said: \\"What time is it?\\" """
        self.assertTrue(TestLexer.test(input, expect, 144))
    def test_145(self):
        self.assertTrue(TestLexer.test(""" \"abc\ndef\" """, "Unclosed String: abc\n", 145))
    def test_146(self):
        self.assertTrue(TestLexer.test("abc?0983", "abc,Error Token ?", 146))
    def test_147(self):
        self.assertTrue(TestLexer.test("1_2", "12,<EOF>", 147))
    def test_148(self):
        self.assertTrue(TestLexer.test("3_27.03E-10", "327.03E-10,<EOF>", 148))
    def test_149(self):
        self.assertTrue(TestLexer.test("x: boolean = true;", "x,:,boolean,=,true,;,<EOF>", 149))
    def test_150(self):
        input = "a: array[2] of string;"
        expect = "a,:,array,[,2,],of,string,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))
    def test_151(self):
        self.assertTrue(TestLexer.test("0.21983e1", "0.21983e1,<EOF>", 151))
    def test_152(self):
        self.assertTrue(TestLexer.test("1e8", "1e8,<EOF>", 152))
    def test_153(self):
        self.assertTrue(TestLexer.test("""\"This is John""", "Unclosed String: This is John", 153))
    def test_154(self):
        self.assertTrue(TestLexer.test("""\"He is my brother\t\"""", "He is my brother\t,<EOF>", 154))
    def test_155(self):
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
        expect = """main,:,function,void,(,),{,a,:,integer,=,1,;,do,{,if,(,a,>,10,),{,break,;,},a,=,a,+,1,;,},while,(,true,),;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 155))
    def test_156(self):
        self.assertTrue(TestLexer.test("a: integer = 1_23.456;", "a,:,integer,=,123.456,;,<EOF>", 156))
    def test_157(self):
        input = """x, y: string = \"Peter\", \"John\n\";"""
        expect = """x,,,y,:,string,=,Peter,,,Unclosed String: John\n"""
        self.assertTrue(TestLexer.test(input, expect, 157))
    def test_158(self):
        self.assertTrue(TestLexer.test("_ptr", "_ptr,<EOF>", 158))
    def test_159(self):
        self.assertTrue(TestLexer.test("_192atf", "_192atf,<EOF>", 159))
    def test_160(self):
        self.assertTrue(TestLexer.test("a_int: integer = 0;", "a_int,:,integer,=,0,;,<EOF>", 160))
    def test_161(self):
        self.assertTrue(TestLexer.test("x: array [3] of boolean;", "x,:,array,[,3,],of,boolean,;,<EOF>", 161))
    def test_162(self):
        self.assertTrue(TestLexer.test("var_a: float;", "var_a,:,float,;,<EOF>", 162))
    def test_163(self):
        self.assertTrue(TestLexer.test("""a: string = \"abcdef\";""", "a,:,string,=,abcdef,;,<EOF>", 163))
    def test_164(self):
        self.assertTrue(TestLexer.test("a: integer = 8 - 2;","a,:,integer,=,8,-,2,;,<EOF>", 164))
    def test_165(self):
        self.assertTrue(TestLexer.test("""main: function void() {
            a@198: integer = 20;
        }""", "main,:,function,void,(,),{,a,Error Token @", 165))
    def test_166(self):
        self.assertTrue(TestLexer.test("-123_456_789", "-,123456789,<EOF>", 166))
    def test_167(self):
        self.assertTrue(TestLexer.test("_a&198_bcd", "_a,Error Token &", 167))
    def test_168(self):
        self.assertTrue(TestLexer.test("//This is a comment", "<EOF>", 168))
    def test_169(self):
        self.assertTrue(TestLexer.test("""\"abc198@$#\"""", "abc198@$#,<EOF>", 169))
    def test_170(self):
        input = """a, b: integer = 19, 20 * 10, 30;"""
        expect = "a,,,b,:,integer,=,19,,,20,*,10,,,30,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))
    def test_171(self):
        self.assertTrue(TestLexer.test("a@207: integer;", "a,Error Token @", 171))
    def test_172(self):
        self.assertTrue(TestLexer.test("0123456789", "0,123456789,<EOF>", 172))
    def test_173(self):
        self.assertTrue(TestLexer.test("auto: integer = 39", "auto,:,integer,=,39,<EOF>", 173))
    def test_174(self):
        self.assertTrue(TestLexer.test("""a: string = \"123@#$456\";""", "a,:,string,=,123@#$456,;,<EOF>", 174))
    def test_175(self):
        self.assertTrue(TestLexer.test("10_023", "10023,<EOF>", 175))
    def test_176(self):
        input = """abc: function auto(a: integer, b: float) {
            c: auto = 2 * a + b;
            printInteger(c);
        }
        main: function void(a: float) {
            abc(1, 2.0);
        }"""
        expect = "abc,:,function,auto,(,a,:,integer,,,b,:,float,),{,c,:,auto,=,2,*,a,+,b,;,printInteger,(,c,),;,},main,:,function,void,(,a,:,float,),{,abc,(,1,,,2.0,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))
    def test_177(self):
        self.assertTrue(TestLexer.test("""\"abc\\"abc\\"\"""", """abc\\"abc\\",<EOF>""", 177))
    def test_178(self):
        self.assertTrue(TestLexer.test("a: string = \"PPL\n\";", "a,:,string,=,Unclosed String: PPL\n", 178))
    def test_179(self):
        self.assertTrue(TestLexer.test("1_234_56_7", "1234567,<EOF>", 179))
    def test_180(self):
        self.assertTrue(TestLexer.test("a: boolean = true;", "a,:,boolean,=,true,;,<EOF>", 180))
    def test_181(self):
        self.assertTrue(TestLexer.test("""\"abc\\v\"""", "Illegal Escape In String: abc\\v", 181))
    def test_182(self):
        self.assertTrue(TestLexer.test("foo: function array[3] of string(a: array [3] of string) {}", "foo,:,function,array,[,3,],of,string,(,a,:,array,[,3,],of,string,),{,},<EOF>", 182))
    def test_183(self):
        self.assertTrue(TestLexer.test("201.E3", "201.E3,<EOF>", 183))
    def test_184(self):
        self.assertTrue(TestLexer.test("a: array [2_0, 3 + 20, 1_92 / 16] of boolean;", "a,:,array,[,20,,,3,+,20,,,192,/,16,],of,boolean,;,<EOF>", 184))
    def test_185(self):
        self.assertTrue(TestLexer.test("abc@901", "abc,Error Token @", 185))
    def test_186(self):
        self.assertTrue(TestLexer.test("main: function bool() { return true; }", "main,:,function,bool,(,),{,return,true,;,},<EOF>", 186))
    def test_187(self):
        self.assertTrue(TestLexer.test("a, b, c: integer = 1, 2;", "a,,,b,,,c,:,integer,=,1,,,2,;,<EOF>", 187))
    def test_188(self):
        self.assertTrue(TestLexer.test("x, y: string = \"a\", \"b\", \"c\";", "x,,,y,:,string,=,a,,,b,,,c,;,<EOF>", 188))
    def test_189(self):
        input = """foo: function void() {}
                   fact: function integer() inherit foo { return 0; }"""
        self.assertTrue(TestLexer.test(input, "foo,:,function,void,(,),{,},fact,:,function,integer,(,),inherit,foo,{,return,0,;,},<EOF>", 189))
    def test_190(self):
        self.assertTrue(TestLexer.test("1_234_56_7.214857e-10", "1234567.214857e-10,<EOF>", 190))
    def test_191(self):
        self.assertTrue(TestLexer.test("""\"Hello \\"World\\"\"""", """Hello \\"World\\",<EOF>""", 191))
    def test_192(self):
        self.assertTrue(TestLexer.test("""\"abc_efg\\v!#$\"""", """Illegal Escape In String: abc_efg\\v""", 192))
    def test_193(self):
        self.assertTrue(TestLexer.test("a: string = \"\";", "a,:,string,=,,;,<EOF>", 193))
    def test_194(self):
        self.assertTrue(TestLexer.test("""\"This is an unclosed string""", "Unclosed String: This is an unclosed string", 194))
    def test_195(self):
        self.assertTrue(TestLexer.test("id1: integer = id2;", "id1,:,integer,=,id2,;,<EOF>", 195))
    def test_196(self):
        input = """uwxyz: string = \"Test Identifier: \\"Success\\"\";"""
        expect = """uwxyz,:,string,=,Test Identifier: \\"Success\\",;,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 196))
    def test_197(self):
        self.assertTrue(TestLexer.test("err: function void(inherit out a: integer, b: array [2] of float) inherit err1 {}", "err,:,function,void,(,inherit,out,a,:,integer,,,b,:,array,[,2,],of,float,),inherit,err1,{,},<EOF>", 197))
    def test_198(self):
        self.assertTrue(TestLexer.test("a: integer = 2_147_483_647", "a,:,integer,=,2147483647,<EOF>", 198))
    def test_199(self):
        self.assertTrue(TestLexer.test("""\"Hello\\0\"""", "Illegal Escape In String: Hello\\0", 199))