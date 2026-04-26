from importlib.metadata import version as _pkg_version

from .frames import ErrorDetail, ErrorFrame, SuccessFrame
from .helpers import error, ok

__all__ = ["SuccessFrame", "ErrorDetail", "ErrorFrame", "ok", "error"]

__version__ = _pkg_version("jsonframe")
