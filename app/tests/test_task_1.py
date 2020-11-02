import pytest

from ..postcodes import Stores


@pytest.fixture(scope="module")
def stores():
    import os
    os.chdir('app')
    return Stores()


def test_postcode_without_coordinates(stores):
    "Test with a postcode for which postcodes.io doesn't return results."
    # These two postcodes don't have coordinates: GU19 5DG SS1 1PA
    with pytest.raises(ValueError):
        stores.stores_within_radius(25, "GU19 5DG")


def test_with_large_radius(stores):
    "Test that a radius higher than 6371 will through a value error."
    with pytest.raises(ValueError):
        stores.stores_within_radius(8000, 'BR5 3RP')


def test_with_negative_radius(stores):
    "Test that negative radius throughs a value error."
    with pytest.raises(ValueError):
        stores.stores_within_radius(-800, 'BR5 3RP')


def test_with_nonexistent_postcode(stores):
    "Test that using a postcode that's not found in stores.json will through error"
    with pytest.raises(ValueError):
        stores.stores_within_radius(80, 'KJON')


def test_sorting_north_to_south(stores):
    "Test that lower indexes in the resultset have higher latitude."
    results = stores.stores_within_radius(30, "BR5 3RP")
    assert results[0]['latitude'] > results[5]['latitude']
