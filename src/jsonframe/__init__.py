from importlib.metadata import PackageNotFoundError, version as _pkg_version

from .frames import SuccessFrame, ErrorDetail, ErrorFrame
from .helpers import ok, error

__all__ = ["SuccessFrame", "ErrorDetail", "ErrorFrame", "ok", "error"]

try:
    __version__ = _pkg_version("jsonframe")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"
