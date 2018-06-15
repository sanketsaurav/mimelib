#!/usr/bin/env python
# -*- coding: utf-8 -*-
from six import string_types
from mimelib import VERSION, mimetype, url


def test_version():
    assert isinstance(VERSION, string_types)


def test_mimetype():
    assert mimetype("application/json").is_text is True


def test_url():
    assert url("https://example.com/foo.csv").is_text is True
