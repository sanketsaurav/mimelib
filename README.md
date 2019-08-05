# mimelib 🙊 <a href="https://deepsource.io/gh/sanketsaurav/mimelib/?ref=repository-badge" target="_blank"><img align="right" alt="DeepSource" title="DeepSource" src="https://static.deepsource.io/deepsource-badge-light.svg"></a>

[![Build Status](https://travis-ci.org/sanketsaurav/mimelib.svg?branch=master)](https://travis-ci.org/sanketsaurav/mimelib) [![Coverage Status](https://coveralls.io/repos/github/sanketsaurav/mimelib/badge.svg?branch=master)](https://coveralls.io/github/sanketsaurav/mimelib?branch=master)

> A MIME type is a label used to identify a type of data. It is used so software can know how to handle the data.
> It serves the same purpose on the Internet that file extensions do on Microsoft Windows.
> &mdash; [Quentin](https://stackoverflow.com/a/3828381/1088579)

`mimelib` aims at working with MIME types easier in Python. The standard library comes with the [mimetypes](https://docs.python.org/3/library/mimetypes.html)
module. This library builds on top of it and adds more niceties to it, so you're generally happier when working with MIME types today.


```python
>>> import mimelib
>>> mimelib.mimetype('application/json').is_text
True
>>> mimelib.url('https://example.com/avatar.jpg').is_image
True
>>> mimelib.url('pianoman.mp3').file_type
media
```

## Installation

To install mimelib, use pipenv (or pip):

```
$ pipenv install mimelib
```

## Usage

`mimelib` is intended to be used alongside the `mimetypes` standard library
module, and builds on top of it under the hood. So, if you are adding additional
MIME types to be recognized, `mimelib` will work just as fine.

### Initialization
Either a valid MIME type string, or a URL or path can be used to work with `mimelib`.

```python
>>> m1 = mimelib.mimetype("application/json")  # pass a valid MIME type
>>> m2 = mimelib.url("foo/bar/dataset.csv")  # or pass a path / url
```

Both these methods return a `MIME` object, the various useful properties of which
are listed below.

### Getting the file type

The following file types are reported: `text`, `image`, `media` and `binary`.

```python
>>> mimelib.mimetype("application/ecmascript").file_type
text
>>> mimelib.mimetype("video/mpeg").file_type
media
>>> mimelib.url("archive.rar").file_type
binary
```

The `Mime` object also has the following properties for conveniently checking
specific file types:

 - `is_text`
 - `is_image`
 - `is_media`
 - `is_binary`
