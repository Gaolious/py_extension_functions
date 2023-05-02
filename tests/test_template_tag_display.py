import pytest

from gpp.templatetags.display_tags import replace_query_param, money_1k, get_item, percentage, precision2


@pytest.mark.parametrize('url', ['https://domain.com/?p1=1&p2=2&p3=3'])
@pytest.mark.parametrize('attr, val, expected', [
    ('p1', '3', 'https://domain.com/?p1=3&p2=2&p3=3')
])
def test_replace_query_param(url, attr, val, expected):
    assert replace_query_param(url, attr, val) == expected


@pytest.mark.parametrize('val, expected', [
    (0, '0'),
    (1, '0'),
    (999, '0'),
    (1000, '1'),
    ('1', '1'),
])
def test_money_1k(val, expected):
    assert money_1k(val) == expected


@pytest.mark.parametrize('key, expected', [
    ('a', 1),
    ('b', None)
])
def test_get_item(key, expected):
    data = {'a': 1}
    assert get_item(data, key) == expected


@pytest.mark.parametrize('val, expected', [
    (0, '0.00%'),
    (-1, '-1.00%'),
    (1, '1.00%'),
    (1.111111, '1.11%'),
])
def test_percentage(val, expected):
    assert percentage(val) == expected


@pytest.mark.parametrize('val, expected', [
    (0, '0.00'),
    (-1, '-1.00'),
    (1, '1.00'),
    (1.111111, '1.11'),
    ('a', 'a'),
    (None, None)
])
def test_precision2(val, expected):
    assert precision2(val) == expected
