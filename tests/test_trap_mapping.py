"""Mapping unit tests."""
import json
import pathlib

import pytest
from dateutil.parser import isoparse
from victor_smart_kill._models import TrapSchema


@pytest.fixture()
def trap_json(request) -> dict:
    """Get trap json test data."""
    file = pathlib.Path(request.node.fspath)
    file_path = file.with_name("trap.json")
    with open(file_path) as json_file:
        return json.load(json_file)


def test_trap_mappig(trap_json: dict):
    """Test trap json mapping."""
    trap = TrapSchema().load(trap_json)
    assert trap
    assert trap.id == trap_json["id"]
    assert trap.url == trap_json["url"]
    assert trap.corruption_status == trap_json["corruption_status"]
    assert trap.operator == trap_json["operator"]
    assert trap.operator_name == trap_json["operator_name"]
    assert trap.name == trap_json["name"]
    assert trap.ssid == trap_json["ssid"]
    assert trap.serial_number == trap_json["serial_number"]
    assert trap.auto_upgrade == trap_json["auto_upgrade"]
    assert trap.status == trap_json["status"]
    assert trap.location == trap_json["location"]
    assert trap.lat == float(trap_json["lat"])
    assert trap.long == float(trap_json["long"])
    assert trap.upgrade_firmware == trap_json["upgrade_firmware"]
    assert trap.commercial_gateway == trap_json["commercial_gateway"]
    assert (
        trap.commercial_monitor_mode_enabled
        == trap_json["commercial_monitor_mode_enabled"]
    )
    assert trap.lorawan_app_key == trap_json["lorawan_app_key"]
    assert trap.site_name == trap_json["site_name"]
    assert trap.floor_plan_x == trap_json["floor_plan_x"]
    assert trap.floor_plan_y == trap_json["floor_plan_y"]
    assert trap.building_name == trap_json["building_name"]
    assert trap.floor_name == trap_json["floor_name"]
    assert trap.room == trap_json["room"]
    assert trap.room_name == trap_json["room_name"]
    assert trap.trap_type == trap_json["trap_type"]
    assert trap.trap_type_verbose == trap_json["trap_type_verbose"]
    assert trap.alerts == trap_json["alerts"]

    assert trap.corruption_status_options == [
        tuple(x) for x in trap_json["corruption_status_options"]
    ]

    assert trap.corruption_status_verbose == next(
        item[1]
        for item in trap_json["corruption_status_options"]
        if item[0] == trap_json["corruption_status"]
    )

    assert trap.trapstatistics
    assert trap.trapstatistics.id == trap_json["trapstatistics"]["id"]
    assert trap.trapstatistics.url == trap_json["trapstatistics"]["url"]
    assert trap.trapstatistics.trap == trap_json["trapstatistics"]["trap"]
    assert trap.trapstatistics.trap_name == trap_json["trapstatistics"]["trap_name"]
    assert (
        trap.trapstatistics.kills_present
        == trap_json["trapstatistics"]["kills_present"]
    )
    assert trap.trapstatistics.install_date == isoparse(
        trap_json["trapstatistics"]["install_date"]
    )
    assert trap.trapstatistics.owner_name == trap_json["trapstatistics"]["owner_name"]
    assert trap.trapstatistics.owner_email == trap_json["trapstatistics"]["owner_email"]
    assert trap.trapstatistics.last_report_date == isoparse(
        trap_json["trapstatistics"]["last_report_date"]
    )
    assert trap.trapstatistics.last_kill_date == isoparse(
        trap_json["trapstatistics"]["last_kill_date"]
    )
    assert trap.trapstatistics.temperature == trap_json["trapstatistics"]["temperature"]
    assert (
        trap.trapstatistics.battery_level
        == trap_json["trapstatistics"]["battery_level"]
    )
    assert trap.trapstatistics.total_kills == trap_json["trapstatistics"]["total_kills"]
    assert (
        trap.trapstatistics.total_escapes
        == trap_json["trapstatistics"]["total_escapes"]
    )
    assert (
        trap.trapstatistics.rx_power_level
        == trap_json["trapstatistics"]["rx_power_level"]
    )
    assert (
        trap.trapstatistics.firmware_version
        == trap_json["trapstatistics"]["firmware_version"]
    )
    assert (
        trap.trapstatistics.trap_provisioned
        == trap_json["trapstatistics"]["trap_provisioned"]
    )
    assert (
        trap.trapstatistics.last_sequence_number
        == trap_json["trapstatistics"]["last_sequence_number"]
    )
    assert (
        trap.trapstatistics.total_retreats
        == trap_json["trapstatistics"]["total_retreats"]
    )
    assert (
        trap.trapstatistics.wireless_network_rssi
        == trap_json["trapstatistics"]["wireless_network_rssi"]
    )
    assert trap.trapstatistics.error_code == trap_json["trapstatistics"]["error_code"]
    assert (
        trap.trapstatistics.send_conn_lost_nt
        == trap_json["trapstatistics"]["send_conn_lost_nt"]
    )
    assert (
        trap.trapstatistics.send_empty_trap_nt
        == trap_json["trapstatistics"]["send_empty_trap_nt"]
    )
    assert trap.trapstatistics.board_type == trap_json["trapstatistics"]["board_type"]
    assert (
        trap.trapstatistics.last_maintenance_date
        == trap_json["trapstatistics"]["last_maintenance_date"]
    )
    assert trap.trapstatistics.temperature_celcius == round(
        trap_json["trapstatistics"]["temperature"] / 20, 1
    )
