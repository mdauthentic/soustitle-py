## Soustitle-py

A simple python `srt` parser.

>Soustitle `[FrEnglish]`: `sous [FR]` meaning `sub` and `title[EN]`, a combination of the two forms `soustitle` (subtitle).

Read and parse subtitle (`.srt`) file, returns a dictionary consisting of the subtitle details (e.g start / end time and subtitle text). The result can also be converted into `csv` or `json` format for further use.

This script is ported from my `Scala` version of the library. You can check the project version [here](https://github.com/mdauthentic/sous-title).

### Usage

```python3
$ python3
>>> from soustitle import Subtitle
```

#### Reading from file

```python3
>>> srt = Subtitle('resources/sample.srt')
>>> res = srt.open()
>>> print(res)
```

Alternatively, the file path could be passed directly to the `open` method.

```python3
>>> srt = Subtitle()
>>> res = srt.open('resources/sample.srt')
>>> print(res)
```

#### Parsing string

```python3
>>> sample = """1
            00:00:12,815 --> 00:00:14,509
            Lorem ipsum dolor sit amet
            consectetur adipiscing elit.

            2
            00:00:14,815 --> 00:00:16,498
            Lorem ipsum dolor sit amet.

            3
            00:00:16,934 --> 00:00:17,814
            Lorem ipsum dolor sit amet."""

>>> parse_srt = Subtitle(srt_string=sample)
>>> result = parse_srt.parse()
>>> print(result)
```

#### Result of Parsed String

```json
[
    {
        "start_time": "00:00:12:815", 
        "end_time": "00:00:14:509", 
        "subtitle_text": "Lorem ipsum dolor sit amet consectetur adipiscing elit."
    }, {
        "start_time": "00:00:14:815", 
        "end_time": "00:00:16:498", 
        "subtitle_text": "Lorem ipsum dolor sit amet."
    }, {
        "start_time": "00:00:16:934", 
        "end_time": "00:00:17:814", 
        "subtitle_text": "Lorem ipsum dolor sit amet."
    }
]
```

#### Convert parsed result

- Convert to `.csv` format

```python3
>>> csv_out = parse_srt.to_csv(result, 'resources/output.csv')
>>> print(csv_out)
```

- Convert to `.json` format

```python3
>>> csv_out = parse_srt.to_json(result, 'resources/output.json')
>>> print(csv_out)
```

### Dev

```bash
git clone https://github.com/mdauthentic/soustitle-py.git
cd soustitle-py
python3 -m venv my-env
source my-env/bin/activate  
pip install -r requirements.txt
```

### Testing

Run

```bash
pytest tests.py
```

Optionally, you can run the test with docker

```bash
docker build -t image-name .
docker run image-name
```