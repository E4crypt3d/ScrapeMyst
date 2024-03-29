# ScrapeMyst

ScrapeMyst is a Python class for sending web requests with customizable headers and user-agents. It provides methods for sending both GET and POST requests with customizable headers, user-agents, and optional proxy support. The class also includes features for adding random sleep intervals before making requests to simulate human-like behavior.

## Installation

You can install ScrapeMyst using pip:

```bash
pip install scrapemyst
```

## Usage

- Import the ScrapeMyst class

```python
from scrapemyst import ScrapeMyst
# Create an instance of ScrapeMyst, optionally providing a list of proxy URLs
scrapemyst = ScrapeMyst(proxies=["127.0.0.1:8000", "example.com:8080"])
```

##### OR

- Import the ScrapeMyst object directly if you are not providing list of proxy urls

```python
from scrapemyst import scrapemyst
```

- Example of sending a GET request
  - `send_get` and `send_post` both methods support sleep between requests sleep argument accepts `int`,`float` or `tuple` as shown in the examples.

```python
url_get = "https://www.example.com"
get_response = scrapemyst.send_get(url_get, params={"param1": "value1"}, sleep=3, referer="https://www.referer.com")

if get_response['success']:
print(f"GET Request Successful. Status Code: {get_response['status_code']}") # Access the response object if needed: get_response['data']
```

- Example of sending a POST request with form data

```python
url_post_form = "https://www.example.com/post"
form_data = {"key1": "value1", "key2": "value2"}
post_response_form = scrapemyst.send_post(url_post_form, data=form_data, sleep=4.5, referer="https://www.referer.com")

if post_response_form['success']:
print(f"POST Request (Form Data) Successful. Status Code: {post_response_form['status_code']}") # Access the response object if needed: post_response_form['data']
```

- Example of sending a POST request with JSON data

```python
url_post_json = "https://www.example.com/api"
json_data = {"key1": "value1", "key2": "value2"}
post_response_json = scrapemyst.send_post(url_post_json, json=json_data, sleep=(2,9), referer="https://www.referer.com")

if post_response_json['success']:
print(f"POST Request (JSON Data) Successful. Status Code: {post_response_json['status_code']}") # Access the response object if needed: post_response_json['data']
```

## Customization

You can customize the headers, user-agents, and other settings by updating the ScrapeMyst instance. For example:

```python
# Update headers add more headers to the request
custom_headers = {
    "User-Agent": "CustomUserAgent",
    "Accept-Language": "en-US",
    "Custom-Header": "CustomValue"
}
scrapemyst.update_headers(custom_headers)
# OR
# Replace the default headers
scrapemyst.update_headers(custom_headers, replace=True)

# Send a request with updated headers
response_custom = scrapemyst.send_get('https://example.com')
print("Custom Response:", response_custom)
```

## Contributing

If you'd like to contribute to ScrapeMyst, feel free to submit pull requests, report issues, or suggest improvements.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
