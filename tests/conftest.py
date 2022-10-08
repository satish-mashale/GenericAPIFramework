import json
import pytest
from config import TEST_DATA_PATH

@pytest.fixture
def test_data(scope='session') -> object:
    filepath = f"{TEST_DATA_PATH}{'/publisheronboarding_data.json'}"
    with open(filepath) as testdata:
        data = json.load(testdata)
        yield data



