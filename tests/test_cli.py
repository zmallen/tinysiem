import pytest

from tinysiem.__main__ import main


def test_help_succeeds(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--help"])

    assert exit_info.value.code == 0
    assert "usage: tinysiem" in capsys.readouterr().out


def test_unknown_argument_fails(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        main(["--unknown"])

    assert exit_info.value.code == 2
    assert "unrecognized arguments: --unknown" in capsys.readouterr().err
