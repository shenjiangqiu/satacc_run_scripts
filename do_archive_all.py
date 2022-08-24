# %%
import toml
import init_config
import run_all
import do_archive


def archive_all():
    with open("configs.toml") as f:
        configs = toml.load(f)
        for c in configs["config"]:
            do_archive.archive(c)
            pass

# %%


if __name__ == "__main__":
    archive_all()

# %%
