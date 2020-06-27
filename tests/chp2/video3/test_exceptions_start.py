from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():  # TO DO
    # with pytest.raises(Exception) as exp:
    with pytest.raises(ValueError) as exp:
        Point("Buenos Aires", 17.1234, -555.01234)
    assert str(exp.value) == 'Invalid latitude or longitude combination'
    # in case if you need to debug
    # breakpoint()
    # commands for debugging
    # {k: v for k,v in locals().items() if '__' not in k and 'pdb' not in k}
    # dir(exp)
    # for getting the object
    # exp.value
    # for getting the string representation of the oject
    # str(exp.value)
    #     raise(Exception)
    # pass
