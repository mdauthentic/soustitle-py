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


@pytest.mark.parametrize(
    "test_data, expected",
    [
        ("00:00:12,815", "00:00:12:815"),
        ("00:00:14,509", "00:00:14:509"),
        ("00:00:16,934", "00:00:16:934"),
    ],
)
def test_format_time_delta(srt, test_data, expected):
    assert srt.format_time_delta(test_data) == expected


def test_parse(sample_data):
    return_data = [
        {
            "start_time": "00:00:12:815",
            "end_time": "00:00:14:509",
            "subtitle_text": "Lorem ipsum dolor sit amet consectetur adipiscing elit.",
        }
    ]
    assert Subtitle(srt_string=sample_data).parse() == return_data


def test_file_size_conv(srt):
    assert srt.size_in_bytes(2000) == "2.0 KB"
