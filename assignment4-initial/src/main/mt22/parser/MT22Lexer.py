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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\5\2\u0081\n\2\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\5\4\u0089\n\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\7\63\u0141\n\63\f\63\16\63\u0144\13\63\3\64\3")
        buf.write("\64\5\64\u0148\n\64\3\64\3\64\3\65\5\65\u014d\n\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0158\n")
        buf.write("\65\3\65\3\65\3\66\3\66\7\66\u015e\n\66\f\66\16\66\u0161")
        buf.write("\13\66\3\66\3\66\3\66\3\67\3\67\7\67\u0168\n\67\f\67\16")
        buf.write("\67\u016b\13\67\3\67\3\67\6\67\u016f\n\67\r\67\16\67\u0170")
        buf.write("\7\67\u0173\n\67\f\67\16\67\u0176\13\67\38\38\78\u017a")
        buf.write("\n8\f8\168\u017d\138\39\39\59\u0181\n9\39\69\u0184\n9")
        buf.write("\r9\169\u0185\3:\3:\3:\3:\7:\u018c\n:\f:\16:\u018f\13")
        buf.write(":\3:\3:\3;\3;\3;\7;\u0196\n;\f;\16;\u0199\13;\3;\3;\3")
        buf.write(";\3;\3;\3<\6<\u01a1\n<\r<\16<\u01a2\3<\3<\3=\3=\3=\3>")
        buf.write("\3>\7>\u01ac\n>\f>\16>\u01af\13>\3>\3>\3>\3?\3?\7?\u01b6")
        buf.write("\n?\f?\16?\u01b9\13?\3?\3?\3?\5?\u01be\n?\3?\3?\3\u0197")
        buf.write("\2@\3\2\5\2\7\2\t\3\13\4\r\5\17\6\21\7\23\b\25\t\27\n")
        buf.write("\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26")
        buf.write("\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#")
        buf.write("K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\2o\2q\2")
        buf.write("s\65u\66w\67y8{9}:\3\2\17\3\3\f\f\7\2\n\f\16\17$$))^^")
        buf.write("\5\2\n\13\16\17))\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\4\2\f\f\16\17\5\2\13\f\17\17\"")
        buf.write("\"\t\2))^^ddhhppttvv\3\2^^\2\u01ce\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\u0080\3\2")
        buf.write("\2\2\5\u0082\3\2\2\2\7\u0088\3\2\2\2\t\u008a\3\2\2\2\13")
        buf.write("\u008f\3\2\2\2\r\u0095\3\2\2\2\17\u009d\3\2\2\2\21\u00a0")
        buf.write("\3\2\2\2\23\u00a5\3\2\2\2\25\u00ab\3\2\2\2\27\u00b1\3")
        buf.write("\2\2\2\31\u00b5\3\2\2\2\33\u00be\3\2\2\2\35\u00c1\3\2")
        buf.write("\2\2\37\u00c9\3\2\2\2!\u00d0\3\2\2\2#\u00d7\3\2\2\2%\u00dc")
        buf.write("\3\2\2\2\'\u00e1\3\2\2\2)\u00e7\3\2\2\2+\u00eb\3\2\2\2")
        buf.write("-\u00f4\3\2\2\2/\u00f7\3\2\2\2\61\u00ff\3\2\2\2\63\u0105")
        buf.write("\3\2\2\2\65\u0107\3\2\2\2\67\u0109\3\2\2\29\u010b\3\2")
        buf.write("\2\2;\u010d\3\2\2\2=\u010f\3\2\2\2?\u0112\3\2\2\2A\u0115")
        buf.write("\3\2\2\2C\u0118\3\2\2\2E\u011b\3\2\2\2G\u011d\3\2\2\2")
        buf.write("I\u011f\3\2\2\2K\u0122\3\2\2\2M\u0125\3\2\2\2O\u0128\3")
        buf.write("\2\2\2Q\u012a\3\2\2\2S\u012c\3\2\2\2U\u012e\3\2\2\2W\u0130")
        buf.write("\3\2\2\2Y\u0132\3\2\2\2[\u0134\3\2\2\2]\u0136\3\2\2\2")
        buf.write("_\u0138\3\2\2\2a\u013a\3\2\2\2c\u013c\3\2\2\2e\u013e\3")
        buf.write("\2\2\2g\u0147\3\2\2\2i\u0157\3\2\2\2k\u015b\3\2\2\2m\u0165")
        buf.write("\3\2\2\2o\u0177\3\2\2\2q\u017e\3\2\2\2s\u0187\3\2\2\2")
        buf.write("u\u0192\3\2\2\2w\u01a0\3\2\2\2y\u01a6\3\2\2\2{\u01a9\3")
        buf.write("\2\2\2}\u01b3\3\2\2\2\177\u0081\t\2\2\2\u0080\177\3\2")
        buf.write("\2\2\u0081\4\3\2\2\2\u0082\u0083\7^\2\2\u0083\u0084\7")
        buf.write("$\2\2\u0084\6\3\2\2\2\u0085\u0089\n\3\2\2\u0086\u0089")
        buf.write("\5\5\3\2\u0087\u0089\t\4\2\2\u0088\u0085\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089\b\3\2\2\2\u008a")
        buf.write("\u008b\7c\2\2\u008b\u008c\7w\2\2\u008c\u008d\7v\2\2\u008d")
        buf.write("\u008e\7q\2\2\u008e\n\3\2\2\2\u008f\u0090\7d\2\2\u0090")
        buf.write("\u0091\7t\2\2\u0091\u0092\7g\2\2\u0092\u0093\7c\2\2\u0093")
        buf.write("\u0094\7m\2\2\u0094\f\3\2\2\2\u0095\u0096\7d\2\2\u0096")
        buf.write("\u0097\7q\2\2\u0097\u0098\7q\2\2\u0098\u0099\7n\2\2\u0099")
        buf.write("\u009a\7g\2\2\u009a\u009b\7c\2\2\u009b\u009c\7p\2\2\u009c")
        buf.write("\16\3\2\2\2\u009d\u009e\7f\2\2\u009e\u009f\7q\2\2\u009f")
        buf.write("\20\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7n\2\2\u00a2")
        buf.write("\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\22\3\2\2\2\u00a5")
        buf.write("\u00a6\7h\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7n\2\2\u00a8")
        buf.write("\u00a9\7u\2\2\u00a9\u00aa\7g\2\2\u00aa\24\3\2\2\2\u00ab")
        buf.write("\u00ac\7h\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae\7q\2\2\u00ae")
        buf.write("\u00af\7c\2\2\u00af\u00b0\7v\2\2\u00b0\26\3\2\2\2\u00b1")
        buf.write("\u00b2\7h\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7t\2\2\u00b4")
        buf.write("\30\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7\7w\2\2\u00b7")
        buf.write("\u00b8\7p\2\2\u00b8\u00b9\7e\2\2\u00b9\u00ba\7v\2\2\u00ba")
        buf.write("\u00bb\7k\2\2\u00bb\u00bc\7q\2\2\u00bc\u00bd\7p\2\2\u00bd")
        buf.write("\32\3\2\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7h\2\2\u00c0")
        buf.write("\34\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3")
        buf.write("\u00c4\7v\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7i\2\2\u00c6")
        buf.write("\u00c7\7g\2\2\u00c7\u00c8\7t\2\2\u00c8\36\3\2\2\2\u00c9")
        buf.write("\u00ca\7t\2\2\u00ca\u00cb\7g\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\u00cd\7w\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7p\2\2\u00cf")
        buf.write(" \3\2\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7v\2\2\u00d2")
        buf.write("\u00d3\7t\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5")
        buf.write("\u00d6\7i\2\2\u00d6\"\3\2\2\2\u00d7\u00d8\7v\2\2\u00d8")
        buf.write("\u00d9\7t\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7g\2\2\u00db")
        buf.write("$\3\2\2\2\u00dc\u00dd\7x\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7k\2\2\u00df\u00e0\7f\2\2\u00e0&\3\2\2\2\u00e1")
        buf.write("\u00e2\7y\2\2\u00e2\u00e3\7j\2\2\u00e3\u00e4\7k\2\2\u00e4")
        buf.write("\u00e5\7n\2\2\u00e5\u00e6\7g\2\2\u00e6(\3\2\2\2\u00e7")
        buf.write("\u00e8\7q\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("*\3\2\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7q\2\2\u00ed")
        buf.write("\u00ee\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7k\2\2\u00f0")
        buf.write("\u00f1\7p\2\2\u00f1\u00f2\7w\2\2\u00f2\u00f3\7g\2\2\u00f3")
        buf.write(",\3\2\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7h\2\2\u00f6")
        buf.write(".\3\2\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7p\2\2\u00f9")
        buf.write("\u00fa\7j\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc\7t\2\2\u00fc")
        buf.write("\u00fd\7k\2\2\u00fd\u00fe\7v\2\2\u00fe\60\3\2\2\2\u00ff")
        buf.write("\u0100\7c\2\2\u0100\u0101\7t\2\2\u0101\u0102\7t\2\2\u0102")
        buf.write("\u0103\7c\2\2\u0103\u0104\7{\2\2\u0104\62\3\2\2\2\u0105")
        buf.write("\u0106\7-\2\2\u0106\64\3\2\2\2\u0107\u0108\7/\2\2\u0108")
        buf.write("\66\3\2\2\2\u0109\u010a\7,\2\2\u010a8\3\2\2\2\u010b\u010c")
        buf.write("\7\61\2\2\u010c:\3\2\2\2\u010d\u010e\7\'\2\2\u010e<\3")
        buf.write("\2\2\2\u010f\u0110\7(\2\2\u0110\u0111\7(\2\2\u0111>\3")
        buf.write("\2\2\2\u0112\u0113\7~\2\2\u0113\u0114\7~\2\2\u0114@\3")
        buf.write("\2\2\2\u0115\u0116\7?\2\2\u0116\u0117\7?\2\2\u0117B\3")
        buf.write("\2\2\2\u0118\u0119\7#\2\2\u0119\u011a\7?\2\2\u011aD\3")
        buf.write("\2\2\2\u011b\u011c\7>\2\2\u011cF\3\2\2\2\u011d\u011e\7")
        buf.write("@\2\2\u011eH\3\2\2\2\u011f\u0120\7>\2\2\u0120\u0121\7")
        buf.write("?\2\2\u0121J\3\2\2\2\u0122\u0123\7@\2\2\u0123\u0124\7")
        buf.write("?\2\2\u0124L\3\2\2\2\u0125\u0126\7<\2\2\u0126\u0127\7")
        buf.write("<\2\2\u0127N\3\2\2\2\u0128\u0129\7#\2\2\u0129P\3\2\2\2")
        buf.write("\u012a\u012b\7]\2\2\u012bR\3\2\2\2\u012c\u012d\7_\2\2")
        buf.write("\u012dT\3\2\2\2\u012e\u012f\7}\2\2\u012fV\3\2\2\2\u0130")
        buf.write("\u0131\7\177\2\2\u0131X\3\2\2\2\u0132\u0133\7*\2\2\u0133")
        buf.write("Z\3\2\2\2\u0134\u0135\7+\2\2\u0135\\\3\2\2\2\u0136\u0137")
        buf.write("\7.\2\2\u0137^\3\2\2\2\u0138\u0139\7=\2\2\u0139`\3\2\2")
        buf.write("\2\u013a\u013b\7<\2\2\u013bb\3\2\2\2\u013c\u013d\7?\2")
        buf.write("\2\u013dd\3\2\2\2\u013e\u0142\t\5\2\2\u013f\u0141\t\6")
        buf.write("\2\2\u0140\u013f\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143f\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0145\u0148\5m\67\2\u0146\u0148\7\62\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014a\b\64\2\2\u014ah\3\2\2\2\u014b\u014d\5g\64")
        buf.write("\2\u014c\u014b\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u014f\5o8\2\u014f\u0150\5q9\2\u0150\u0158")
        buf.write("\3\2\2\2\u0151\u0152\5g\64\2\u0152\u0153\5o8\2\u0153\u0158")
        buf.write("\3\2\2\2\u0154\u0155\5g\64\2\u0155\u0156\5q9\2\u0156\u0158")
        buf.write("\3\2\2\2\u0157\u014c\3\2\2\2\u0157\u0151\3\2\2\2\u0157")
        buf.write("\u0154\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\b\65\3")
        buf.write("\2\u015aj\3\2\2\2\u015b\u015f\7$\2\2\u015c\u015e\5\7\4")
        buf.write("\2\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0162\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0162\u0163\7$\2\2\u0163\u0164\b\66\4\2")
        buf.write("\u0164l\3\2\2\2\u0165\u0169\t\7\2\2\u0166\u0168\t\b\2")
        buf.write("\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0174\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016e\7a\2\2\u016d\u016f\t\b\2\2")
        buf.write("\u016e\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u016e\3")
        buf.write("\2\2\2\u0170\u0171\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u016c")
        buf.write("\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175n\3\2\2\2\u0176\u0174\3\2\2\2\u0177")
        buf.write("\u017b\7\60\2\2\u0178\u017a\t\b\2\2\u0179\u0178\3\2\2")
        buf.write("\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017cp\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0180")
        buf.write("\t\t\2\2\u017f\u0181\t\n\2\2\u0180\u017f\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0184\t\b\2\2")
        buf.write("\u0183\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0183\3")
        buf.write("\2\2\2\u0185\u0186\3\2\2\2\u0186r\3\2\2\2\u0187\u0188")
        buf.write("\7\61\2\2\u0188\u0189\7\61\2\2\u0189\u018d\3\2\2\2\u018a")
        buf.write("\u018c\n\13\2\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2")
        buf.write("\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190")
        buf.write("\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\b:\5\2\u0191")
        buf.write("t\3\2\2\2\u0192\u0193\7\61\2\2\u0193\u0197\7,\2\2\u0194")
        buf.write("\u0196\13\2\2\2\u0195\u0194\3\2\2\2\u0196\u0199\3\2\2")
        buf.write("\2\u0197\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u019a")
        buf.write("\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b\7,\2\2\u019b")
        buf.write("\u019c\7\61\2\2\u019c\u019d\3\2\2\2\u019d\u019e\b;\5\2")
        buf.write("\u019ev\3\2\2\2\u019f\u01a1\t\f\2\2\u01a0\u019f\3\2\2")
        buf.write("\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\b<\5\2\u01a5")
        buf.write("x\3\2\2\2\u01a6\u01a7\13\2\2\2\u01a7\u01a8\b=\6\2\u01a8")
        buf.write("z\3\2\2\2\u01a9\u01ad\7$\2\2\u01aa\u01ac\5\7\4\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01b0\u01b1\5\3\2\2\u01b1\u01b2\b>\7\2\u01b2|\3")
        buf.write("\2\2\2\u01b3\u01b7\7$\2\2\u01b4\u01b6\5\7\4\2\u01b5\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01bd\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01ba\u01bb\7^\2\2\u01bb\u01be\n\r\2\2\u01bc\u01be\n")
        buf.write("\16\2\2\u01bd\u01ba\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bf\u01c0\b?\b\2\u01c0~\3\2\2\2\26\2")
        buf.write("\u0080\u0088\u0142\u0147\u014c\u0157\u015f\u0169\u0170")
        buf.write("\u0174\u017b\u0180\u0185\u018d\u0197\u01a2\u01ad\u01b7")
        buf.write("\u01bd\t\3\64\2\3\65\3\3\66\4\b\2\2\3=\5\3>\6\3?\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INTEGER = 11
    RETURN = 12
    STRING = 13
    TRUE = 14
    VOID = 15
    WHILE = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    AND = 27
    OR = 28
    EQ = 29
    NOT_EQ = 30
    LT = 31
    GT = 32
    LTE = 33
    GTE = 34
    CONCAT = 35
    NEGATION = 36
    SQ_OPEN = 37
    SQ_CLOSE = 38
    CUR_OPEN = 39
    CUR_CLOSE = 40
    R_OPEN = 41
    R_CLOSE = 42
    COMMA = 43
    SEMI_COLON = 44
    COLON = 45
    ASSIGN = 46
    ID = 47
    INT_LIT = 48
    FLOAT_LIT = 49
    STR_LIT = 50
    CMTLINE = 51
    CMTBLOCK = 52
    WS = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'void'", "'while'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'::'", "'!'", "'['", "']'", "'{'", "'}'", "'('", "')'", 
            "','", "';'", "':'", "'='" ]

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

    ruleNames = [ "Unterminated", "DoubleQuote", "Character", "AUTO", "BREAK", 
                  "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", 
                  "IF", "INTEGER", "RETURN", "STRING", "TRUE", "VOID", "WHILE", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "AND", "OR", "EQ", "NOT_EQ", "LT", 
                  "GT", "LTE", "GTE", "CONCAT", "NEGATION", "SQ_OPEN", "SQ_CLOSE", 
                  "CUR_OPEN", "CUR_CLOSE", "R_OPEN", "R_CLOSE", "COMMA", 
                  "SEMI_COLON", "COLON", "ASSIGN", "ID", "INT_LIT", "FLOAT_LIT", 
                  "STR_LIT", "DEC", "F_Dec", "F_Exp", "CMTLINE", "CMTBLOCK", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[50] = self.INT_LIT_action 
            actions[51] = self.FLOAT_LIT_action 
            actions[52] = self.STR_LIT_action 
            actions[59] = self.ERROR_CHAR_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
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

     


