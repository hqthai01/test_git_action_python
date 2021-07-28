import pytest

@pytest.mark.parametrize('test_input, expected', [
    ('1+1', 2),
    ('2*2', 4),
    pytest.param('3+3',5, marks = pytest.mark.xfail)
    ])
def test_calculation(test_input, expected):
    assert eval(test_input) == expected