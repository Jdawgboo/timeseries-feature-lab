import unittest
from tool import rolling_features


class FeatureTests(unittest.TestCase):
    def test_generates_trailing_features(self):
        rows = rolling_features([1.0, 3.0, 2.0], 2)
        self.assertEqual(rows[1]["mean"], 2.0)
        self.assertEqual(rows[2]["delta"], -1.0)
        self.assertEqual(rows[2]["min"], 2.0)


if __name__ == "__main__":
    unittest.main()
