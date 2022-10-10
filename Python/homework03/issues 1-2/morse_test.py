from morse import decode
import pytest

@pytest.mark.parametrize(
    "source_string, result",
    [
        ('... --- ...', 'SOS'),
        ('.-.. --- ...- .', 'LOVE'),
        ('.--. -.-- - .... --- -.', 'PYTHON'),
    ],
)
def test_decode(source_string, result):
    assert decode(source_string) == result
