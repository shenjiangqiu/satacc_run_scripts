# %%
import json
import os
from typing import Dict
import toml
import config_suffix
import subprocess
import checkpoint_start


def average_of_list(data, name):
    target_data = [v[name] for v in data]
    return sum(target_data)/len(target_data)


def print_data(data, tasks, cnfs):
    print("configs: ", end=" ")
    for config in tasks:
        print(config, end=" ")
    print()
    for cnf in cnfs:
        print(cnf, end=" ")
        for config in tasks:
            if cnf in data[config]:
                print(data[config][cnf], end=" ")
            else:
                print("-", end=" ")
        print()

# %%


def read_json(config: Dict):

    tasks = ["1x1", "1x4", "4x4", "4x16", "16x16"]
    cnfs = [cnf[0] for cnf in checkpoint_start.cnfs]
    decoder = json.decoder.JSONDecoder()

    cycles = dict()
    average_assignments = dict()
    average_watchers = dict()
    average_clauses = dict()
    l3_cache_statistics = dict()
    l1_cache_miss_rate = dict()
    watcher_idle_rate = dict()
    clause_idle_rate = dict()
    # %%

    suffix = config_suffix.get_suffix(config)
    print(suffix)
    tasks = [task+suffix for task in tasks]
    for config in tasks:
        cycles[config] = dict()
        average_assignments[config] = dict()
        average_watchers[config] = dict()
        average_clauses[config] = dict()
        l3_cache_statistics[config] = dict()

        l1_cache_miss_rate[config] = dict()
        watcher_idle_rate[config] = dict()
        clause_idle_rate[config] = dict()
        for cnf in cnfs:
            file = f"{config}/{cnf}/statistics.json"
            if not os.path.exists(file):
                print(file, "not exists")
                continue
            with open(file) as f:
                data = decoder.decode(f.read())
                cycles[config][cnf] = data["total_cycle"]
                average_assignments[config][cnf] = data["average_assignments"]["total"] / \
                    data["average_assignments"]["count"]
                average_watchers[config][cnf] = data["average_watchers"]["total"] / \
                    data["average_watchers"]["count"]
                average_clauses[config][cnf] = data["average_clauses"]["total"] / \
                    data["average_clauses"]["count"]
                cache_data = data["l3_cache_statistics"]
                hits = cache_data["cache_hits"]
                misses = cache_data["cache_misses"]
                miss_rate = misses/(hits+misses)
                l3_cache_statistics[config][cnf] = miss_rate

                l1_cache_data_array = data["private_cache_statistics"]
                cache_hits = average_of_list(l1_cache_data_array, "cache_hits")
                cache_misses = average_of_list(
                    l1_cache_data_array, "cache_misses")
                cache_miss_rate = cache_misses/(cache_hits+cache_misses)
                l1_cache_miss_rate[config][cnf] = cache_miss_rate

                watcher_idle_data_array = data["watcher_statistics"]
                idle_cycls = average_of_list(
                    watcher_idle_data_array, "idle_cycle")
                busy_cycle = average_of_list(
                    watcher_idle_data_array, "busy_cycle")
                idle_rate = idle_cycls/(idle_cycls+busy_cycle)
                watcher_idle_rate[config][cnf] = idle_rate
                clause_data = data["clause_statistics"]
                total_idle = 0
                total_busy = 0
                for single_clause in clause_data:
                    for clause in single_clause["single_clause"]:
                        total_idle += clause["idle_cycle"]
                        total_busy += clause["busy_cycle"]
                idle_rate = total_idle/(total_idle+total_busy)
                clause_idle_rate[config][cnf] = idle_rate
    for data_to_print in [cycles,
                          # average_assignments, average_watchers,
                          #average_clauses, l3_cache_statistics, l1_cache_miss_rate,
                          #watcher_idle_rate, clause_idle_rate
                          ]:
        print_data(data_to_print, tasks, cnfs)
        print()


def read_json_all():
    with open("configs.toml") as f:
        configs = toml.load(f)
        for c in configs["config"]:
            read_json(c)
            pass

# %%

# %%


# %%
if __name__ == "__main__":
    read_json_all()
