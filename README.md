# ScrapeMyst

a lean, human-like wrapper for Python `requests`. Handles user-agent rotation, proxy setup, and random delays so you don't have to.

## Installation

```bash
pip install scrapemyst
```

## Usage

### Setup

```python
from scrapemyst import ScrapeMyst
```

### Initialize with proxies

```python
proxies = ["127.0.0.1:8000", "example.com:8080"]
scrapemyst = ScrapeMyst(proxies=proxies)
```

### Or use the default instance for quick tasks

```python
from scrapemyst import scrapemyst
```

## GET request

Supports fixed sleep (`sleep=3`) or random ranges (`sleep=(1, 5)`).

```python
res = scrapemyst.send_get(
    "https://example.com",
    params={"id": "123"},
    sleep=(2, 4),
    referer="https://google.com"
)

if res["success"]:
    print(f"status: {res['status_code']}")
    # data is the raw requests response object
    print(res["data"].text)
```

## POST request

Works with standard form data or JSON.

### POST form data

```python
scrapemyst.send_post(
    "https://example.com/login",
    data={"user": "admin"}
)
```

### POST JSON

```python
res = scrapemyst.send_post(
    "https://api.com/v1",
    json={"key": "val"},
    sleep=2
)
```

## Response structure

Every method returns a simple dictionary:

* `success`: bool — `True` if the request worked
* `status_code`: int — HTTP status code (200, 404, etc.)
* `data`: the raw response object (if successful)
* `error_message`: string (if it failed)

## Customization

### Add new headers

```python
scrapemyst.update_headers({"X-Custom": "Value"})
```

### Overwrite all headers

```python
scrapemyst.update_headers({"User-Agent": "MyBot"}, replace=True)
```

## License

MIT
