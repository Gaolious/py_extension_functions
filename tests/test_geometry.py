import pytest

from gpp.geometry import Tile, tile_to_proj_coord, ProjectedCoordinate, proj_coord_to_tile, proj_coord_to_coord, \
    Coordinate, coord_to_proj_coord, distance


@pytest.mark.parametrize(
    'zoom_level, xidx, yidx, expected_x, expected_y', [
        (0, 0, 0, 0, 0),
        (1, 1, 1, 0.5, 0.5),
        (2, 2, 2, 0.5, 0.5),
        (3, 4, 4, 0.5, 0.5),
        (21, 1234567, 1234567, 0.5886874198913574, 0.5886874198913574),
    ]
)
def test_tile_and_proj_coord(zoom_level, xidx, yidx, expected_x, expected_y):
    ##########################################################
    # precondition
    tile = Tile(x_index=xidx, y_index=yidx, zoom_level=zoom_level)
    reverse_p = ProjectedCoordinate(x=expected_x, y=expected_y)

    ##########################################################
    # call function
    p = tile_to_proj_coord(tile)

    ##########################################################
    # assertion
    assert abs(p.x - expected_x) < 10 ** -9
    assert abs(p.y - expected_y) < 10 ** -9

    ##########################################################
    # call function
    coord = proj_coord_to_coord(proj_coord=p)

    ##########################################################
    # assertion
    assert -180 <= coord.lng <= 180
    assert -90 <= coord.lat <= 90

    ##########################################################
    # call function
    tile = proj_coord_to_tile(proj_coord=reverse_p, zoom_level=zoom_level)

    ##########################################################
    # assertion
    assert tile.x == xidx
    assert tile.y == yidx


