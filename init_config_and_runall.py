# %%
import toml
import init_config
import run_all
import subprocess


def init_config_and_runall():
    subprocess.run("cd build_release;make -j;", shell=True)
    with open("configs.toml") as f:
        configs = toml.load(f)
        for c in configs["config"]:
            init_config.init_config(c)
            run_all.run_all(c)
            pass

# %%


if __name__ == "__main__":
    init_config_and_runall()

# %%
