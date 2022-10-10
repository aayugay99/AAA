from one_hot_encoder import fit_transform
import pytest


@pytest.mark.parametrize(
    "input_list, output",
    [
        (
            [
                'LinearRegression', 'RandomForest', 'SVR', 'LinearRegression', 'XGBRegressor'
            ],
            [
                ('LinearRegression', [0, 0, 0, 1]),
                ('RandomForest', [0, 0, 1, 0]),
                ('SVR', [0, 1, 0, 0]),
                ('LinearRegression', [0, 0, 0, 1]),
                ('XGBRegressor', [1, 0, 0, 0]),
            ]
        ),
        (
            ['dog', 'cat', 'cat', 'dog', 'cow', 'fox', 'cow'],
            [
                ('dog', [0, 0, 0, 1]),
                ('cat', [0, 0, 1, 0]),
                ('cat', [0, 0, 1, 0]),
                ('dog', [0, 0, 0, 1]),
                ('cow', [0, 1, 0, 0]),
                ('fox', [1, 0, 0, 0]),
                ('cow', [0, 1, 0, 0]),
            ]
        ),
        (
            ['Moscow', 'New York', 'Moscow', 'London'],
            [
                ('Moscow', [0, 0, 1]),
                ('New York', [0, 1, 0]),
                ('Moscow', [0, 0, 1]),
                ('London', [1, 0, 0]),
            ]
        )
    ],
)
def test_fit_transform(input_list, output):
    assert fit_transform(input_list) == output


def test_fit_transform_raise():
    with pytest.raises(TypeError):
        fit_transform()

