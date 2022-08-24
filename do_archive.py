# %%
import os

import config_suffix


def archive(config):
    configs = ["1x1", "1x4", "4x4", "4x16", "16x16"]
    suffix = config_suffix.get_suffix(config)

    os.mkdir(f"archive{suffix}")

    configs = [config+suffix for config in configs]

    # move folder to archive
    for config in configs:
        folder_name = config
        src = "./" + folder_name
        dst = f"./archive{suffix}/" + folder_name
        os.rename(src, dst)
        print("moved " + src + " to " + dst)

    # %%
