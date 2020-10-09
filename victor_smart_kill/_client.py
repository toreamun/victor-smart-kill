"""Victor Smart Kill API module."""
import logging

from httpx import URL, AsyncClient, Response, codes

log = logging.getLogger(__name__)

DEFAULT_BASE_URL = URL("https://www.victorsmartkill.com")


class VictorAsyncClient(AsyncClient):
    """An asynchronous HTTP client to Victor Smart Kill API."""

    def __init__(self, username: str, password: str, **kwargs) -> None:
        """
        Initialize VictorAsyncClient.

        :param username: User name used to access Victor API.
        :param username: Password used to access Victor API.
        :param kwargs: Arguments to pass to the httpx.AsyncClient constructor.
        """
        super().__init__(**kwargs)

        if not username:
            raise ValueError("User name is required.")

        if not password:
            raise ValueError("Password is required.")

        if self.base_url == URL():
            self.base_url = DEFAULT_BASE_URL

        self._credentials = {"password": password, "username": username}
        self._token = None

    @property
    def has_token(self) -> bool:
        """Boolean that indicates whether this session has an token or not."""
        return self._token is not None

    async def fetch_token(self) -> None:
        """Fetch token and store in client."""
        self._token = None

        response = await super().request(
            "POST",
            "api-token-auth/",
            json=self._credentials,
        )

        response.raise_for_status()

        token = response.json().get("token")
        if token:
            self._token = token
            log.info("Fetched token.")
        else:
            raise Exception("Unexpected response from token endpoind")

    async def request(
        self,
        *args,
        **kwargs,
    ) -> Response:
        """Intercept all requests and add token. Fetches token if needed."""
        return await self._request(True, *args, **kwargs)

    # pylint: disable=R0913
    async def _request(
        self, retry_unauthorized, method, url, data=None, headers=None, **kwargs
    ) -> Response:
        if not self.has_token:
            log.info("Token is missing. Fetch token.")
            await self.fetch_token()

        if not headers:
            request_headers = dict()
        else:
            request_headers = headers.copy()

        request_headers["Authorization"] = f"Token {self._token}"

        log.debug("Adding token %s to request.", self._token)
        log.debug("Requesting url %s using method %s.", url, method)
        log.debug("Supplying headers %s and data %s", request_headers, data)
        log.debug("Passing through key word arguments %s.", kwargs)

        response = await super().request(
            method, url, headers=request_headers, data=data, **kwargs
        )

        if retry_unauthorized and response.status_code == codes.UNAUTHORIZED:
            log.info("Unauthorized response code. Fetch token and retry.")
            await self.fetch_token()
            response = await self._request(
                False, method, url, data=data, headers=headers, **kwargs
            )

        return response
