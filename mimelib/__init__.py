#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['mimetype', 'url', 'VERSION']

from .__version__ import __version__
from .lib import Mime

VERSION = __version__


def mimetype(mime_type):
    """Takes in a MIME type string and provides information about it.

    Usage:
        >>> mimelib.mimetype("application/json").is_text
        True
        >>> mimelib.mimetype("font/woff2").is_binrary
        True
        >>> mimelib.mimetype("application/x-tar").is_image
        False
    """
    return Mime("mimetype", mime_type)


def url(url):
    """Takes in a URL or a valid file path and provides information about it.

    Usage:
        >>> mimelib.url("https://example.com/foo.csv").is_text
        True
        >>> mimelib.url("hunter.png").is_image
        True
    """
    return Mime("url", url)
