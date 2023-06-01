import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 101))

    def test_intlit(self):
        """test integer literal"""
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 102))

    def test_floatlit(self):
        """test float literal"""
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 103))

    def test_stringlit(self):
        """test string literal"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,
                        """He asked me: \\"Where is John?\\",<EOF>""", 104))

    def test_stringlit(self):
        """test string literal"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """,
                        """He asked me: \\"Where is John?\\",<EOF>""", 104))
