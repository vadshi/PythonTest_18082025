import subprocess
import sys
from pathlib import Path

import pytest

from Day_3.Solutions.codec26 import decode, encode

def test_decode_example():
    assert decode("070411111426152419071413") == "hello python"

def test_encode_example():
    assert encode("hello python") == "070411111426152419071413"

def test_empty():
    assert decode("") == ""
    assert encode("") == ""

def test_single_space():
    assert decode("26") == " "
    assert encode(" ") == "26"

@pytest.mark.parametrize("text", ["a", "abc", "python is fun", "", "hello world"])
def test_round_trip_text(text):
    assert decode(encode(text)) == text

@pytest.mark.parametrize("num", ["00", "2600", "0126", "070411111426152419071413", ""])
def test_round_trip_num(num):
    assert encode(decode(num)) == num

@pytest.mark.parametrize("num", ["07a4", " 07", "001", "27", "99", "2700"])
def test_decode_errors(num):
    with pytest.raises(ValueError):
        decode(num)

@pytest.mark.parametrize("text", ["Hello!", "привет", "a_b", "a\nb", "a1b", "\t"])
def test_encode_errors(text):
    with pytest.raises(ValueError):
        encode(text)


def _run_cli(stdin: str) -> str:
    """Запускаем CLI и возвращаем последнюю строку вывода."""
    result = subprocess.run(
        [sys.executable, str(Path(__file__).with_name("codec26.py"))],
        input=stdin,
        text=True,
        capture_output=True,
        check=False,
    )
    # возвращаем последнюю непустую строку stdout
    return result.stdout.strip().splitlines()[-1]


def test_cli_encode():
    assert _run_cli("encode\nhello python\n") == "070411111426152419071413"


def test_cli_decode():
    assert _run_cli("decode\n070411111426152419071413\n") == "hello python"

if __name__ == "__main__":
    import pytest, sys
    sys.exit(pytest.main([__file__]))