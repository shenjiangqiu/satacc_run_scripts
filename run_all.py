import os
import subprocess
from multiprocessing import Pool
import checkpoint_start
import config_suffix


def run_all(config):

    configs = ["1x1", "1x4", "4x4", "4x16", "16x16"]

    cnf_root = os.path.abspath(os.path.expanduser("~/cnfs/"))

    cnfs = [i[0] for i in checkpoint_start.cnfs]
    checkpoint_start_int = [i[1] for i in checkpoint_start.cnfs]

    check_points = [f"{a}.checkpint" for a in cnfs]

    end_props_int = [i+100000 for i in checkpoint_start_int]
    end_props = [str(i) for i in end_props_int]

    def run_task(command):
        # print("going to run {}".format(command))
        subprocess.run(command, shell=True)
    suffix = config_suffix.get_suffix(config)
    configs = [c+suffix for c in configs]

    commands = [
        f"sjqjobsender \'cd ~/satacc_run;\
    cd {config};mkdir {c};\
    cd {c};\
    ln -sf ../satacc_config.toml ./;\
    ../../build_release/minisat/minisat -enable-acc -load -checkpoint-name=../../new_save_checkpoints/{c}/{checkpoint} \
    -end-prop={end_prop} {os.path.join(cnf_root, c)}  \
    > result_{c}.txt 2> result_{c}.err \'" for config in configs
        for c, checkpoint, end_prop in zip(cnfs, check_points, end_props)]

    for cnf in cnfs:
        checkpoint_path = f"new_save_checkpoints/{cnf}/{cnf}.checkpint"
        if not os.path.exists(checkpoint_path):
            print(f"checkpint not exits in {checkpoint_path}")
            exit(-1)

    cnf_paths = [os.path.join(cnf_root, c) for c in cnfs]
    path_exits = True
    for cnf_path in cnf_paths:
        if not os.path.isfile(cnf_path):
            path_exits = False
            print("cnf path not exits: {}".format(cnf_path))
    if not path_exits:
        exit(-1)

    for i in commands:
        run_task(i)
