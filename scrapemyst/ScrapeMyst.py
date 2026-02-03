import requests
import random
import time
from typing import List, Optional, Dict, Union, Tuple


class ScrapeMyst:
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    ]

    def __init__(self, proxies: Optional[List] = None):
        try:
            self.session = requests.Session()
            self.headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            }

            self.proxies = None
            if proxies:
                p = random.choice(proxies)
                # fixed: added https support so it doesnt leak real ip
                self.proxies = {"http": f"http://{p}", "https": f"http://{p}"}
        except Exception as e:
            print(f"init err: {e}")

    def update_headers(self, headers: Dict, replace: bool = False):
        if replace:
            self.headers = headers
        else:
            self.headers.update(headers)

    def _sleep(self, val):
        if val:
            # handles both (min, max) and fixed numbers
            t = random.uniform(val[0], val[1]) if isinstance(val, tuple) else val
            time.sleep(t)

    def send_get(
        self, url: str, params=None, sleep=None, referer=None, verbose=False
    ) -> Dict:
        try:
            self._sleep(sleep)
            self.headers["Referer"] = referer if referer else url
            self.headers["User-Agent"] = random.choice(self.user_agents)

            if verbose:
                for k, v in self.headers.items():
                    print(f"{k}: {v}")

            r = self.session.get(
                url,
                headers=self.headers,
                params=params,
                proxies=self.proxies,
                timeout=10,
            )
            r.raise_for_status()

            return {"status_code": r.status_code, "success": True, "data": r}

        except Exception as e:
            print(f"get failed: {e}")
            return {"status_code": None, "success": False, "error_message": str(e)}

    def send_post(
        self, url: str, data=None, json=None, sleep=None, referer=None, verbose=False
    ) -> Dict:
        try:
            self._sleep(sleep)
            self.headers["Referer"] = referer if referer else url
            self.headers["User-Agent"] = random.choice(self.user_agents)

            if verbose:
                for k, v in self.headers.items():
                    print(f"{k}: {v}")

            if data:
                r = self.session.post(
                    url,
                    headers=self.headers,
                    data=data,
                    proxies=self.proxies,
                    timeout=10,
                )
            elif json:
                r = self.session.post(
                    url,
                    headers=self.headers,
                    json=json,
                    proxies=self.proxies,
                    timeout=10,
                )
            else:
                raise ValueError("need data or json")

            r.raise_for_status()
            return {"status_code": r.status_code, "success": True, "data": r}

        except Exception as e:
            print(f"post failed: {e}")
            return {"status_code": None, "success": False, "error_message": str(e)}


# create object
scrapemyst = ScrapeMyst()
