"""Integration tests."""
import os

import pytest
from testfixtures import LogCapture
from victor_smart_kill import Trap, VictorApi, VictorAsyncClient


@pytest.fixture
def secret_victor_username():
    """Get Victor API username."""
    return os.environ.get("SECRET_VICTOR_USERNAME")


@pytest.fixture
def secret_victor_password():
    """Get Victor API password."""
    return os.environ.get("SECRET_VICTOR_PASSWORD")


@pytest.fixture
async def victor_api_client(secret_victor_username, secret_victor_password):
    """Get Victor API async client instance for use in integration tests."""
    async with VictorAsyncClient(
        secret_victor_username, secret_victor_password, verify=False
    ) as client:
        yield client


@pytest.fixture
async def victor_api(secret_victor_username, secret_victor_password):
    """Get Victor API client instance for use in integration tests."""
    async with VictorAsyncClient(
        secret_victor_username, secret_victor_password, verify=False
    ) as client:
        api = VictorApi(client)
        yield api


@pytest.mark.asyncio
async def test_fetch_token(victor_api_client: VictorAsyncClient, capture: LogCapture):
    await victor_api_client.fetch_token()


@pytest.mark.asyncio
async def test_traps(victor_api: VictorApi):
    traps = await victor_api.get_traps()
    assert traps is not None
    for trap in traps:
        assert isinstance(trap, Trap)
