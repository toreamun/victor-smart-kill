"""Integration tests."""
import os

import pytest
from victor_smart_kill import (
    MobileApp,
    Operator,
    Profile,
    Trap,
    User,
    VictorApi,
    VictorAsyncClient,
)


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
        secret_victor_username, secret_victor_password, verify=False, timeout=60.0
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
async def test_fetch_token(victor_api_client: VictorAsyncClient):
    """Test fetch_token."""
    await victor_api_client.fetch_token()


# @pytest.mark.asyncio
# async def test_activity_log(victor_api: VictorApi):
#     """Test get_activity_logs."""
#     logs = await victor_api.get_activity_logs()
#     assert logs is not None
#     for log_item in logs:
#         assert isinstance(log_item, Activity)

#         log_item_by_id = await victor_api.get_activity_log_record(log_item.id)
#         assert isinstance(log_item_by_id, Activity)
#         assert log_item.id == log_item_by_id.id
#         assert log_item.url == log_item_by_id.url


@pytest.mark.asyncio
async def test_mobile_apps(victor_api: VictorApi):
    """Test mobile_apps."""
    apps = await victor_api.get_mobile_apps()
    assert apps is not None
    for app in apps:
        assert isinstance(app, MobileApp)

        app_by_url = await victor_api.get_mobile_app_by_url(app.url)
        assert isinstance(app_by_url, MobileApp)
        assert app.url == app_by_url.url

    app_1 = await victor_api.get_mobile_app_by_id(1)
    assert isinstance(app_1, MobileApp)


@pytest.mark.asyncio
async def test_get_operators(victor_api: VictorApi):
    """Test get_operators."""
    operators = await victor_api.get_operators()
    assert operators is not None
    for operator in operators:
        assert isinstance(operator, Operator)

        operator_by_id = await victor_api.get_operator_by_id(operator.id)
        assert isinstance(operator_by_id, Operator)
        assert operator.id == operator_by_id.id
        assert operator.url == operator_by_id.url

        operator_by_url = await victor_api.get_operator_by_url(operator.url)
        assert isinstance(operator_by_url, Operator)
        assert operator.id == operator_by_url.id
        assert operator.url == operator_by_url.url


@pytest.mark.asyncio
async def test_get_profiles(victor_api: VictorApi):
    """Test get_profiles."""
    profiles = await victor_api.get_profiles()
    assert profiles is not None
    for profile in profiles:
        assert isinstance(profile, Profile)

        profile_by_id = await victor_api.get_profile_by_id(profile.id)
        assert isinstance(profile_by_id, Profile)
        assert profile.id == profile_by_id.id
        assert profile.url == profile_by_id.url

        profile_by_url = await victor_api.get_profile_by_url(profile.url)
        assert isinstance(profile_by_url, Profile)
        assert profile.id == profile_by_url.id
        assert profile.url == profile_by_url.url


@pytest.mark.asyncio
async def test_traps(victor_api: VictorApi):
    """Test get_traps."""
    traps = await victor_api.get_traps()
    assert traps is not None
    for trap in traps:
        assert isinstance(trap, Trap)

        trap_by_id = await victor_api.get_trap_by_id(trap.id)
        assert isinstance(trap_by_id, Trap)
        assert trap.id == trap_by_id.id
        assert trap.url == trap_by_id.url

        trap_by_url = await victor_api.get_trap_by_url(trap.url)
        assert isinstance(trap_by_url, Trap)
        assert trap.id == trap_by_url.id
        assert trap.url == trap_by_url.url


@pytest.mark.asyncio
async def test_get_users(victor_api: VictorApi):
    """Test get_users."""
    users = await victor_api.get_users()
    assert users is not None
    for user in users:
        assert isinstance(user, User)

        user_by_id = await victor_api.get_user_by_id(user.id)
        assert isinstance(user_by_id, User)
        assert user.id == user_by_id.id
        assert user.url == user_by_id.url

        user_by_url = await victor_api.get_user_by_url(user.url)
        assert isinstance(user_by_url, User)
        assert user.id == user_by_url.id
        assert user.url == user_by_url.url
