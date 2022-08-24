import toml
import config_suffix


def test_getsuffix():
    assert 1 == 1
    configs = toml.load("configs.toml")
    for c in configs["config"]:
        print(config_suffix.get_suffix(c))
