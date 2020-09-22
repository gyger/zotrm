# -*- coding: utf-8 -*-
from pathlib import Path

from pkg_resources import get_distribution, DistributionNotFound
from appdirs import user_data_dir


dist_name = __name__
dist_author = "samuelyeewl"

try:
    # Change here if project is renamed and does not equal the package name
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound

config_path = Path(user_data_dir(dist_name, dist_author))