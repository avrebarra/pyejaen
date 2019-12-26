import unittest


from pyejaen import parse, parse_tree


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
                "expected": [
                    "s", "e", "se", "m", "a", "ma", "sema",
                    "r", "a", "ra", "ng", "rang", "semarang"
                ]
            },
            {
                "given": "((((ku)(ra))((ku)(ra)))(((ni)(n))(ja)))",
                "expected": [
                    "k", "u", "ku", "r", "a", "ra", "kura",
                    "k", "u", "ku", "r", "a", "ra", "kura", "kurakura",
                    "n", "i", "ni", "n", "nin", "j", "a", "ja", "ninja",
                    "kurakuraninja"
                ]
            }
        ]

        # act and assert
        for case in cases:
            result = parse(case["given"])
            self.assertEqual(result, case["expected"])

    # Test that it returns correct spelling tree breakdowns
    def test_spell_tree_correctness(self):
        # arrange
        cases = [
            {
                "given": "((a)((ya)(m)))",
                "expected": {
                    "value": "ayam",
                    "parent": True,
                    "children": [
                        {
                            "value": "ayam",
                            "children": [
                                {"value": "a"},
                                {
                                    "value": "yam",
                                    "children": [
                                        {
                                            "value": "ya",
                                            "children": [
                                                {"value": "y"},
                                                {"value": "a"}
                                            ]
                                        },
                                        {"value": "m"}
                                    ]
                                }
                            ]
                        }
                    ],
                },
            },
            {
                "given": "(((se)(ma))((ra)(!ng)))",
                "expected": {
                    "value": "semarang",
                    "parent": True,
                    "children": [
                        {
                            "value": "semarang",
                            "children": [
                                {
                                    "value": "sema",
                                    "children": [
                                        {
                                            "value": "se",
                                            "children": [
                                                {
                                                    "value": "s"
                                                },
                                                {
                                                    "value": "e"
                                                },

                                            ]
                                        },
                                        {
                                            "value": "ma",
                                            "children": [
                                                {
                                                    "value": "m"
                                                },
                                                {
                                                    "value": "a"
                                                },

                                            ]
                                        },
                                    ]
                                },
                                {
                                    "value": "rang",
                                    "children": [
                                        {
                                            "value": "ra",
                                            "children": [
                                                {
                                                    "value": "r"
                                                },
                                                {
                                                    "value": "a"
                                                },

                                            ]
                                        },
                                        {
                                            "value": "ng"
                                        },

                                    ]
                                },
                            ]
                        }
                    ],
                },
            },
        ]

        # act and assert
        for case in cases:
            result = parse_tree(case["given"])
            self.assertEqual(result, case["expected"])


if __name__ == "__main__":
    unittest.main()
