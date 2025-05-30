"""CLI for GogoGate2 and iSmartGate devices."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from enum import Enum
from collections.abc import Callable

import pytest
from unittest.mock import MagicMock, Mock, patch
from click.testing import CliRunner
from typing import Final

import ismartgate.cli as cli_module
from ismartgate import GogoGate2Api, ISmartGateApi
from ismartgate.cli import (
    Command,
    DeviceType,
    Option,
    cli,
    gogogate2_cli,
    ismartgate_cli,
)


class StubbedTypeEnum(Enum):
    """Test enum."""

    TYPE1 = "type1"
    TYPE2 = "type2"


@dataclass
class StubbedClassData:
    """Test data class."""

    name: str
    type: StubbedTypeEnum


@patch("ismartgate.cli.GogoGate2Api")
def test_info(class_mock: Mock) -> None:
    """Test get device info."""
    api: Final = MagicMock(spec=GogoGate2Api)
    class_mock.return_value = api
    api.async_info.return_value = StubbedClassData(
        name="my_name", type=StubbedTypeEnum.TYPE1
    )

    runner: Final = CliRunner()
    result = runner.invoke(
        cli,
        (
            Option.HOST.value,
            "my_host",
            Option.USERNAME.value,
            "my_username",
            Option.PASSWORD.value,
            "my_password",
            Option.DEVICE_TYPE.value,
            DeviceType.GOGOGATE2.value,
            Command.INFO.value,
        ),
    )
    assert result.exit_code == 0
    assert json.loads(result.output) == json.loads(
        """
        {
            "name": "my_name",
            "type": "type1"
        }
    """
    )


@patch("ismartgate.cli.GogoGate2Api")
@patch("ismartgate.cli.getpass")
def test_open_with_stdin_password(getpass: Mock, class_mock: Mock) -> None:
    """Test open door."""
    api: Final = MagicMock(spec=GogoGate2Api)
    class_mock.return_value = api
    api.async_open_door.return_value = True

    getpass.return_value = "my_password"

    runner: Final = CliRunner()
    result = runner.invoke(
        cli,
        (
            Option.HOST.value,
            "my_host",
            Option.USERNAME.value,
            "my_username",
            Option.PASSWORD.value,
            "-",
            Option.DEVICE_TYPE.value,
            DeviceType.GOGOGATE2.value,
            Command.OPEN.value,
            "1",
        ),
    )
    assert result.exit_code == 0
    assert json.loads(result.output) is True


@patch("ismartgate.cli.ISmartGateApi")
@patch("ismartgate.cli.getpass")
def test_close_without_password_option(getpass: Mock, class_mock: Mock) -> None:
    """Test close door."""
    api: Final = MagicMock(spec=ISmartGateApi)
    class_mock.return_value = api
    api.async_close_door.return_value = False

    getpass.return_value = "my_password"

    runner: Final = CliRunner()
    result = runner.invoke(
        cli,
        args=(
            Option.HOST.value,
            "my_host",
            Option.USERNAME.value,
            "my_username",
            Option.DEVICE_TYPE.value,
            DeviceType.ISMARTGATE.value,
            Command.CLOSE.value,
            "1",
        ),
    )
    if result.exception:
        raise result.exception
    assert result.exit_code == 0
    assert json.loads(result.output) is False


@pytest.mark.parametrize(("cli_func",), ((gogogate2_cli,), (ismartgate_cli,)))
def test_device_cli(cli_func: Callable) -> None:
    """Test specific CLI call doesn't crash.."""
    with patch.object(sys, "argv", ["--help"]), patch.object(sys, "exit"):
        cli_func()


@patch.object(cli_module, "__name__", "__main__")
@patch.object(cli_module, "cli")
def test_maybe_init_is_main(cli_mock: Mock) -> None:
    """Test cli called when file is main."""
    cli_module.maybe_init()
    cli_mock.assert_called()


@patch.object(cli_module, "cli")
def test_maybe_init_is_not_main(cli_mock: Mock) -> None:
    """Test cli not called when file is not main."""
    cli_module.maybe_init()
    cli_mock.assert_not_called()
