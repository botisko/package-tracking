import pytest
import datetime

from package_tracking import CeskaPosta


@pytest.mark.parametrize("package_num", ["DR2350001447U", "DR2350001420U", "DR2350001447U", "DR2350001464U"])
def test_class(package_num):
    assert CeskaPosta(package_num)


@pytest.mark.parametrize("package_num", ["asdfgw", "NP2350001", "DR2350002447U"])
def test_errors_class(package_num):
    with pytest.raises(ValueError):
        assert CeskaPosta(package_num)


@pytest.mark.parametrize("package_num, expected",
                         [("DR2350001447U", "8.11.2021"),
                          ("DR2350001420U", "10.11.2021"),
                          ("DR2350001447U", "8.11.2021"),
                          ("DR2350001464U", "8.11.2021")])
def test_datetime(package_num, expected):
    c = CeskaPosta(package_num)
    assert c.date() == expected


def test_find_package_status_none():
    with pytest.raises(AttributeError):
        CeskaPosta(None)
