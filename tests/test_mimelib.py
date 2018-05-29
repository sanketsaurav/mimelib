from mimelib import VERSION
from six import string_types


def test_version():
    assert isinstance(VERSION, string_types)
