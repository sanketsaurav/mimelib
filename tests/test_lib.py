#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pytest import raises
from mimelib.lib import Mime

NUM_GET_FILE_TYPE_CALLED = 0


def only_once(func):
    def wrap():
        global NUM_GET_FILE_TYPE_CALLED
        NUM_GET_FILE_TYPE_CALLED += 1
        return func()
    return wrap


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
    assert Mime("mimetype", "application/dummy").file_type == ''


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


def test_mime_unrecognized_type():
    assert Mime("mimetype", "foo/bar").file_type == ''
    assert Mime("url", "dummy.baz").file_type == ''


def test_get_file_type_executes_only_once():
    obj = Mime("url", "https://foo.mp3")
    assert NUM_GET_FILE_TYPE_CALLED == 0
    obj._Mime__get_file_type = only_once(obj._Mime__get_file_type)
    assert obj.file_type == 'media'
    assert obj.file_type == 'media'
    assert NUM_GET_FILE_TYPE_CALLED == 1
