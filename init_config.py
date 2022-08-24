# %%
import os
import toml
import shutil
import config_suffix


def init_config(config):
    configs = ["1x1", "1x4", "4x4", "4x16", "16x16"]
    for c in configs:
        suffix = config_suffix.get_suffix(config)
        c = c+suffix
        if not os.path.exists(c):
            os.mkdir(c)
        num_config = c.split("_")[0].split("x")
        watchers = int(num_config[0])
        clauses = int(num_config[1])
        clauses = int(clauses/watchers)
        shutil.copy(f"template/satacc_config.toml", c)
        shutil.copy(f"template/checkpoint_start.py", c)
        shutil.copy(f"template/run.py", c)
        config_file = toml.load(open(f"{c}/satacc_config.toml", "r"))
        config_file["n_watchers"] = watchers
        config_file["n_clauses"] = clauses
        config_file.update(config)
        new_config_file = toml.dumps(config_file)
        with open(f"{c}/satacc_config.toml", "w") as f:
            f.write(new_config_file)

    # %%
