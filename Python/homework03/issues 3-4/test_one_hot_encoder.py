import unittest
from one_hot_encoder import fit_transform


class MyTestCase(unittest.TestCase):
    def test_fit_transform(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        actual = fit_transform(cities)
        self.assertEqual(actual, exp_transformed_cities)

        animals = ['dog', 'cat', 'cat', 'dog', 'cow', 'fox', 'cow']
        exp_transformed_animals = [
            ('dog', [0, 0, 0, 1]),
            ('cat', [0, 0, 1, 0]),
            ('cat', [0, 0, 1, 0]),
            ('dog', [0, 0, 0, 1]),
            ('cow', [0, 1, 0, 0]),
            ('fox', [1, 0, 0, 0]),
            ('cow', [0, 1, 0, 0]),
        ]
        actual = fit_transform(animals)
        self.assertEqual(actual, exp_transformed_animals)

        ml_models = ['LinearRegression', 'RandomForest', 'SVR', 'LinearRegression', 'XGBRegressor']
        exp_transformed_ml_models = [
            ('LinearRegression', [0, 0, 0, 1]),
            ('RandomForest', [0, 0, 1, 0]),
            ('SVR', [0, 1, 0, 0]),
            ('LinearRegression', [0, 0, 0, 1]),
            ('XGBRegressor', [1, 0, 0, 0]),
        ]
        actual = fit_transform(ml_models)
        self.assertEqual(actual, exp_transformed_ml_models)

        # testing that function raises TypeError when arguments are not passed
        with self.assertRaises(TypeError):
            fit_transform()
