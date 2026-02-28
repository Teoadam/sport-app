import unittest

from src.league_table import calculate_points, goal_difference, total_matches


class TestLeagueTable(unittest.TestCase):
    def test_calculate_points_nominal(self):
        self.assertEqual(calculate_points(10, 5, 3), 35)

    def test_calculate_points_all_zero(self):
        self.assertEqual(calculate_points(0, 0, 0), 0)

    def test_calculate_points_rejects_negative(self):
        with self.assertRaises(ValueError):
            calculate_points(-1, 0, 0)

    def test_calculate_points_rejects_non_int(self):
        with self.assertRaises(TypeError):
            calculate_points(1, 2.5, 0)

    def test_calculate_points_rejects_bool(self):
        with self.assertRaises(TypeError):
            calculate_points(True, 2, 0)

    def test_goal_difference_nominal(self):
        self.assertEqual(goal_difference(20, 12), 8)

    def test_goal_difference_negative_result(self):
        self.assertEqual(goal_difference(4, 9), -5)

    def test_goal_difference_rejects_negative(self):
        with self.assertRaises(ValueError):
            goal_difference(2, -1)

    def test_total_matches_nominal(self):
        self.assertEqual(total_matches(8, 4, 6), 18)

    def test_total_matches_rejects_non_int(self):
        with self.assertRaises(TypeError):
            total_matches(8, "4", 6)


if __name__ == "__main__":
    unittest.main()
