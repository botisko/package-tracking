import pytest

from package_tracking import print_package_status, find_package_status


@pytest.mark.parametrize('status', [["DR1234567890E", "1.1.1970", "Nope"], ["EE123456789CZ", "23.11.1969", "Yep"]])
def test_print_package_status_pass(status):
    print_package_status(status)


@pytest.mark.parametrize('status', [None, "Le String", 25])
def test_print_package_status_raise_type_err(status):
    with pytest.raises(TypeError):
        print_package_status(status)


@pytest.mark.parametrize('status', [[], ["Uno"], ["Foo", "Bar"]])
def test_print_package_status_raise_index_err(status):
    with pytest.raises(IndexError):
        print_package_status(status)


def test_find_package_status_none():
    with pytest.raises(AttributeError):
        find_package_status(None)
