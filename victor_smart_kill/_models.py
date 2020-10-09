"""Models module."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List, Optional, Tuple, Union

from marshmallow_dataclass import class_schema


@dataclass
class Activity:  # pylint: disable=too-many-instance-attributes
    """Activity data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    trap: str
    trap_name: str
    time_stamp: datetime
    time_stamp_unix: datetime
    sequence_number: int
    activity_type: int
    activity_type_text: str
    kills_present: int
    total_kills_reported: int
    battery_level: int
    wireless_network_rssi: int
    firmware_version_string: str
    temperature: int
    board_type: str
    error_code: int
    active: bool
    is_rat_kill: bool = field(metadata={"data_key": "isRatKill"})
    sex_kill_detail: Optional[Any] = field(metadata={"data_key": "sexKillDetail"})
    age_kill_detail: Optional[Any] = field(metadata={"data_key": "ageKillDetail"})
    species_kill_detail: Optional[Any] = field(
        metadata={"data_key": "speciesKillDetail"}
    )
    replaced_attractant: bool = field(metadata={"data_key": "replacedAttractant"})
    replaced_battery: bool = field(metadata={"data_key": "replacedBattery"})
    cleaned_trap: bool = field(metadata={"data_key": "cleanedTrap"})
    note: Optional[Any]
    site_id: Optional[Any]
    building_id: Optional[Any]
    floor_id: Optional[Any]
    floor_plan_x: Optional[Any]
    floor_plan_y: Optional[Any]
    trap_type_text: str

    @property
    def temperature_celcius(self) -> float:
        """Get temperature in celcius."""
        return round(self.temperature / 20, 1)


@dataclass
class MobileApp:  # pylint: disable=too-many-instance-attributes
    """Mobile app data class."""

    url: str
    min_android_version: int
    ideal_android_version: int
    min_ios_version: str
    ideal_ios_version: str
    commercial_min_android_version: int
    commercial_ideal_android_version: int
    commercial_min_ios_version: str
    commercial_ideal_ios_version: str


@dataclass
class Profile:  # pylint: disable=too-many-instance-attributes
    """Profile data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    user: str
    name: Optional[str]
    operator: str
    operator_name: str
    client: Optional[str]
    client_name: Optional[str]
    telephone_number: str
    phone_names: Optional[Any] = field(metadata={"data_key": "phoneNames"})
    phone_numbers: Optional[Any] = field(metadata={"data_key": "phoneNumbers"})
    email_addresses: Optional[Any] = field(metadata={"data_key": "emailAddresses"})
    email_notifications_enabled: bool
    notifications_enabled: bool
    terms_version: int
    notify_wifi_connection: bool
    notify_low_battery: bool
    notify_kill_alerts: bool
    notify_new_products: bool
    text_notifications_enabled: bool
    notify_empty_trap: bool
    fcm_tokens: Optional[Any] = field(metadata={"data_key": "fcmTokens"})
    apns_tokens: Optional[Any] = field(metadata={"data_key": "apnsTokens"})
    fcm_arns: Optional[Any] = field(metadata={"data_key": "fcmARNs"})
    apns_arns: Optional[Any] = field(metadata={"data_key": "apnsARNs"})
    fcm_tokens_pro: Optional[Any] = field(metadata={"data_key": "fcmTokensPro"})
    apns_tokens_pro: Optional[Any] = field(metadata={"data_key": "apnsTokensPro"})
    fcm_arns_pro: Optional[Any] = field(metadata={"data_key": "fcmARNsPro"})
    apns_arns_pro: Optional[Any] = field(metadata={"data_key": "apnsARNsPro"})
    favorite_sites: Optional[Any]
    notify_false_trigger: bool


@dataclass
class User:  # pylint: disable=too-many-instance-attributes
    """User data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    username: str
    password: str
    email: str
    groups: List[str]
    group_names: List[str]
    date_joined: datetime
    last_login: datetime
    first_name: str
    last_name: str
    profile: Profile


@dataclass
class TermsAndConditions:
    """Terms- and condtions data class."""

    id: int  # pylint: disable=invalid-name
    operator_id: int
    time_stamp: datetime
    terms_and_conditions: str
    terms_version: str


@dataclass
class Operator:  # pylint: disable=too-many-instance-attributes
    """Operator data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    account_number: str
    name: str
    address: str
    type: int
    number_sites: int
    number_buildings: int
    number_traps: int
    terms_version: int
    terms: str
    contact: User
    terms_and_conditions: Optional[List[TermsAndConditions]]


@dataclass
class TrapStatistics:  # pylint: disable=too-many-instance-attributes
    """Trap statistics data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    trap: str
    trap_name: str
    kills_present: int
    install_date: datetime
    owner_name: str
    owner_email: str
    last_report_date: datetime
    last_kill_date: Optional[datetime]
    temperature: int
    battery_level: int
    total_kills: Optional[int]
    total_escapes: Optional[int]
    rx_power_level: int
    firmware_version: str
    trap_provisioned: bool
    last_sequence_number: Optional[int]
    total_retreats: Optional[int]
    wireless_network_rssi: int
    error_code: int
    send_conn_lost_nt: bool
    send_empty_trap_nt: bool
    board_type: str
    last_maintenance_date: Union[str, datetime]

    @property
    def temperature_celcius(self) -> float:
        """Get temperature in celcius."""
        return round(self.temperature / 20, 1)


@dataclass
class Trap:  # pylint: disable=too-many-instance-attributes
    """Trap data class."""

    id: int  # pylint: disable=invalid-name
    url: str
    corruption_status: int
    corruption_status_options: Optional[List[Tuple[int, str]]]
    operator: Optional[str]
    operator_name: Optional[str]
    name: str
    ssid: str
    serial_number: str
    auto_upgrade: bool
    status: int
    location: str
    lat: float
    long: float
    upgrade_firmware: Optional[str]
    commercial_gateway: Optional[str]
    commercial_monitor_mode_enabled: bool
    lorawan_app_key: str
    site_name: Optional[str]
    floor_plan_x: int
    floor_plan_y: int
    building_name: Optional[str]
    floor_name: Optional[str]
    room: Optional[str]
    room_name: Optional[str]
    trap_type: int
    trap_type_verbose: str
    alerts: int
    trapstatistics: TrapStatistics

    @property
    def corruption_status_verbose(self) -> Optional[str]:
        """Get description of corruption_status code."""
        if self.corruption_status_options:
            return next(
                item[1]
                for item in self.corruption_status_options
                if item[0] == self.corruption_status
            )
        return None


ActivitySchema = class_schema(Activity)
MobileAppsSchema = class_schema(MobileApp)
OperatorSchema = class_schema(Operator)
ProfileSchema = class_schema(Profile)
TermsAndConditionsSchema = class_schema(TermsAndConditions)
TrapSchema = class_schema(Trap)
TrapStatisticsSchema = class_schema(TrapStatistics)
UserSchema = class_schema(User)
