import math

V_2PI = 2 * math.pi  # 2 pi
V_4PI = 4 * math.pi  # 4 pi
V_PI_2 = math.pi / 2.0  # pi/2
V_PI_4 = math.pi / 4.0  # pi/4

DEG_TO_RAD = math.pi / 180.0  # degree to radian
RAD_TO_DEG = 180.0 / math.pi  # radian to degree


class Coordinate:
    """
        지리좌표계 / 단위: degree

        :ivar lng: 경도 (-180 <= 경도 <= 180)
        :type lng: float
        :ivar lat: 위도 (-90 <= 위도 <= 90)
        :type lat: float
    """

    lng: float
    lat: float

    def __init__(self, lng: float, lat: float):
        self.lng = lng
        self.lat = lat


class ProjXY(object):
    """
        메르카토르 도법에 의해 투영(projection)된 및 0 ~ 1로 scale된 xy 평면 좌표

        ::

          (0,0)
            +--------------------------+
            |                          |
            |                          |
            |                          |
            |                          |
            +--------------------------+ (1,1)

        :ivar x: 0 <= x <= 1
        :ivar y: 0 <= y <= 1
    """
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Tile(object):
    """
        Point 객체를 zoom level에 따라 tile index로 표현

        ::

            example for zoom level = 1

            +------------+-------------+
            |(0,0)       |(1,0)        |
            |            |             |
            +------------+-------------+
            |(0,1)       |(1,1)        |
            |            |             |
            +------------+-------------+

        :ivar x: 0 <= x index < 2^z
        :ivar y: 0 <= y index < 2^z
        :ivar z: zoom level
    """
    x: int
    y: int
    z: int

    def __init__(self, x_index: int, y_index: int, zoom_level: int):
        self.x = x_index
        self.y = y_index
        self.z = zoom_level


def coord2point(coord: Coordinate) -> ProjXY:
    """
    위경도 좌표 범위를 Point로 변환

    :param coord: 위경도
    :type coord: Coordinate
    :return: Point instance
    :rtype: ProjXY
    """
    x = coord.lng / 360.0 + 0.5

    if coord.lat >= 85.051128:
        y = 0
    elif coord.lat <= -85.051128:
        y = 1
    else:
        y = math.sin(coord.lat * DEG_TO_RAD)
        y = 0.5 - math.log((1 + y) / (1 - y)) / V_4PI

    return ProjXY(x=x, y=y)


def point2coord(point: ProjXY) -> Coordinate:
    """
    Point를 위경도 좌표 범위로 변환

    :param point: projected & converted coordinate
    :type point: ProjXY
    :return: Coordinate Instance
    :rtype: Coordinate
    """

    lng = 360.0 * (point.x - 0.5)

    lat = 2 * math.atan(math.exp((0.5 - point.y) * V_2PI)) - V_PI_2
    lat = lat * RAD_TO_DEG

    return Coordinate(lng=lng, lat=lat)


def tile2point(tile: Tile) -> ProjXY:
    """
    Tile을 Point로 변환

    :param tile: Tile instance
    :type tile: Tile
    :return: Point Instance
    :rtype: ProjXY
    """
    zp = 2 ** tile.z

    x = tile.x / zp
    y = tile.y / zp

    return ProjXY(x=x, y=y)


def point2tile(point: ProjXY, zoom_level: int) -> Tile:
    """
    Point를 Tile로 변환

    :param point: Point instance
    :type point: ProjXY
    :param zoom_level: zoom level
    :type zoom_level: int
    :return: Tile Instance
    :rtype: Tile
    """
    zp = 2 ** zoom_level

    x = int(point.x * zp)
    y = int(point.y * zp)

    return Tile(x_index=x, y_index=y, zoom_level=zoom_level)


def distance(p1: Coordinate, p2: Coordinate) -> float:
    """
    하버 사인 (haversine) 공식을 이용하여 두 점 사이의 곡선에 따른 표면 거리(단위: m)를 구합니다.

    :param p1: p1
    :type p1: Coordinate
    :param p2: p2
    :type p2: Coordinate
    :return: distance in meter
    :rtype: float
    """
    r = 6371008.8  # earth radius (m)

    lat1 = p1.lat * RAD_TO_DEG
    lng1 = p1.lng * RAD_TO_DEG
    lat2 = p2.lat * RAD_TO_DEG
    lng2 = p2.lng * RAD_TO_DEG

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = math.sin(lat * 0.5) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(lng * 0.5) ** 2

    return 2 * r * math.asin(math.sqrt(d))
