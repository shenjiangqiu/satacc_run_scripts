import toml
from typing import *


def get_suffix(config: Dict[str, Any]) -> str:
    return "_"+"_".join(["{}".format(v) for v in config.values()])
