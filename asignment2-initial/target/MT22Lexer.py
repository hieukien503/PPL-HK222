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
        buf.write("\u01c3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\5\2\u0081\n\2\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\u008b\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\7\63\u0143\n\63\f\63\16\63\u0146")
        buf.write("\13\63\3\64\3\64\5\64\u014a\n\64\3\64\3\64\3\65\5\65\u014f")
        buf.write("\n\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u015a\n\65\3\65\3\65\3\66\3\66\7\66\u0160\n\66\f\66\16")
        buf.write("\66\u0163\13\66\3\66\3\66\3\66\3\67\3\67\7\67\u016a\n")
        buf.write("\67\f\67\16\67\u016d\13\67\3\67\3\67\6\67\u0171\n\67\r")
        buf.write("\67\16\67\u0172\7\67\u0175\n\67\f\67\16\67\u0178\13\67")
        buf.write("\38\38\78\u017c\n8\f8\168\u017f\138\39\39\59\u0183\n9")
        buf.write("\39\69\u0186\n9\r9\169\u0187\3:\3:\3:\3:\7:\u018e\n:\f")
        buf.write(":\16:\u0191\13:\3:\3:\3;\3;\3;\7;\u0198\n;\f;\16;\u019b")
        buf.write("\13;\3;\3;\3;\3;\3;\3<\6<\u01a3\n<\r<\16<\u01a4\3<\3<")
        buf.write("\3=\3=\3=\3>\3>\7>\u01ae\n>\f>\16>\u01b1\13>\3>\3>\3>")
        buf.write("\3?\3?\7?\u01b8\n?\f?\16?\u01bb\13?\3?\3?\3?\5?\u01c0")
        buf.write("\n?\3?\3?\3\u0199\2@\3\2\5\2\7\2\t\3\13\4\r\5\17\6\21")
        buf.write("\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21\'")
        buf.write("\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35")
        buf.write("?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62")
        buf.write("i\63k\64m\2o\2q\2s\65u\66w\67y8{9}:\3\2\17\3\3\f\f\7\2")
        buf.write("\n\f\16\17$$))^^\5\2\n\13\16\17))\t\2))^^ddhhppttvv\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2GGgg\4\2-")
        buf.write("-//\4\2\f\f\16\17\5\2\13\f\17\17\"\"\3\2^^\2\u01d1\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\3\u0080\3\2\2\2\5\u0082\3\2\2\2\7\u008a\3\2\2\2\t\u008c")
        buf.write("\3\2\2\2\13\u0091\3\2\2\2\r\u0097\3\2\2\2\17\u009f\3\2")
        buf.write("\2\2\21\u00a2\3\2\2\2\23\u00a7\3\2\2\2\25\u00ad\3\2\2")
        buf.write("\2\27\u00b3\3\2\2\2\31\u00b7\3\2\2\2\33\u00c0\3\2\2\2")
        buf.write("\35\u00c3\3\2\2\2\37\u00cb\3\2\2\2!\u00d2\3\2\2\2#\u00d9")
        buf.write("\3\2\2\2%\u00de\3\2\2\2\'\u00e3\3\2\2\2)\u00e9\3\2\2\2")
        buf.write("+\u00ed\3\2\2\2-\u00f6\3\2\2\2/\u00f9\3\2\2\2\61\u0101")
        buf.write("\3\2\2\2\63\u0107\3\2\2\2\65\u0109\3\2\2\2\67\u010b\3")
        buf.write("\2\2\29\u010d\3\2\2\2;\u010f\3\2\2\2=\u0111\3\2\2\2?\u0114")
        buf.write("\3\2\2\2A\u0117\3\2\2\2C\u011a\3\2\2\2E\u011d\3\2\2\2")
        buf.write("G\u011f\3\2\2\2I\u0121\3\2\2\2K\u0124\3\2\2\2M\u0127\3")
        buf.write("\2\2\2O\u012a\3\2\2\2Q\u012c\3\2\2\2S\u012e\3\2\2\2U\u0130")
        buf.write("\3\2\2\2W\u0132\3\2\2\2Y\u0134\3\2\2\2[\u0136\3\2\2\2")
        buf.write("]\u0138\3\2\2\2_\u013a\3\2\2\2a\u013c\3\2\2\2c\u013e\3")
        buf.write("\2\2\2e\u0140\3\2\2\2g\u0149\3\2\2\2i\u0159\3\2\2\2k\u015d")
        buf.write("\3\2\2\2m\u0167\3\2\2\2o\u0179\3\2\2\2q\u0180\3\2\2\2")
        buf.write("s\u0189\3\2\2\2u\u0194\3\2\2\2w\u01a2\3\2\2\2y\u01a8\3")
        buf.write("\2\2\2{\u01ab\3\2\2\2}\u01b5\3\2\2\2\177\u0081\t\2\2\2")
        buf.write("\u0080\177\3\2\2\2\u0081\4\3\2\2\2\u0082\u0083\7^\2\2")
        buf.write("\u0083\u0084\7$\2\2\u0084\6\3\2\2\2\u0085\u008b\n\3\2")
        buf.write("\2\u0086\u008b\5\5\3\2\u0087\u008b\t\4\2\2\u0088\u0089")
        buf.write("\7^\2\2\u0089\u008b\t\5\2\2\u008a\u0085\3\2\2\2\u008a")
        buf.write("\u0086\3\2\2\2\u008a\u0087\3\2\2\2\u008a\u0088\3\2\2\2")
        buf.write("\u008b\b\3\2\2\2\u008c\u008d\7c\2\2\u008d\u008e\7w\2\2")
        buf.write("\u008e\u008f\7v\2\2\u008f\u0090\7q\2\2\u0090\n\3\2\2\2")
        buf.write("\u0091\u0092\7d\2\2\u0092\u0093\7t\2\2\u0093\u0094\7g")
        buf.write("\2\2\u0094\u0095\7c\2\2\u0095\u0096\7m\2\2\u0096\f\3\2")
        buf.write("\2\2\u0097\u0098\7d\2\2\u0098\u0099\7q\2\2\u0099\u009a")
        buf.write("\7q\2\2\u009a\u009b\7n\2\2\u009b\u009c\7g\2\2\u009c\u009d")
        buf.write("\7c\2\2\u009d\u009e\7p\2\2\u009e\16\3\2\2\2\u009f\u00a0")
        buf.write("\7f\2\2\u00a0\u00a1\7q\2\2\u00a1\20\3\2\2\2\u00a2\u00a3")
        buf.write("\7g\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6")
        buf.write("\7g\2\2\u00a6\22\3\2\2\2\u00a7\u00a8\7h\2\2\u00a8\u00a9")
        buf.write("\7c\2\2\u00a9\u00aa\7n\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\24\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af")
        buf.write("\7n\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\26\3\2\2\2\u00b3\u00b4\7h\2\2\u00b4\u00b5")
        buf.write("\7q\2\2\u00b5\u00b6\7t\2\2\u00b6\30\3\2\2\2\u00b7\u00b8")
        buf.write("\7h\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb")
        buf.write("\7e\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7q\2\2\u00be\u00bf\7p\2\2\u00bf\32\3\2\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7h\2\2\u00c2\34\3\2\2\2\u00c3\u00c4")
        buf.write("\7k\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\u00c8\7i\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\36\3\2\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd")
        buf.write("\7g\2\2\u00cd\u00ce\7v\2\2\u00ce\u00cf\7w\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7p\2\2\u00d1 \3\2\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7i\2\2\u00d8\"")
        buf.write("\3\2\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7t\2\2\u00db\u00dc")
        buf.write("\7w\2\2\u00dc\u00dd\7g\2\2\u00dd$\3\2\2\2\u00de\u00df")
        buf.write("\7x\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2")
        buf.write("\7f\2\2\u00e2&\3\2\2\2\u00e3\u00e4\7y\2\2\u00e4\u00e5")
        buf.write("\7j\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8(\3\2\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb")
        buf.write("\7w\2\2\u00eb\u00ec\7v\2\2\u00ec*\3\2\2\2\u00ed\u00ee")
        buf.write("\7e\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7v\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7w\2\2\u00f4\u00f5\7g\2\2\u00f5,\3\2\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7h\2\2\u00f8.\3\2\2\2\u00f9\u00fa")
        buf.write("\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7j\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100\60\3\2\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7t\2\2\u0104\u0105\7c\2\2\u0105\u0106")
        buf.write("\7{\2\2\u0106\62\3\2\2\2\u0107\u0108\7-\2\2\u0108\64\3")
        buf.write("\2\2\2\u0109\u010a\7/\2\2\u010a\66\3\2\2\2\u010b\u010c")
        buf.write("\7,\2\2\u010c8\3\2\2\2\u010d\u010e\7\61\2\2\u010e:\3\2")
        buf.write("\2\2\u010f\u0110\7\'\2\2\u0110<\3\2\2\2\u0111\u0112\7")
        buf.write("(\2\2\u0112\u0113\7(\2\2\u0113>\3\2\2\2\u0114\u0115\7")
        buf.write("~\2\2\u0115\u0116\7~\2\2\u0116@\3\2\2\2\u0117\u0118\7")
        buf.write("?\2\2\u0118\u0119\7?\2\2\u0119B\3\2\2\2\u011a\u011b\7")
        buf.write("#\2\2\u011b\u011c\7?\2\2\u011cD\3\2\2\2\u011d\u011e\7")
        buf.write(">\2\2\u011eF\3\2\2\2\u011f\u0120\7@\2\2\u0120H\3\2\2\2")
        buf.write("\u0121\u0122\7>\2\2\u0122\u0123\7?\2\2\u0123J\3\2\2\2")
        buf.write("\u0124\u0125\7@\2\2\u0125\u0126\7?\2\2\u0126L\3\2\2\2")
        buf.write("\u0127\u0128\7<\2\2\u0128\u0129\7<\2\2\u0129N\3\2\2\2")
        buf.write("\u012a\u012b\7#\2\2\u012bP\3\2\2\2\u012c\u012d\7]\2\2")
        buf.write("\u012dR\3\2\2\2\u012e\u012f\7_\2\2\u012fT\3\2\2\2\u0130")
        buf.write("\u0131\7}\2\2\u0131V\3\2\2\2\u0132\u0133\7\177\2\2\u0133")
        buf.write("X\3\2\2\2\u0134\u0135\7*\2\2\u0135Z\3\2\2\2\u0136\u0137")
        buf.write("\7+\2\2\u0137\\\3\2\2\2\u0138\u0139\7.\2\2\u0139^\3\2")
        buf.write("\2\2\u013a\u013b\7=\2\2\u013b`\3\2\2\2\u013c\u013d\7<")
        buf.write("\2\2\u013db\3\2\2\2\u013e\u013f\7?\2\2\u013fd\3\2\2\2")
        buf.write("\u0140\u0144\t\6\2\2\u0141\u0143\t\7\2\2\u0142\u0141\3")
        buf.write("\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145f\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u014a")
        buf.write("\5m\67\2\u0148\u014a\7\62\2\2\u0149\u0147\3\2\2\2\u0149")
        buf.write("\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\b\64\2")
        buf.write("\2\u014ch\3\2\2\2\u014d\u014f\5g\64\2\u014e\u014d\3\2")
        buf.write("\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151")
        buf.write("\5o8\2\u0151\u0152\5q9\2\u0152\u015a\3\2\2\2\u0153\u0154")
        buf.write("\5g\64\2\u0154\u0155\5o8\2\u0155\u015a\3\2\2\2\u0156\u0157")
        buf.write("\5g\64\2\u0157\u0158\5q9\2\u0158\u015a\3\2\2\2\u0159\u014e")
        buf.write("\3\2\2\2\u0159\u0153\3\2\2\2\u0159\u0156\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\u015c\b\65\3\2\u015cj\3\2\2\2\u015d")
        buf.write("\u0161\7$\2\2\u015e\u0160\5\7\4\2\u015f\u015e\3\2\2\2")
        buf.write("\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3")
        buf.write("\2\2\2\u0162\u0164\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165")
        buf.write("\7$\2\2\u0165\u0166\b\66\4\2\u0166l\3\2\2\2\u0167\u016b")
        buf.write("\t\b\2\2\u0168\u016a\t\t\2\2\u0169\u0168\3\2\2\2\u016a")
        buf.write("\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u0176\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u0170\7")
        buf.write("a\2\2\u016f\u0171\t\t\2\2\u0170\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0175\3\2\2\2\u0174\u016e\3\2\2\2\u0175\u0178\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177n\3\2\2")
        buf.write("\2\u0178\u0176\3\2\2\2\u0179\u017d\7\60\2\2\u017a\u017c")
        buf.write("\t\t\2\2\u017b\u017a\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017ep\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0182\t\n\2\2\u0181\u0183\t\13\2")
        buf.write("\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185")
        buf.write("\3\2\2\2\u0184\u0186\t\t\2\2\u0185\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188r\3\2\2\2\u0189\u018a\7\61\2\2\u018a\u018b\7\61")
        buf.write("\2\2\u018b\u018f\3\2\2\2\u018c\u018e\n\f\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u018f\3\2\2\2")
        buf.write("\u0192\u0193\b:\5\2\u0193t\3\2\2\2\u0194\u0195\7\61\2")
        buf.write("\2\u0195\u0199\7,\2\2\u0196\u0198\13\2\2\2\u0197\u0196")
        buf.write("\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u019a\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u019a\u019c\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019c\u019d\7,\2\2\u019d\u019e\7\61\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019f\u01a0\b;\5\2\u01a0v\3\2\2\2\u01a1\u01a3\t")
        buf.write("\r\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a7\b<\5\2\u01a7x\3\2\2\2\u01a8\u01a9\13\2\2\2\u01a9")
        buf.write("\u01aa\b=\6\2\u01aaz\3\2\2\2\u01ab\u01af\7$\2\2\u01ac")
        buf.write("\u01ae\5\7\4\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2")
        buf.write("\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b2\3")
        buf.write("\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\5\3\2\2\u01b3\u01b4")
        buf.write("\b>\7\2\u01b4|\3\2\2\2\u01b5\u01b9\7$\2\2\u01b6\u01b8")
        buf.write("\5\7\4\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9")
        buf.write("\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bf\3\2\2\2")
        buf.write("\u01bb\u01b9\3\2\2\2\u01bc\u01bd\7^\2\2\u01bd\u01c0\n")
        buf.write("\5\2\2\u01be\u01c0\n\16\2\2\u01bf\u01bc\3\2\2\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\b?\b\2")
        buf.write("\u01c2~\3\2\2\2\26\2\u0080\u008a\u0144\u0149\u014e\u0159")
        buf.write("\u0161\u016b\u0172\u0176\u017d\u0182\u0187\u018f\u0199")
        buf.write("\u01a4\u01af\u01b9\u01bf\t\3\64\2\3\65\3\3\66\4\b\2\2")
        buf.write("\3=\5\3>\6\3?\7")
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

     


