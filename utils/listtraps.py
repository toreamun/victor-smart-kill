#!/usr/bin/env python3.8

"""List the traps and status."""

import argparse
import asyncio
import logging
import os
import sys

sys.path.append(os.path.abspath(".."))
from victor_smart_kill import VictorApi, VictorAsyncClient  # noqa:E402

_version = "0.1"

try:
    import config
except ImportError:
    logging.warning(
        (
            "No config file present. Copy sample_config.py to config.py"
            " and add your username and password."
        )
    )
    sys.exit(1)


async def start():
    """Print trap details."""
    async with VictorAsyncClient(config.username, config.password) as client:
        if os.path.exists(".token"):
            client._token = open(".token").read()

        api = VictorApi(client)

        if client._token:
            open(".token", "w").write(client._token)

        traps = await api.get_traps()

        traps.sort(key=lambda x: x.name)
        for n, trap in enumerate(traps):
            print(
                "%2s %-30s %10s %3s %3s %3s"
                % (
                    n,
                    trap.name,
                    trap.ssid,
                    trap.status,
                    trap.trapstatistics.battery_level,
                    trap.trapstatistics.kills_present,
                )
            )

        if 0:
            history = await api.get_trap_history(traps[0].id)
            for act in history:
                print(
                    act.sequence_number,
                    act.time_stamp,
                    act.activity_type,
                    act.activity_type_text,
                    act.battery_level,
                    act.is_rat_kill,
                )


def test():
    """Print test info."""
    logging.warn("Testing")


def parse_args(argv):
    """Parse command arguments."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter, description=__doc__
    )

    parser.add_argument(
        "-t",
        "--test",
        dest="test_flag",
        default=False,
        action="store_true",
        help="Run test function",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Desired console log level",
    )
    parser.add_argument(
        "-d",
        "--debug",
        dest="log_level",
        action="store_const",
        const="DEBUG",
        help="Activate debugging",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        dest="log_level",
        action="store_const",
        const="CRITICAL",
        help="Quite mode",
    )
    # parser.add_argument("files", type=str, nargs='+')

    args = parser.parse_args(argv[1:])

    return parser, args


def main(argv, stdout, environ):
    """Program main entry point."""
    if sys.version_info < (3, 0):
        reload(sys)
        sys.setdefaultencoding("utf8")

    parser, args = parse_args(argv)

    logging.basicConfig(
        format="[%(asctime)s] %(levelname)-8s %(message)s",
        datefmt="%m/%d %H:%M:%S",
        level=args.log_level,
    )

    if args.test_flag:
        test()
        return

    asyncio.run(start())


if __name__ == "__main__":
    main(sys.argv, sys.stdout, os.environ)
