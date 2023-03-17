from datetime import date
import pytest
from gpp.texts import remove_spaces, extract_hangul, convert_words, convert_date


@pytest.mark.parametrize(
    'in_data, default, expected', [
        ('a', None, 'a'),
        (' ', None, ''),
        (' a ', None, 'a'),
        ('\t\t\t\t\t\t\t\t\t\t\b a ', None, 'a'),
        ('\n\r\t\b \u200b가\n\r\t\b \u200b나\n\r\t\b \u200b다\n\r\t\b \u200b라\n\r\t\b \u200b', None, '가나다라'),
        (-1, None, '-1'),
        (1, None, '1'),
    ]
)
def test_remove_spaces(in_data, expected, default):
    ret = remove_spaces(text=in_data, default=default)

    assert ret == expected


@pytest.mark.parametrize(
    'address, expected', [
        ('우 : 13911 경기도 안양시 만안구 예술공원로 164-1 (안양동)', '우경기도안양시만안구예술공원로안양동'),
        ('	우 : 33 rue du Puits Romain, Boite 6, L-8070 Bertrange, Luxembourg', '우'),
        ('가abc나', '가나')
    ]
)
def test_extract_hangul(address, expected):

    ret = extract_hangul(address)

    assert ret == expected


@pytest.mark.parametrize(
    'address, expected', [
        ('1      가나     다', '1 가나 다'),
        ('1 가나 다', '1 가나 다'),
        (123, '123'),
        (-123, '-123'),
    ]
)
def test_convert_text(address, expected):

    ret = convert_words(address)

    assert ret == expected


@pytest.mark.parametrize(
    'in_data, default, expected', [
        ('', None, None),
        (' - - ', None, None),
        ('1-1-1', None, None),
        ('2000-01-01', None, date(2000, 1, 1)),
        ('2000-1-1', None, date(2000, 1, 1)),
        ('2000.01.01', None, date(2000, 1, 1)),
        ('20000101', None, date(2000, 1, 1)),
        ('20009999', None, None),
        ('2018\xa0 - \xa003\xa0 - \xa029', None, date(2018, 3, 29)),
    ]
)
def test_convert_date(in_data, default, expected):
    ret = convert_date(text=in_data, default=default)

    assert ret == expected
