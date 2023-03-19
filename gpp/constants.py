import pytz

KST = pytz.timezone('Asia/Seoul')

# from wiki (https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD_%ED%91%9C%EC%A4%80%EC%8B%9C)
# 1908.04.01 ~ 1911년 말  : UTC+08:30
# 1912.01.01(일제강점기)  : UTC+09:00
# 1954.03.21 ~ 1961.08.09 : UTC+08:30 (대한민국)
# 2015.08.15 ~ 2018.05.04 : UTC+08:30 (북한)
# 그 이후 UTC+09:00
# 따라서, 마지막 값으로..
if hasattr(KST, '_transition_info') and isinstance(KST._transition_info, list) and len(KST._transition_info) > 0:
    key = KST._transition_info[-1]  # key: (timestamp, old_offset, new_offset)
    KST = KST._tzinfos[key]
