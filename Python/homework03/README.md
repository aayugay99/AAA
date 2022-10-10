## issue-01

Для запуска тестов необходимо в консоли набрать команду:

```
python -m doctest -o NORMALIZE_WHITESPACE -v '.\issues 1-2\morse.py'
```

## issue-02

Для запуска тестов необходимо в консоли набрать команду:

```
python -m pytest -v '.\issues 1-2\morse_test.py' 
```

## issue-03

Для запуска тестов необходимо в консоли набрать команды:

```
cd '.\issues 3-4\'
python -m unittest test_one_hot_encoder.py'
cd .. 
```

## issue-04

Для запуска тестов необходимо в консоли набрать команду:

```
python -m pytest -v '.\issues 3-4\pytest_ohe.py'
```

## issue-05

Для запуска тестов необходимо в консоли набрать команду:

```
python -m pytest -v '.\issue 5\test_what_is_year_now.py'
```

Для создания отчета о покрытии:

```
cd '.\issue 5'
python -m pytest --cov . --cov-report html
cd ..
```