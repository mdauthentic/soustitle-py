import pytest
from soustitle import Subtitle


@pytest.fixture
def srt():
    return Subtitle()


@pytest.fixture
def sample_data():
    return """1
            00:00:12,815 --> 00:00:14,509
            Lorem ipsum dolor sit amet
            consectetur adipiscing elit."""



