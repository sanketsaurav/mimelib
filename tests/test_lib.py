#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pytest import raises
from mimelib.lib import Mime


def test_mime_object_init():
    assert Mime("mimetype", "application/json").mime_type == "application/json"
    assert Mime("url", "foo/bar.png").mime_type == "image/png"


def test_mime_object_wrong_init():
    with raises(Exception) as exc:
        Mime("foobar", "dummy")
    assert str(exc.value) == "Invalid value for data_type: foobar"


def test_mime_file_type():
    assert Mime("url", "https://example.com/foo/bar.txt").file_type == "text"
    assert Mime("mimetype", "text/css").file_type == "text"
    assert Mime("url", "example/foo.png").file_type == "image"
    assert Mime("mimetype", "image/jpeg").file_type == "image"
    assert Mime("url", "example/video.mpg").file_type == "media"
    assert Mime("mimetype", "audio/midi").file_type == "media"
    assert Mime("url", "foo.zip").file_type == "binary"
    assert Mime("mimetype", "application/pdf").file_type == "binary"
    assert Mime("mimetype", "application/dummy").file_type is None


def test_mime_is_image():
    assert Mime("url", "https://example.com/foo.png").is_image is True
    assert Mime("url", "foo/bar/baz.jpeg").is_image is True
    assert Mime("mimetype", "image/jpeg").is_image is True
    assert Mime("url", "https://example.com/foo/bar.json").is_image is False
    assert Mime("mimetype", "text/csv").is_image is False


def test_mime_is_text():
    assert Mime("url", "https://example.com/robots.html").is_text is True
    assert Mime("mimetype", "application/json").is_text is True
    assert Mime("url", "foo.mp3").is_text is False
    assert Mime("mimetype", "application/octet-stream").is_text is False


def test_mime_is_media():
    assert Mime("url", "https://foo.mp3").is_media is True
    assert Mime("mimetype", "application/x-bzip").is_media is False


def test_mime_is_binary():
    assert Mime("url", "foo.zip").is_binary is True
    assert Mime("mimetype", "application/json").is_binary is False
