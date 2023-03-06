# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0251\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\5\r\u010f")
        buf.write("\n\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u0119")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\7>\u01d1\n>\f>\16>\u01d4\13>\3?\3")
        buf.write("?\5?\u01d8\n?\3?\3?\3@\5@\u01dd\n@\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3@\3@\5@\u01e8\n@\3@\3@\3A\3A\7A\u01ee\nA\fA\16A\u01f1")
        buf.write("\13A\3A\3A\3A\3B\3B\7B\u01f8\nB\fB\16B\u01fb\13B\3B\3")
        buf.write("B\6B\u01ff\nB\rB\16B\u0200\7B\u0203\nB\fB\16B\u0206\13")
        buf.write("B\3C\3C\7C\u020a\nC\fC\16C\u020d\13C\3D\3D\5D\u0211\n")
        buf.write("D\3D\6D\u0214\nD\rD\16D\u0215\3E\3E\3E\3E\7E\u021c\nE")
        buf.write("\fE\16E\u021f\13E\3E\3E\3F\3F\3F\7F\u0226\nF\fF\16F\u0229")
        buf.write("\13F\3F\3F\3F\3F\3F\3G\6G\u0231\nG\rG\16G\u0232\3G\3G")
        buf.write("\3H\3H\3H\3I\3I\7I\u023c\nI\fI\16I\u023f\13I\3I\3I\3I")
        buf.write("\3J\3J\7J\u0246\nJ\fJ\16J\u0249\13J\3J\3J\3J\5J\u024e")
        buf.write("\nJ\3J\3J\3\u0227\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\2\33\2\35\2\37\16!\17#\20%\21\'")
        buf.write("\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35")
        buf.write("?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62")
        buf.write("i\63k\64m\65o\66q\67s8u9w:y;{<}=\177>\u0081?\u0083\2\u0085")
        buf.write("\2\u0087\2\u0089@\u008bA\u008dB\u008fC\u0091D\u0093E\3")
        buf.write("\2\17\3\3\f\f\7\2\n\f\16\17$$))^^\5\2\n\13\16\17))\t\2")
        buf.write("))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\4\2\f\f\16\17\5\2\13\f\17\17\"\"\3\2")
        buf.write("^^\2\u025f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2")
        buf.write("\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\3\u0095\3\2\2\2\5\u009a\3\2\2\2\7\u00a6\3\2\2")
        buf.write("\2\t\u00b3\3\2\2\2\13\u00bd\3\2\2\2\r\u00c8\3\2\2\2\17")
        buf.write("\u00d4\3\2\2\2\21\u00e1\3\2\2\2\23\u00ec\3\2\2\2\25\u00f8")
        buf.write("\3\2\2\2\27\u00fe\3\2\2\2\31\u010e\3\2\2\2\33\u0110\3")
        buf.write("\2\2\2\35\u0118\3\2\2\2\37\u011a\3\2\2\2!\u011f\3\2\2")
        buf.write("\2#\u0125\3\2\2\2%\u012d\3\2\2\2\'\u0130\3\2\2\2)\u0135")
        buf.write("\3\2\2\2+\u013b\3\2\2\2-\u0141\3\2\2\2/\u0145\3\2\2\2")
        buf.write("\61\u014e\3\2\2\2\63\u0151\3\2\2\2\65\u0159\3\2\2\2\67")
        buf.write("\u0160\3\2\2\29\u0167\3\2\2\2;\u016c\3\2\2\2=\u0171\3")
        buf.write("\2\2\2?\u0177\3\2\2\2A\u017b\3\2\2\2C\u0184\3\2\2\2E\u0187")
        buf.write("\3\2\2\2G\u018f\3\2\2\2I\u0195\3\2\2\2K\u0197\3\2\2\2")
        buf.write("M\u0199\3\2\2\2O\u019b\3\2\2\2Q\u019d\3\2\2\2S\u019f\3")
        buf.write("\2\2\2U\u01a2\3\2\2\2W\u01a5\3\2\2\2Y\u01a8\3\2\2\2[\u01ab")
        buf.write("\3\2\2\2]\u01ad\3\2\2\2_\u01af\3\2\2\2a\u01b2\3\2\2\2")
        buf.write("c\u01b5\3\2\2\2e\u01b8\3\2\2\2g\u01ba\3\2\2\2i\u01bc\3")
        buf.write("\2\2\2k\u01be\3\2\2\2m\u01c0\3\2\2\2o\u01c2\3\2\2\2q\u01c4")
        buf.write("\3\2\2\2s\u01c6\3\2\2\2u\u01c8\3\2\2\2w\u01ca\3\2\2\2")
        buf.write("y\u01cc\3\2\2\2{\u01ce\3\2\2\2}\u01d7\3\2\2\2\177\u01e7")
        buf.write("\3\2\2\2\u0081\u01eb\3\2\2\2\u0083\u01f5\3\2\2\2\u0085")
        buf.write("\u0207\3\2\2\2\u0087\u020e\3\2\2\2\u0089\u0217\3\2\2\2")
        buf.write("\u008b\u0222\3\2\2\2\u008d\u0230\3\2\2\2\u008f\u0236\3")
        buf.write("\2\2\2\u0091\u0239\3\2\2\2\u0093\u0243\3\2\2\2\u0095\u0096")
        buf.write("\7o\2\2\u0096\u0097\7c\2\2\u0097\u0098\7k\2\2\u0098\u0099")
        buf.write("\7p\2\2\u0099\4\3\2\2\2\u009a\u009b\7t\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7c\2\2\u009d\u009e\7f\2\2\u009e\u009f")
        buf.write("\7K\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\u00a3\7i\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\6\3\2\2\2\u00a6\u00a7\7r\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7K\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae")
        buf.write("\7v\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7i\2\2\u00b0\u00b1")
        buf.write("\7g\2\2\u00b1\u00b2\7t\2\2\u00b2\b\3\2\2\2\u00b3\u00b4")
        buf.write("\7t\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7")
        buf.write("\7f\2\2\u00b7\u00b8\7H\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7v\2\2\u00bc\n")
        buf.write("\3\2\2\2\u00bd\u00be\7r\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0")
        buf.write("\7k\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7H\2\2\u00c3\u00c4\7n\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6")
        buf.write("\7c\2\2\u00c6\u00c7\7v\2\2\u00c7\f\3\2\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc")
        buf.write("\7f\2\2\u00cc\u00cd\7D\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7q\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2")
        buf.write("\7c\2\2\u00d2\u00d3\7p\2\2\u00d3\16\3\2\2\2\u00d4\u00d5")
        buf.write("\7r\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7D\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7p\2\2\u00e0\20")
        buf.write("\3\2\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7f\2\2\u00e5\u00e6\7U\2\2\u00e6\u00e7")
        buf.write("\7v\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7i\2\2\u00eb\22\3\2\2\2\u00ec\u00ed")
        buf.write("\7r\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7v\2\2\u00f1\u00f2\7U\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7i\2\2\u00f7\24\3\2\2\2\u00f8\u00f9")
        buf.write("\7u\2\2\u00f9\u00fa\7w\2\2\u00fa\u00fb\7r\2\2\u00fb\u00fc")
        buf.write("\7g\2\2\u00fc\u00fd\7t\2\2\u00fd\26\3\2\2\2\u00fe\u00ff")
        buf.write("\7r\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7x\2\2\u0102\u0103\7g\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7v\2\2\u0105\u0106\7F\2\2\u0106\u0107\7g\2\2\u0107\u0108")
        buf.write("\7h\2\2\u0108\u0109\7c\2\2\u0109\u010a\7w\2\2\u010a\u010b")
        buf.write("\7n\2\2\u010b\u010c\7v\2\2\u010c\30\3\2\2\2\u010d\u010f")
        buf.write("\t\2\2\2\u010e\u010d\3\2\2\2\u010f\32\3\2\2\2\u0110\u0111")
        buf.write("\7^\2\2\u0111\u0112\7$\2\2\u0112\34\3\2\2\2\u0113\u0119")
        buf.write("\n\3\2\2\u0114\u0119\5\33\16\2\u0115\u0119\t\4\2\2\u0116")
        buf.write("\u0117\7^\2\2\u0117\u0119\t\5\2\2\u0118\u0113\3\2\2\2")
        buf.write("\u0118\u0114\3\2\2\2\u0118\u0115\3\2\2\2\u0118\u0116\3")
        buf.write("\2\2\2\u0119\36\3\2\2\2\u011a\u011b\7c\2\2\u011b\u011c")
        buf.write("\7w\2\2\u011c\u011d\7v\2\2\u011d\u011e\7q\2\2\u011e \3")
        buf.write("\2\2\2\u011f\u0120\7d\2\2\u0120\u0121\7t\2\2\u0121\u0122")
        buf.write("\7g\2\2\u0122\u0123\7c\2\2\u0123\u0124\7m\2\2\u0124\"")
        buf.write("\3\2\2\2\u0125\u0126\7d\2\2\u0126\u0127\7q\2\2\u0127\u0128")
        buf.write("\7q\2\2\u0128\u0129\7n\2\2\u0129\u012a\7g\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7p\2\2\u012c$\3\2\2\2\u012d\u012e")
        buf.write("\7f\2\2\u012e\u012f\7q\2\2\u012f&\3\2\2\2\u0130\u0131")
        buf.write("\7g\2\2\u0131\u0132\7n\2\2\u0132\u0133\7u\2\2\u0133\u0134")
        buf.write("\7g\2\2\u0134(\3\2\2\2\u0135\u0136\7h\2\2\u0136\u0137")
        buf.write("\7c\2\2\u0137\u0138\7n\2\2\u0138\u0139\7u\2\2\u0139\u013a")
        buf.write("\7g\2\2\u013a*\3\2\2\2\u013b\u013c\7h\2\2\u013c\u013d")
        buf.write("\7n\2\2\u013d\u013e\7q\2\2\u013e\u013f\7c\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140,\3\2\2\2\u0141\u0142\7h\2\2\u0142\u0143")
        buf.write("\7q\2\2\u0143\u0144\7t\2\2\u0144.\3\2\2\2\u0145\u0146")
        buf.write("\7h\2\2\u0146\u0147\7w\2\2\u0147\u0148\7p\2\2\u0148\u0149")
        buf.write("\7e\2\2\u0149\u014a\7v\2\2\u014a\u014b\7k\2\2\u014b\u014c")
        buf.write("\7q\2\2\u014c\u014d\7p\2\2\u014d\60\3\2\2\2\u014e\u014f")
        buf.write("\7k\2\2\u014f\u0150\7h\2\2\u0150\62\3\2\2\2\u0151\u0152")
        buf.write("\7k\2\2\u0152\u0153\7p\2\2\u0153\u0154\7v\2\2\u0154\u0155")
        buf.write("\7g\2\2\u0155\u0156\7i\2\2\u0156\u0157\7g\2\2\u0157\u0158")
        buf.write("\7t\2\2\u0158\64\3\2\2\2\u0159\u015a\7t\2\2\u015a\u015b")
        buf.write("\7g\2\2\u015b\u015c\7v\2\2\u015c\u015d\7w\2\2\u015d\u015e")
        buf.write("\7t\2\2\u015e\u015f\7p\2\2\u015f\66\3\2\2\2\u0160\u0161")
        buf.write("\7u\2\2\u0161\u0162\7v\2\2\u0162\u0163\7t\2\2\u0163\u0164")
        buf.write("\7k\2\2\u0164\u0165\7p\2\2\u0165\u0166\7i\2\2\u01668\3")
        buf.write("\2\2\2\u0167\u0168\7v\2\2\u0168\u0169\7t\2\2\u0169\u016a")
        buf.write("\7w\2\2\u016a\u016b\7g\2\2\u016b:\3\2\2\2\u016c\u016d")
        buf.write("\7x\2\2\u016d\u016e\7q\2\2\u016e\u016f\7k\2\2\u016f\u0170")
        buf.write("\7f\2\2\u0170<\3\2\2\2\u0171\u0172\7y\2\2\u0172\u0173")
        buf.write("\7j\2\2\u0173\u0174\7k\2\2\u0174\u0175\7n\2\2\u0175\u0176")
        buf.write("\7g\2\2\u0176>\3\2\2\2\u0177\u0178\7q\2\2\u0178\u0179")
        buf.write("\7w\2\2\u0179\u017a\7v\2\2\u017a@\3\2\2\2\u017b\u017c")
        buf.write("\7e\2\2\u017c\u017d\7q\2\2\u017d\u017e\7p\2\2\u017e\u017f")
        buf.write("\7v\2\2\u017f\u0180\7k\2\2\u0180\u0181\7p\2\2\u0181\u0182")
        buf.write("\7w\2\2\u0182\u0183\7g\2\2\u0183B\3\2\2\2\u0184\u0185")
        buf.write("\7q\2\2\u0185\u0186\7h\2\2\u0186D\3\2\2\2\u0187\u0188")
        buf.write("\7k\2\2\u0188\u0189\7p\2\2\u0189\u018a\7j\2\2\u018a\u018b")
        buf.write("\7g\2\2\u018b\u018c\7t\2\2\u018c\u018d\7k\2\2\u018d\u018e")
        buf.write("\7v\2\2\u018eF\3\2\2\2\u018f\u0190\7c\2\2\u0190\u0191")
        buf.write("\7t\2\2\u0191\u0192\7t\2\2\u0192\u0193\7c\2\2\u0193\u0194")
        buf.write("\7{\2\2\u0194H\3\2\2\2\u0195\u0196\7-\2\2\u0196J\3\2\2")
        buf.write("\2\u0197\u0198\7/\2\2\u0198L\3\2\2\2\u0199\u019a\7,\2")
        buf.write("\2\u019aN\3\2\2\2\u019b\u019c\7\61\2\2\u019cP\3\2\2\2")
        buf.write("\u019d\u019e\7\'\2\2\u019eR\3\2\2\2\u019f\u01a0\7(\2\2")
        buf.write("\u01a0\u01a1\7(\2\2\u01a1T\3\2\2\2\u01a2\u01a3\7~\2\2")
        buf.write("\u01a3\u01a4\7~\2\2\u01a4V\3\2\2\2\u01a5\u01a6\7?\2\2")
        buf.write("\u01a6\u01a7\7?\2\2\u01a7X\3\2\2\2\u01a8\u01a9\7#\2\2")
        buf.write("\u01a9\u01aa\7?\2\2\u01aaZ\3\2\2\2\u01ab\u01ac\7>\2\2")
        buf.write("\u01ac\\\3\2\2\2\u01ad\u01ae\7@\2\2\u01ae^\3\2\2\2\u01af")
        buf.write("\u01b0\7>\2\2\u01b0\u01b1\7?\2\2\u01b1`\3\2\2\2\u01b2")
        buf.write("\u01b3\7@\2\2\u01b3\u01b4\7?\2\2\u01b4b\3\2\2\2\u01b5")
        buf.write("\u01b6\7<\2\2\u01b6\u01b7\7<\2\2\u01b7d\3\2\2\2\u01b8")
        buf.write("\u01b9\7#\2\2\u01b9f\3\2\2\2\u01ba\u01bb\7]\2\2\u01bb")
        buf.write("h\3\2\2\2\u01bc\u01bd\7_\2\2\u01bdj\3\2\2\2\u01be\u01bf")
        buf.write("\7}\2\2\u01bfl\3\2\2\2\u01c0\u01c1\7\177\2\2\u01c1n\3")
        buf.write("\2\2\2\u01c2\u01c3\7*\2\2\u01c3p\3\2\2\2\u01c4\u01c5\7")
        buf.write("+\2\2\u01c5r\3\2\2\2\u01c6\u01c7\7.\2\2\u01c7t\3\2\2\2")
        buf.write("\u01c8\u01c9\7=\2\2\u01c9v\3\2\2\2\u01ca\u01cb\7<\2\2")
        buf.write("\u01cbx\3\2\2\2\u01cc\u01cd\7?\2\2\u01cdz\3\2\2\2\u01ce")
        buf.write("\u01d2\t\6\2\2\u01cf\u01d1\t\7\2\2\u01d0\u01cf\3\2\2\2")
        buf.write("\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3")
        buf.write("\2\2\2\u01d3|\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d8")
        buf.write("\5\u0083B\2\u01d6\u01d8\7\62\2\2\u01d7\u01d5\3\2\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\b?\2\2")
        buf.write("\u01da~\3\2\2\2\u01db\u01dd\5}?\2\u01dc\u01db\3\2\2\2")
        buf.write("\u01dc\u01dd\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\5")
        buf.write("\u0085C\2\u01df\u01e0\5\u0087D\2\u01e0\u01e8\3\2\2\2\u01e1")
        buf.write("\u01e2\5}?\2\u01e2\u01e3\5\u0085C\2\u01e3\u01e8\3\2\2")
        buf.write("\2\u01e4\u01e5\5}?\2\u01e5\u01e6\5\u0087D\2\u01e6\u01e8")
        buf.write("\3\2\2\2\u01e7\u01dc\3\2\2\2\u01e7\u01e1\3\2\2\2\u01e7")
        buf.write("\u01e4\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\b@\3\2")
        buf.write("\u01ea\u0080\3\2\2\2\u01eb\u01ef\7$\2\2\u01ec\u01ee\5")
        buf.write("\35\17\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f2\3\2\2\2")
        buf.write("\u01f1\u01ef\3\2\2\2\u01f2\u01f3\7$\2\2\u01f3\u01f4\b")
        buf.write("A\4\2\u01f4\u0082\3\2\2\2\u01f5\u01f9\t\b\2\2\u01f6\u01f8")
        buf.write("\t\t\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u0204\3\2\2\2")
        buf.write("\u01fb\u01f9\3\2\2\2\u01fc\u01fe\7a\2\2\u01fd\u01ff\t")
        buf.write("\t\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u01fe")
        buf.write("\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0203\3\2\2\2\u0202")
        buf.write("\u01fc\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2\2")
        buf.write("\u0204\u0205\3\2\2\2\u0205\u0084\3\2\2\2\u0206\u0204\3")
        buf.write("\2\2\2\u0207\u020b\7\60\2\2\u0208\u020a\t\t\2\2\u0209")
        buf.write("\u0208\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2")
        buf.write("\u020b\u020c\3\2\2\2\u020c\u0086\3\2\2\2\u020d\u020b\3")
        buf.write("\2\2\2\u020e\u0210\t\n\2\2\u020f\u0211\t\13\2\2\u0210")
        buf.write("\u020f\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0213\3\2\2\2")
        buf.write("\u0212\u0214\t\t\2\2\u0213\u0212\3\2\2\2\u0214\u0215\3")
        buf.write("\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0088")
        buf.write("\3\2\2\2\u0217\u0218\7\61\2\2\u0218\u0219\7\61\2\2\u0219")
        buf.write("\u021d\3\2\2\2\u021a\u021c\n\f\2\2\u021b\u021a\3\2\2\2")
        buf.write("\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3")
        buf.write("\2\2\2\u021e\u0220\3\2\2\2\u021f\u021d\3\2\2\2\u0220\u0221")
        buf.write("\bE\5\2\u0221\u008a\3\2\2\2\u0222\u0223\7\61\2\2\u0223")
        buf.write("\u0227\7,\2\2\u0224\u0226\13\2\2\2\u0225\u0224\3\2\2\2")
        buf.write("\u0226\u0229\3\2\2\2\u0227\u0228\3\2\2\2\u0227\u0225\3")
        buf.write("\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022b")
        buf.write("\7,\2\2\u022b\u022c\7\61\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write("\u022e\bF\5\2\u022e\u008c\3\2\2\2\u022f\u0231\t\r\2\2")
        buf.write("\u0230\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235")
        buf.write("\bG\5\2\u0235\u008e\3\2\2\2\u0236\u0237\13\2\2\2\u0237")
        buf.write("\u0238\bH\6\2\u0238\u0090\3\2\2\2\u0239\u023d\7$\2\2\u023a")
        buf.write("\u023c\5\35\17\2\u023b\u023a\3\2\2\2\u023c\u023f\3\2\2")
        buf.write("\2\u023d\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0240")
        buf.write("\3\2\2\2\u023f\u023d\3\2\2\2\u0240\u0241\5\31\r\2\u0241")
        buf.write("\u0242\bI\7\2\u0242\u0092\3\2\2\2\u0243\u0247\7$\2\2\u0244")
        buf.write("\u0246\5\35\17\2\u0245\u0244\3\2\2\2\u0246\u0249\3\2\2")
        buf.write("\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u024d")
        buf.write("\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b\7^\2\2\u024b")
        buf.write("\u024e\n\5\2\2\u024c\u024e\n\16\2\2\u024d\u024a\3\2\2")
        buf.write("\2\u024d\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250")
        buf.write("\bJ\b\2\u0250\u0094\3\2\2\2\26\2\u010e\u0118\u01d2\u01d7")
        buf.write("\u01dc\u01e7\u01ef\u01f9\u0200\u0204\u020b\u0210\u0215")
        buf.write("\u021d\u0227\u0232\u023d\u0247\u024d\t\3?\2\3@\3\3A\4")
        buf.write("\b\2\2\3H\5\3I\6\3J\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    AUTO = 12
    BREAK = 13
    BOOLEAN = 14
    DO = 15
    ELSE = 16
    FALSE = 17
    FLOAT = 18
    FOR = 19
    FUNCTION = 20
    IF = 21
    INTEGER = 22
    RETURN = 23
    STRING = 24
    TRUE = 25
    VOID = 26
    WHILE = 27
    OUT = 28
    CONTINUE = 29
    OF = 30
    INHERIT = 31
    ARRAY = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    MOD = 37
    AND = 38
    OR = 39
    EQ = 40
    NOT_EQ = 41
    LT = 42
    GT = 43
    LTE = 44
    GTE = 45
    CONCAT = 46
    NEGATION = 47
    SQ_OPEN = 48
    SQ_CLOSE = 49
    CUR_OPEN = 50
    CUR_CLOSE = 51
    R_OPEN = 52
    R_CLOSE = 53
    COMMA = 54
    SEMI_COLON = 55
    COLON = 56
    ASSIGN = 57
    ID = 58
    INT_LIT = 59
    FLOAT_LIT = 60
    STR_LIT = 61
    CMTLINE = 62
    CMTBLOCK = 63
    WS = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'readInteger'", "'printInteger'", "'readFloat'", 
            "'printFloat'", "'readBoolean'", "'printBoolean'", "'readString'", 
            "'printString'", "'super'", "'preventDefault'", "'auto'", "'break'", 
            "'boolean'", "'do'", "'else'", "'false'", "'float'", "'for'", 
            "'function'", "'if'", "'integer'", "'return'", "'string'", "'true'", 
            "'void'", "'while'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'::'", "'!'", 
            "'['", "']'", "'{'", "'}'", "'('", "')'", "','", "';'", "':'", 
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "VOID", "WHILE", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "EQ", "NOT_EQ", 
            "LT", "GT", "LTE", "GTE", "CONCAT", "NEGATION", "SQ_OPEN", "SQ_CLOSE", 
            "CUR_OPEN", "CUR_CLOSE", "R_OPEN", "R_CLOSE", "COMMA", "SEMI_COLON", 
            "COLON", "ASSIGN", "ID", "INT_LIT", "FLOAT_LIT", "STR_LIT", 
            "CMTLINE", "CMTBLOCK", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "Unterminated", "DoubleQuote", 
                  "Character", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", 
                  "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "VOID", "WHILE", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "AND", "OR", "EQ", "NOT_EQ", "LT", "GT", "LTE", 
                  "GTE", "CONCAT", "NEGATION", "SQ_OPEN", "SQ_CLOSE", "CUR_OPEN", 
                  "CUR_CLOSE", "R_OPEN", "R_CLOSE", "COMMA", "SEMI_COLON", 
                  "COLON", "ASSIGN", "ID", "INT_LIT", "FLOAT_LIT", "STR_LIT", 
                  "DEC", "F_Dec", "F_Exp", "CMTLINE", "CMTBLOCK", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[61] = self.INT_LIT_action 
            actions[62] = self.FLOAT_LIT_action 
            actions[63] = self.STR_LIT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace('_', '') 
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = self.text.replace('_', '') 
     

    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                temp = self.text
                self.text = temp[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                esc = ['\n']
                temp = str(self.text)
                if (temp[-1] in esc):
                    raise UncloseString(temp[1:-1])
                else:
                    raise UncloseString(temp[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                temp = self.text
                raise IllegalEscape(temp[1:])

     


