#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MIME file type knowledge base."""

# list of known MIME types, apart from the ones starting with `text/`
# that can be safely rendered as textual data.
TEXT_MIME_TYPES = (
    'application/ecmascript',
    'application/javascript', 'application/json',
    'application/typescript',
    'application/vnd.mozilla.xul+xml',
    'application/x-csh', 'application/x-sh',
    'application/xhtml+xml', 'application/xml',
)
