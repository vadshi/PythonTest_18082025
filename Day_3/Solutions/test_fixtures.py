import pytest


@pytest.fixture(scope='module')
def return_tuple():
    """ Return tuple as result. """
    print("\nStart to return data\n")
    yield ((1, "hello"), (2, "python"))
    print("\nWell done.\n")


@pytest.fixture()
def return_dict(return_tuple):
    """ Return dict as result. """
    return dict(return_tuple)

 
@pytest.fixture()
def return_list(return_tuple):
    """ Return list as result. """
    return list(return_tuple)


def test_get_tuple(return_tuple):
    assert type(return_tuple) is tuple
    assert len(return_tuple) == 2


def test_get_list(return_list):
    assert type(return_list) is list
    assert len(return_list) == 2


def test_get_dict(return_dict):
    assert type(return_dict) is dict
    assert len(return_dict) == 2