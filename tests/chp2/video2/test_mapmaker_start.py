from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("Dakar", 14, 17)
    assert p1.get_lat_long() == (14, 17)
