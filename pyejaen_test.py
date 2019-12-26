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
            },
            {
                "given": "(((se)(ma))((ra)(!ng)))",
                "expected": ["s", "e", "se", "m", "a", "ma", "sema", "r", "a", "ra", "ng", "rang", "semarang"]
            }
        ]

        # act and assert
        for case in cases:
            result = parse(case["given"])
            self.assertEqual(result, case["expected"])


if __name__ == '__main__':
    unittest.main()