@pytest.mark.parametrize(
    'lng, lat, x, y', [
        (127.0, -85, 0.8527777777777779, 0.9983620852139461),
        (127.0, -80, 0.8527777777777779, 0.8877406020370049),
        (127.0, -75, 0.8527777777777779, 0.8227008790403291),
        (127.0, -70, 0.8527777777777779, 0.7761999014553801),
        (127.0, -65, 0.8527777777777779, 0.7397596384131102),
        (127.0, -60, 0.8527777777777779, 0.7096003591394914),
        (127.0, -55, 0.8527777777777779, 0.6837021346943182),
        (127.0, -50, 0.8527777777777779, 0.6608552253787816),
        (127.0, -45, 0.8527777777777779, 0.640274963084795),
        (127.0, -40, 0.8527777777777779, 0.6214208422589191),
        (127.0, -35, 0.8527777777777779, 0.603902168693612),
        (127.0, -30, 0.8527777777777779, 0.587424788141515),
        (127.0, -25, 0.8527777777777779, 0.5717590374800048),
        (127.0, -20, 0.8527777777777779, 0.5567194006385946),
        (127.0, -15, 0.8527777777777779, 0.5421509528707389),
        (127.0, -10, 0.8527777777777779, 0.5279198879350837),
        (127.0, -5, 0.8527777777777779, 0.5139065508480531),
        (127.0, 0, 0.8527777777777779, 0.5),
        (127.0, 5, 0.8527777777777779, 0.4860934491519468),
        (127.0, 10, 0.8527777777777779, 0.47208011206491635),
        (127.0, 15, 0.8527777777777779, 0.4578490471292611),
        (127.0, 20, 0.8527777777777779, 0.4432805993614054),
        (127.0, 25, 0.8527777777777779, 0.4282409625199952),
        (127.0, 30, 0.8527777777777779, 0.41257521185848506),
        (127.0, 35, 0.8527777777777779, 0.396097831306388),
        (127.0, 40, 0.8527777777777779, 0.3785791577410809),
        (127.0, 45, 0.8527777777777779, 0.35972503691520497),
        (127.0, 50, 0.8527777777777779, 0.33914477462121845),
        (127.0, 55, 0.8527777777777779, 0.3162978653056818),
        (127.0, 60, 0.8527777777777779, 0.2903996408605086),
        (127.0, 65, 0.8527777777777779, 0.26024036158688973),
        (127.0, 70, 0.8527777777777779, 0.2238000985446199),
        (127.0, 75, 0.8527777777777779, 0.17729912095967099),
        (127.0, 80, 0.8527777777777779, 0.11225939796299511),
        (127.0, 85, 0.8527777777777779, 0.0016379147860539622),
        (-180, 37.5, 0.0, 0.38748522730623625),
        (-175, 37.5, 0.013888888888888895, 0.38748522730623625),
        (-170, 37.5, 0.02777777777777779, 0.38748522730623625),
        (-165, 37.5, 0.041666666666666685, 0.38748522730623625),
        (-160, 37.5, 0.05555555555555558, 0.38748522730623625),
        (-155, 37.5, 0.06944444444444442, 0.38748522730623625),
        (-150, 37.5, 0.08333333333333331, 0.38748522730623625),
        (-145, 37.5, 0.09722222222222221, 0.38748522730623625),
        (-140, 37.5, 0.1111111111111111, 0.38748522730623625),
        (-135, 37.5, 0.125, 0.38748522730623625),
        (-130, 37.5, 0.1388888888888889, 0.38748522730623625),
        (-125, 37.5, 0.1527777777777778, 0.38748522730623625),
        (-120, 37.5, 0.16666666666666669, 0.38748522730623625),
        (-115, 37.5, 0.18055555555555558, 0.38748522730623625),
        (-110, 37.5, 0.19444444444444442, 0.38748522730623625),
        (-105, 37.5, 0.20833333333333331, 0.38748522730623625),
        (-100, 37.5, 0.2222222222222222, 0.38748522730623625),
        (-95, 37.5, 0.2361111111111111, 0.38748522730623625),
        (-90, 37.5, 0.25, 0.38748522730623625),
        (-85, 37.5, 0.2638888888888889, 0.38748522730623625),
        (-80, 37.5, 0.2777777777777778, 0.38748522730623625),
        (-75, 37.5, 0.29166666666666663, 0.38748522730623625),
        (-70, 37.5, 0.3055555555555556, 0.38748522730623625),
        (-65, 37.5, 0.3194444444444444, 0.38748522730623625),
        (-60, 37.5, 0.33333333333333337, 0.38748522730623625),
        (-55, 37.5, 0.3472222222222222, 0.38748522730623625),
        (-50, 37.5, 0.3611111111111111, 0.38748522730623625),
        (-45, 37.5, 0.375, 0.38748522730623625),
        (-40, 37.5, 0.3888888888888889, 0.38748522730623625),
        (-35, 37.5, 0.4027777777777778, 0.38748522730623625),
        (-30, 37.5, 0.4166666666666667, 0.38748522730623625),
        (-25, 37.5, 0.4305555555555556, 0.38748522730623625),
        (-20, 37.5, 0.4444444444444444, 0.38748522730623625),
        (-15, 37.5, 0.4583333333333333, 0.38748522730623625),
        (-10, 37.5, 0.4722222222222222, 0.38748522730623625),
        (-5, 37.5, 0.4861111111111111, 0.38748522730623625),
        (0, 37.5, 0.5, 0.38748522730623625),
        (5, 37.5, 0.5138888888888888, 0.38748522730623625),
        (10, 37.5, 0.5277777777777778, 0.38748522730623625),
        (15, 37.5, 0.5416666666666666, 0.38748522730623625),
        (20, 37.5, 0.5555555555555556, 0.38748522730623625),
        (25, 37.5, 0.5694444444444444, 0.38748522730623625),
        (30, 37.5, 0.5833333333333334, 0.38748522730623625),
        (35, 37.5, 0.5972222222222222, 0.38748522730623625),
        (40, 37.5, 0.6111111111111112, 0.38748522730623625),
        (45, 37.5, 0.625, 0.38748522730623625),
        (50, 37.5, 0.6388888888888888, 0.38748522730623625),
        (55, 37.5, 0.6527777777777778, 0.38748522730623625),
        (60, 37.5, 0.6666666666666666, 0.38748522730623625),
        (65, 37.5, 0.6805555555555556, 0.38748522730623625),
        (70, 37.5, 0.6944444444444444, 0.38748522730623625),
        (75, 37.5, 0.7083333333333334, 0.38748522730623625),
        (80, 37.5, 0.7222222222222222, 0.38748522730623625),
        (85, 37.5, 0.7361111111111112, 0.38748522730623625),
        (90, 37.5, 0.75, 0.38748522730623625),
        (95, 37.5, 0.7638888888888888, 0.38748522730623625),
        (100, 37.5, 0.7777777777777778, 0.38748522730623625),
        (105, 37.5, 0.7916666666666667, 0.38748522730623625),
        (110, 37.5, 0.8055555555555556, 0.38748522730623625),
        (115, 37.5, 0.8194444444444444, 0.38748522730623625),
        (120, 37.5, 0.8333333333333333, 0.38748522730623625),
        (125, 37.5, 0.8472222222222222, 0.38748522730623625),
        (130, 37.5, 0.8611111111111112, 0.38748522730623625),
        (135, 37.5, 0.875, 0.38748522730623625),
        (140, 37.5, 0.8888888888888888, 0.38748522730623625),
        (145, 37.5, 0.9027777777777778, 0.38748522730623625),
        (150, 37.5, 0.9166666666666667, 0.38748522730623625),
        (155, 37.5, 0.9305555555555556, 0.38748522730623625),
        (160, 37.5, 0.9444444444444444, 0.38748522730623625),
        (165, 37.5, 0.9583333333333333, 0.38748522730623625),
        (170, 37.5, 0.9722222222222222, 0.38748522730623625),
        (175, 37.5, 0.9861111111111112, 0.38748522730623625),
        (180, 37.5, 1.0, 0.38748522730623625),
    ]
)
def test_proj_coord_and_coord(lng, lat, x, y):
    ##########################################################
    # precondition
    c = Coordinate(lng=lng, lat=lat)

    ##########################################################
    # call function
    p = coord_to_proj_coord(coord=c)

    ##########################################################
    # assertion
    assert abs(p.x - x) < 10 ** -9
    assert abs(p.y - y) < 10 ** -9

    ##########################################################
    # call function
    c = proj_coord_to_coord(proj_coord=p)

    ##########################################################
    # assertion
    assert abs(c.lng - lng) < 10 ** -9
    assert abs(c.lat - lat) < 10 ** -9


