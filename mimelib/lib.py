#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the core methods exposed by mimelib.
"""
import mimetypes
from future.utils import python_2_unicode_compatible

from . import known


@python_2_unicode_compatible
class Mime(object):
    """
    This class contains the logic for goodies provided by mimelib. It exposes
    `mime` classmethod that is the primary entry-point of this module.
    Generally, the user should never need to create an instance of this class
    directly.
    """

    ALLOWED_DATA_TYPES = ("mimetype", "url")

    def __init__(self, data_type, data):
        """
        Base class that exposes the goodies exposed by mimelib. The user should
        not need to use this class directly.
        """

        if data_type not in self.ALLOWED_DATA_TYPES:
            raise Exception(
                "Invalid value for data_type: {}".format(data_type)
            )

        self.mime_type = None

        self.__file_type = None

        if data_type == "url":
            self.mime_type = mimetypes.guess_type(data, strict=False)[0]
        else:
            self.mime_type = data

    @property
    def file_type(self):
        """
        Returns the file type for the provided URL or MIME type.

        If the type cannot be determined, or the MIME type provided is not
        recognized, return an empty string.
        """
        if self.__file_type is None:
            self.__file_type = self.__get_file_type()
        return self.__file_type

    def __get_file_type(self):
        # check if this the MIME type is recognized
        if not (self.mime_type and
                mimetypes.guess_extension(self.mime_type, strict=False)):
            return ''

        # check if it's an image
        if self.mime_type.startswith("image/"):
            return "image"

        # check it's a text file
        if (self.mime_type.startswith("text/") or
                self.mime_type in known.TEXT_MIME_TYPES):
            return "text"

        # check if it's a media file
        if (self.mime_type.startswith("audio/") or
                self.mime_type.startswith("video/")):
            return "media"

        # finally, since the MIME type has been checked for validity,
        # it can be considered binary if nothing else matches.
        return "binary"

    @property
    def is_image(self):
        """Returns True if the given URL or MIME type can be safely considered
        an image.
        """
        return self.file_type == "image"

    @property
    def is_text(self):
        """Returns True if the given URL or MIME type can be safely considered
        as text."""
        return self.file_type == "text"

    @property
    def is_media(self):
        """Returns True if the given URL or MIME type can be safely considered
        an audio or video."""
        return self.file_type == "media"

    @property
    def is_binary(self):
        """Returns True if the given URL or MIME type can be considered
        an application binary."""
        return self.file_type == "binary"
