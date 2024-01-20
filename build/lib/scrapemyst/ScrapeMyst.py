import requests
import random
import time


class ScrapeMyst:
    """
    A class for sending web requests with customizable headers and user-agents.

    This class provides methods for sending both GET and POST requests with customizable
    headers, user-agents, and optional proxy support. It also includes features for adding
    random sleep intervals before making requests to simulate human-like behavior.

    Attributes:
        user_agents (list): A list of user-agent strings used in requests to mimic various web browsers and clients.

    Methods:
        __init__(self, proxy=None): Initialize a ScrapeMyst instance with headers and an optional list proxies.
        send_get(self, url, params=None, sleep=None, referer=None): Send a GET request with customizable settings.
        send_post(self, url, data=None, json=None, sleep=None, referer=None): Send a POST request with customizable settings.
    """
    user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.257",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
                   "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
                   "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
                   "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"]

    def __init__(self, proxies=None):
        """
        Initialize a ScrapeMyst instance with headers and an optional proxy.

        Args:
            proxies (list, optional): A list of proxy URLs to choose from for requests.

        Raises:
            Exception: If there is an issue during initialization.

        Example:
            To create a ScrapeMyst instance with a list of proxy URLs, you can use the following code:

            ```python
            proxies = ["127.0.0.1:8000", "example.com:8080"]
            scrapemyst = ScrapeMyst(proxies=proxies)
            ```
        """
        try:
            self.session = requests.Session()

            self.headers = {
                "User-Agent": None,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Referer": None,
            }

            if proxies:
                proxy = random.choice(proxies)
                proxy = f'http://{proxy}'
                self.proxies = {
                    'http': f'{proxy}'
                }
            else:
                self.proxies = None
        except Exception as e:
            print("Something Went Wrong : {e}")

    def update_headers(self, headers, replace=False):
        """
        Update the request headers with the provided headers.

        Args:
            headers (dict): A dictionary of headers to update the request headers with.
            replace (bool, optional): If True, replace the existing headers with the provided headers.
                If False (default), update the existing headers with the provided ones.

        Raises:
            Exception: If there is an issue during the header update, such as a non-dictionary input.

        Example:
            To update the headers with custom headers, you can use the following code:

            ```python
            custom_headers = {
                "User-Agent": "MyCustomUserAgent",
                "Accept-Language": "en-US",
                "X-Custom-Header": "CustomValue"
            }
            scrapemyst.update_headers(custom_headers)
            ```

            To replace the existing headers with custom headers, you can set `replace=True`.
        """
        try:
            if replace:
                # If replace is True, set the headers to the provided headers.
                self.headers = headers
            else:
                # If replace is False (default), update the existing headers with the provided ones.
                self.headers.update(headers)
        except Exception as e:
            # Handle any exceptions and log an error message
            print(f'Error while updating headers: {e}')

    def send_get(self, url, params=None, sleep=None, referer=None):
        """
        Send a GET request with customizable settings.

        Args:
            url (str): The URL to send the GET request to.
            params (dict, optional): Query parameters to include in the request.
            sleep (bool, optional): If True, adds a random sleep interval between 2 to 5 seconds before making the request.
            referer (str, optional): The referer to set in the request headers. Defaults to the request URL if not provided.

        Returns:
            dict or None: A dictionary containing status information and the response object if the request is successful,
            or None if there's an error.

            The dictionary has the following structure:
            {
                'status_code': int,    # HTTP status code of the response
                'success': bool,        # True if the request is successful, False if there's an error
                'data': requests.Response or None  # The response object if successful, or None if there's an error
            }

        Raises:
            requests.exceptions.RequestException: If an error occurs during the GET request.
        """
        try:
            if sleep:
                # Add a random sleep interval between 2 to 5 seconds
                time.sleep(random.uniform(2, 5))

            # Set the Referer header to the specified value or the URL if not provided
            if referer:
                self.headers['Referer'] = referer
            else:
                self.headers['Referer'] = url

            # Rotate the "User-Agent" header by selecting a random user-agent string from the list.
            self.headers["User-Agent"] = random.choice(self.user_agents)

            # Send the GET request
            print(self.headers)
            response = self.session.get(
                url, headers=self.headers, params=params, proxies=self.proxies if self.proxies else None)

            # Check if the response has a successful status code
            response.raise_for_status()

            return {
                'status_code': response.status_code,
                'success': True,
                'data': response
            }

        except requests.exceptions.RequestException as e:
            # Handle any exceptions and log an error message
            print(f"Get requset failed : {e}")
            return {
                'status_code': None,
                'success': False,
                'error_message': str(e)
            }

    def send_post(self, url, data=None, json=None, sleep=None, referer=None):
        """
        Send a POST request with customizable settings.

        Args:
            url (str): The URL to send the POST request to.
            data (dict, optional): Form data to include in the request body.
            json (dict, optional): JSON data to include in the request body.
            sleep (bool, optional): If True, adds a random sleep interval between 2 to 5 seconds before making the request.
            referer (str, optional): The referer to set in the request headers. Defaults to the request URL if not provided.

        Returns:
            dict or None: A dictionary containing status information and the response object if the request is successful,
            or None if there's an error.

            The dictionary has the following structure:
            {
                'status_code': int,    # HTTP status code of the response
                'success': bool,        # True if the request is successful, False if there's an error
                'data': requests.Response or None  # The response object if successful, or None if there's an error
            }

        Raises:
            ValueError: If neither 'data' nor 'json' is provided for the POST request.
            requests.exceptions.RequestException: If an error occurs during the POST request.
        """
        try:
            if sleep:
                # Add a random sleep interval between 2 to 5 seconds
                time.sleep(random.uniform(2, 5))

            # Set the Referer header to the specified value or the URL if not provided
            if referer:
                self.headers['Referer'] = referer
            else:
                self.headers['Referer'] = url

            # Rotate the "User-Agent" header by selecting a random user-agent string from the list.
            self.headers["User-Agent"] = random.choice(self.user_agents)

            # Send the POST request with either form data or JSON data
            if data:
                response = self.session.post(
                    url, headers=self.headers, data=data, proxies=self.proxies if self.proxies else None)
            elif json:
                response = self.session.post(
                    url, headers=self.headers, json=json, proxies=self.proxies if self.proxies else None)
            else:
                raise ValueError(
                    "Either 'data' or 'json' must be provided for the POST request.")

            # Check if the response has a successful status code
            response.raise_for_status()

            return {
                'status_code': response.status_code,
                'success': True,
                'data': response
            }
        except requests.exceptions.RequestException as e:
            # Handle any exceptions and log an error message
            print(f"POST request failed: {e}")
            return {
                'status_code': None,
                'success': False,
                'error_message': str(e)
            }


# creating a object of the class
scrapemyst = ScrapeMyst()
