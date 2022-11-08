import pytest

from scripts import data_processor


def test_2csv_reader_header_fields(process_data):
    """
    Happy Path test to make sure the processed data
    contains the right header fields
    """
    # helper function imported from conftest.py to import file data with our csv reader
    data = process_data
    header_fields = list(data[0].keys())
    print('test4')
    assert header_fields == [
            'Country',
            'City',
            'State_Or_Province',
            'Lat',
            'Long',
            'Altitude'
            ]


def test_1csv_reader_data_contents(process_data):
    """
    Happy Path Test to examine that each row
    has the appropriate data type per field
    """
    print('test3')
    data = process_data
    print(len(data))
    for row in data:
        assert(isinstance(row['Country'], str))
        assert(isinstance(row['City'], str))
        assert(isinstance(row['State_Or_Province'], str))
        assert(isinstance(row['Lat'], float))
        assert(isinstance(row['Long'], float))
        assert(isinstance(row['Altitude'], float))
    assert len(data) == 180


@pytest.fixture(scope="module")
def city_list_location():
    print('test1')
    return 'tests/resources/cities/clean_map.csv'


@pytest.fixture(scope="module")
def process_data(city_list_location):
    print('test2')
    yield data_processor.csv_reader(city_list_location)
