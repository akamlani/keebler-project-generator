import logging
import sys

from {{cookiecutter.package.name}}.version import __version__

logger = logging.getLogger(__name__)
logging.info(f"{sys.modules[__name__]} loading")


def test_version():
    "test version of module"
    assert "0.0.1" == ".".join(map(str, __version__))