@pytest.mark.parametrize(
    'lng, lat, x, y', [
        (127.0, i/10.0, 0.8527777777777779, 1) for i in range(-900, -850, 5)
    ]
)
def test_proj_coord_and_coord_except_latitude_1(lng, lat, x, y):
    """
        위도가 범위 벗어나는 경우 1.
    """
    ##########################################################
    # precondition
    c = Coordinate(lng=lng, lat=lat)

    ##########################################################
    # call function
    p = coord_to_proj_coord(coord=c)

    ##########################################################
    # assertion
    assert abs(p.x - x) < 10 ** -9
    assert abs(p.y - y) < 10 ** -9

    ##########################################################
    # call function
    c = proj_coord_to_coord(proj_coord=p)

    ##########################################################
    # assertion
    assert abs(c.lng - lng) < 10 ** -9
    assert abs(c.lat + 85.05112877980659) < 10 ** -9


@pytest.mark.parametrize(
    'lng, lat, x, y', [
        (127.0, i/10.0, 0.8527777777777779, 0) for i in range(900, 850, -5)
    ]
)
def test_proj_coord_and_coord_except_latitude_2(lng, lat, x, y):
    """
        위도가 범위 벗어나는 경우 2.
    """
    ##########################################################
    # precondition
    c = Coordinate(lng=lng, lat=lat)

    ##########################################################
    # call function
    p = coord_to_proj_coord(coord=c)

    ##########################################################
    # assertion
    assert abs(p.x - x) < 10 ** -9
    assert abs(p.y - y) < 10 ** -9

    ##########################################################
    # call function
    c = proj_coord_to_coord(proj_coord=p)

    ##########################################################
    # assertion
    assert abs(c.lng - lng) < 10 ** -9
    assert abs(c.lat - 85.05112877980659) < 10 ** -9


@pytest.mark.parametrize(
    'lng1, lat1', [(127.0, 36.0), ]
)
@pytest.mark.parametrize(
    'lng2, lat2, expected', [
        (127.0, 36.0, 0.0),
        (127.001, 36.001, 143.0273144594902),
        (127.002, 36.002, 286.053911427857),
        (127.003, 36.003, 429.0797908796973),
        (127.004, 36.004, 572.1049527970165),
        (127.005, 36.005, 715.1293971566106),
        (127.006, 36.006, 858.1531239377349),
        (127.007, 36.007, 1001.176133118624),
        (127.008, 36.008, 1144.1984246769637),
        (127.009, 36.009, 1287.219998593108),
    ]
)
def test_distance(lng1, lat1, lng2, lat2, expected):
    ##########################################################
    # precondition
    c1 = Coordinate(lng=lng1, lat=lat1)
    c2 = Coordinate(lng=lng2, lat=lat2)

    ##########################################################
    # call function
    dist = distance(c1, c2)

    ##########################################################
    # assertion
    assert abs(dist - expected) < 10 ** -9