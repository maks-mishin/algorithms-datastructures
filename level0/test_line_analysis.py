import unittest

from tasks.line_analysis import LineAnalysis


class TestLineAnalysis(unittest.TestCase):
    def test_line_analysis(self):
        self.assertEqual(LineAnalysis('*'), True)
        self.assertEqual(LineAnalysis('***'), True)
        self.assertEqual(LineAnalysis('*.*'), True)
        self.assertEqual(LineAnalysis('**.'), False)
        self.assertEqual(LineAnalysis('.'), False)
        self.assertEqual(LineAnalysis('*.*.*.*'), True)
        self.assertEqual(LineAnalysis('*...*...*'), True)


if __name__ == "__main__":
    unittest.main()
