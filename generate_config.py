# %%
import toml
from typing import *

a = {"config": []}
a["config"].append({"l3_cache": {"hit": False, "miss": True}})
a["config"].append({"l3_cache": {"hit": True, "miss": False}})
print(toml.dumps(a))

# %%
