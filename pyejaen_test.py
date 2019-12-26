import unittest


from pyejaen import parse


class TestParse(unittest.TestCase):
    # Test that it returns correct spelling breakdowns
    def test_spell_correctness(self):
        # arrange
        cases = [
            {
                "given": "((a)((ya)(m)))",
                "expected": ["a", "y", "a", "ya", "m", "yam", "ayam"]
            }
        ]

        # act and assert
        for case in cases:
            result = parse(case["given"])
            self.assertEqual(result, case["expected"])


if __name__ == '__main__':
    unittest.main()
