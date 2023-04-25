import warnings
from typing import Any

from dotenv import dotenv_values, find_dotenv, load_dotenv

warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")


def read_env(root_path: str = ".env") -> dict:
    """_summary_

    Args:
        root_path (str, optional): _description_. Defaults to ".env".

    Returns:
        dict: key:value of loaded environment variables

    Examples:
    >>> read_env(".env.shared")
    >>> read_env()
    """
    load_dotenv(find_dotenv())
    config: dict = dotenv_values(root_path)
    return config


def ifnone(a: Any, b: Any) -> Any:
    "`a` if `a` is not None, otherwise `b`."
    return b if a is None else a
