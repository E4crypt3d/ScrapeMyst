# ScrapeMyst

ScrapeMyst is a Python class for sending web requests with customizable headers and user-agents. It provides methods for sending both GET and POST requests with customizable headers, user-agents, and optional proxy support. The class also includes features for adding random sleep intervals before making requests to simulate human-like behavior.

## Installation

You can install ScrapeMyst using pip:

```bash
pip install scrapemyst
```

## Usage

```python
from scrapemyst import ScrapeMyst

# Create an instance of ScrapeMyst
scrapemyst = ScrapeMyst()

# Send a GET request
response_get = scrapemyst.send_get('https://example.com')

# Send a POST request with form data
response_post = scrapemyst.send_post('https://example.com', data={'key': 'value'})

# Print the responses
print("GET Response:", response_get)
print("POST Response:", response_post)
```

## Customization

You can customize the headers, user-agents, and other settings by updating the ScrapeMyst instance. For example:

```python
# Update headers
custom_headers = {
    "User-Agent": "CustomUserAgent",
    "Accept-Language": "en-US",
    "Custom-Header": "CustomValue"
}
scrapemyst.update_headers(custom_headers)

# Send a request with updated headers
response_custom = scrapemyst.send_get('https://example.com')
print("Custom Response:", response_custom)
```

## Contributing

If you'd like to contribute to ScrapeMyst, feel free to submit pull requests, report issues, or suggest improvements.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.
