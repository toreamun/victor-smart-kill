"""API module."""
from typing import Any, Dict, List

from marshmallow import RAISE
from marshmallow.schema import Schema

from ._client import VictorAsyncClient
from ._models import (
    Activity,
    ActivitySchema,
    MobileApp,
    MobileAppsSchema,
    Operator,
    OperatorSchema,
    Profile,
    ProfileSchema,
    Trap,
    TrapSchema,
    User,
    UserSchema,
)


class VictorApi:
    """Access Victor remote API."""

    def __init__(self, victor_client: VictorAsyncClient, unknown: str = None) -> None:
        """Initialize VictorApi."""
        if not victor_client:
            raise ValueError("Victor client is required.")
        self._client = victor_client
        self._unknown = RAISE if unknown is None else unknown

    async def _get_json_list(self, url: str) -> List[Dict[str, Any]]:
        response = await self._client.get(url)
        response.raise_for_status()
        json = response.json()

        if isinstance(json, list):
            return json

        result = json.get("results")
        if result:
            return result

        raise Exception("Unexpected response content")

    async def _get_list_by_schema(self, schema: Schema, url: str) -> List[Any]:
        return schema.load(
            await self._get_json_list(url), unknown=self._unknown, many=True
        )

    async def _get_json(self, url: str) -> Dict[str, Any]:
        response = await self._client.get(url)
        response.raise_for_status()
        return response.json()

    async def _get_by_schema(self, schema: Schema, url: str) -> Any:
        return schema.load(await self._get_json(url), unknown=self._unknown)

    async def get_activity_logs(self) -> List[Activity]:
        """Get activity logs."""
        return await self._get_list_by_schema(ActivitySchema(), "activitylogs/")

    async def get_activity_log_record(self, log_record_id: int) -> Activity:
        """Get activity log record by record id."""
        return await self._get_by_schema(
            ActivitySchema(), f"activitylogs/{log_record_id}/"
        )

    async def get_mobile_apps(self) -> List[MobileApp]:
        """Get mobile apps."""
        return await self._get_list_by_schema(MobileAppsSchema(), "mobileapps/")

    async def get_mobile_app_by_id(self, app_id: int) -> MobileApp:
        """Get mobile app by app id."""
        return await self.get_mobile_app_by_url(f"mobileapps/{app_id}/")

    async def get_mobile_app_by_url(self, url: str) -> MobileApp:
        """Get mobile app by url."""
        return await self._get_by_schema(MobileAppsSchema(), url)

    async def get_operators(self) -> List[Operator]:
        """Get operators."""
        return await self._get_list_by_schema(OperatorSchema(), "operators/")

    async def get_operator_by_id(self, operator_id: int) -> Operator:
        """Get operator by operator id."""
        return await self.get_operator_by_url(f"operators/{operator_id}/")

    async def get_operator_by_url(self, url: str) -> Operator:
        """Get operator by url."""
        return await self._get_by_schema(OperatorSchema(), url)

    async def get_profiles(self) -> List[Profile]:
        """Get profiles."""
        return await self._get_list_by_schema(ProfileSchema(), "profiles/")

    async def get_profile_by_id(self, profile_id: int) -> Profile:
        """Get profile by profile id."""
        return await self.get_profile_by_url(f"profiles/{profile_id}/")

    async def get_profile_by_url(self, url: str) -> Profile:
        """Get profile by url."""
        return await self._get_by_schema(ProfileSchema(), url)

    async def get_traps(self) -> List[Trap]:
        """Get traps."""
        return await self._get_list_by_schema(TrapSchema(), "traps/")

    async def get_trap_by_id(self, trap_id: int) -> Trap:
        """Get trap by trap id."""
        return await self.get_trap_by_url(f"traps/{trap_id}/")

    async def get_trap_by_url(self, url: str) -> Trap:
        """Get trap by url."""
        return await self._get_by_schema(TrapSchema(), url)

    async def get_trap_history(self, trap_id: int) -> List[Activity]:
        """Get trap history by trap id."""
        return await self._get_list_by_schema(
            ActivitySchema(), f"traps/{trap_id}/history/"
        )

    async def get_users(self) -> List[User]:
        """Get users."""
        return await self._get_list_by_schema(UserSchema(), "users/")

    async def get_user_by_id(self, user_id: int) -> User:
        """Get user by user id."""
        return await self.get_user_by_url(f"users/{user_id}/")

    async def get_user_by_url(self, url: str) -> User:
        """Get user by user id."""
        return await self._get_by_schema(UserSchema(), url)
