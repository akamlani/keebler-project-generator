import glob
import io
import json
import logging
import os
import zipfile
from pathlib import Path
from urllib.parse import urlparse

import hydra
import pandas as pd
import yaml
from omegaconf import DictConfig, OmegaConf

logger = logging.getLogger(__name__)


def check_url_is_valid(uri: str) -> bool:
    """validates if url is valid

    Args:
        uri (str): url

    Returns:
        bool: validation performance
    """
    try:
        result = urlparse(uri)
        return all([result.scheme, result.netloc])
    except Exception as e:
        logger.exception(f"Exception Occured Reading url: {uri}:{e}")


def read_json(file_path: str, encoding="utf-8") -> dict:
    """
    Reads a JSON File
    :param file_path: file path towards content to read
    :param encoding: encoding representation of file, default to utf-8
    :return: dictionary of contents read
    """
    try:
        if Path(file_path).is_file():
            with open(file_path, encoding=encoding) as f:
                data: dict = json.load(f)
            return data
        else:
            logger.error(f"File: {file_path} does not Exist")
    except Exception as e:
        logger.exception(f"Exception Occured Reading File: {file_path}:{e}")


def read_yaml(file_path: str, encoding: str = "utf-8") -> dict:
    """
    Reads a Yaml File
    :param file_path: file path towards content to read
    :param encoding: encoding representation of file, defaults to utf-8
    :return: dictionary of contents read
    """
    try:
        if Path(file_path).is_file():
            with open(file_path, encoding=encoding) as f:
                data: dict = yaml.load(f, Loader=yaml.FullLoader)
                return data
        else:
            logger.error(f"File: {file_path} does not Exist")
    except Exception as e:
        logger.exception(f"Exception Occured Reading File: {file_path}:{e}")


def read_hydra(file_path: str) -> DictConfig:
    """
    Reads a Yaml File
    :param file_path: file path towards content to read
    :return: dictionary configuration
    """
    try:
        if Path(file_path).is_file():
            return OmegaConf.load(file_path)
        else:
            logger.error(f"File: {file_path} does not Exist")
    except Exception as e:
        logger.exception(f"Exception Occured Reading File: {file_path}:{e}")
