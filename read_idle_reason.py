# %%
import json


tasks = ["1x1", "1x4", "4x4", "4x16", "16x16"]
cnfs = [
    "b1904P1-8x8c6h5SAT.cnf",
    "b1904P3-8x8c11h0SAT.cnf",
    "eqsparcl10bpwtrc10.cnf",
    "eqspdtlf14bpwtrc14.cnf",
    "eqspwtrc16bparrc16.cnf",
    "Grain_no_init_ver1_out200_known_last104_0.cnf",
    "Haystacks-ext-12_c18.cnf",
    "hcp_bij16_16.cnf",
    "hcp_CP20_20.cnf",
    "hcp_CP24_24.cnf",
    "knight_20.cnf",
    "Mickey_out250_known_last146_0.cnf",
    "MM-23-2-2-2-2-3.cnf",
    "QuasiGroup-4-12_c18.cnf",
    "sha1r17m145ABCD.cnf",
    "sha1r17m72a.cnf",
    "size_4_4_4_i0418_r8.cnf",
    "size_5_5_5_i003_r12.cnf",
    "toughsat_28bits_0.cnf",
    "toughsat_30bits_0.cnf",
    "Trivium_no_init_out350_known_last142_1.cnf"
]
clause_idle_rate = dict()
clause_idle_no_task = dict()
clause_idle_wating_l1 = dict()
clause_idle_wating_l3 = dict()
clause_idle_send_l1 = dict()
clause_idle_send_l3 = dict()

icnt_idle_rate = dict()
icnt_latency = dict()

watcher_idle_rate = dict()
watcher_idle_no_task = dict()
watcher_idle_wating_l1 = dict()
watcher_idle_wating_l3 = dict()
watcher_idle_send_l1 = dict()
watcher_idle_send_l3 = dict()
watcher_idle_send_clause = dict()

all_stats = {"clause_idle_rate": clause_idle_rate,
             "clause_idle_no_task": clause_idle_no_task,
             "clause_idle_wating_l1": clause_idle_wating_l1,
             "clause_idle_wating_l3": clause_idle_wating_l3,
             "clause_idle_send_l1": clause_idle_send_l1,
             "clause_idle_send_l3": clause_idle_send_l3,
             "icnt_idle_rate": icnt_idle_rate,
             "icnt_latency": icnt_latency,
             "watcher_idle_rate": watcher_idle_rate,
             "watcher_idle_no_task": watcher_idle_no_task,
             "watcher_idle_wating_l1": watcher_idle_wating_l1,
             "watcher_idle_wating_l3": watcher_idle_wating_l3,
             "watcher_idle_send_l1": watcher_idle_send_l1,
             "watcher_idle_send_l3": watcher_idle_send_l3,
             "watcher_idle_send_clause": watcher_idle_send_clause}


def average(data):
    return sum(data)/len(data)


def rate(a, b):
    return a/(a+b)


for config in tasks:

    watcher_idle_rate[config] = dict()
    clause_idle_rate[config] = dict()
    clause_idle_no_task[config] = dict()
    clause_idle_wating_l1[config] = dict()
    clause_idle_wating_l3[config] = dict()
    clause_idle_send_l1[config] = dict()
    clause_idle_send_l3[config] = dict()
    icnt_idle_rate[config] = dict()
    watcher_idle_no_task[config] = dict()
    watcher_idle_wating_l1[config] = dict()
    watcher_idle_wating_l3[config] = dict()
    watcher_idle_send_l1[config] = dict()
    watcher_idle_send_l3[config] = dict()
    watcher_idle_send_clause[config] = dict()
    icnt_latency[config] = dict()

    for cnf in cnfs:
        file = f"{config}/{cnf}/statistics.json"
        with open(file) as f:
            data = json.load(f)
            average_watcher_idle = average([d["idle_cycle"]
                                            for d in data["watcher_statistics"]])
            average_watcher_busy = average([d["busy_cycle"]
                                            for d in data["watcher_statistics"]])
            average_watcher_idle_no_task = average(
                [d["idle_stat"]["idle_no_task"] for d in data["watcher_statistics"]])
            average_watcher_idle_wating_l1 = average(
                [d["idle_stat"]["idle_wating_l1"] for d in data["watcher_statistics"]])
            average_watcher_idle_wating_l3 = average(
                [d["idle_stat"]["idle_wating_l3"] for d in data["watcher_statistics"]])
            average_watcher_idle_send_l1 = average(
                [d["idle_stat"]["idle_send_l1"] for d in data["watcher_statistics"]])
            average_watcher_idle_send_l3 = average(
                [d["idle_stat"]["idle_send_l3"] for d in data["watcher_statistics"]])
            average_watcher_idle_send_clause = average(
                [d["idle_stat"]["idle_send_clause"] for d in data["watcher_statistics"]])
            watcher_idle_rate[config][cnf] = rate(
                average_watcher_idle, average_watcher_busy)
            watcher_idle_no_task[config][cnf] = average_watcher_idle_no_task / \
                average_watcher_idle
            watcher_idle_wating_l1[config][cnf] = average_watcher_idle_wating_l1 / \
                average_watcher_idle
            watcher_idle_wating_l3[config][cnf] = average_watcher_idle_wating_l3 / \
                average_watcher_idle
            watcher_idle_send_l1[config][cnf] = average_watcher_idle_send_l1 / \
                average_watcher_idle
            watcher_idle_send_l3[config][cnf] = average_watcher_idle_send_l3 / \
                average_watcher_idle
            watcher_idle_send_clause[config][cnf] = average_watcher_idle_send_clause / \
                average_watcher_idle

            average_clause_idle = average(
                [average([d["idle_cycle"] for d in watcher["single_clause"]])for watcher in data["clause_statistics"]])
            average_clause_busy = average(
                [average([d["busy_cycle"] for d in watcher["single_clause"]])for watcher in data["clause_statistics"]])
            average_clause_idle_no_task = average(
                [average([d["idle_stat"]["idle_no_task"] for d in watcher["single_clause"]])for watcher in data["clause_statistics"]])
            average_clause_idle_wating_l1 = average(
                [average([d["idle_stat"]["idle_wating_l1"] for d in watcher["single_clause"]])for watcher in data["clause_statistics"]])
            average_clause_idle_wating_l3 = average(
                [average([d["idle_stat"]["idle_wating_l3"] for d in watcher["single_clause"]])for watcher in data["clause_statistics"]])
            average_clause_idle_send_l1 = average(
                [average([d["idle_stat"]["idle_send_l1"] for d in watcher["single_clause"]])for watcher in data["clause_statistics"]])
            average_clause_idle_send_l3 = average(
                [average([d["idle_stat"]["idle_send_l3"] for d in watcher["single_clause"]])for watcher in data["clause_statistics"]])
            clause_idle_rate[config][cnf] = rate(
                average_clause_idle, average_clause_busy)
            clause_idle_no_task[config][cnf] = average_clause_idle_no_task / \
                average_clause_idle
            clause_idle_wating_l1[config][cnf] = average_clause_idle_wating_l1 / \
                average_clause_idle
            clause_idle_wating_l3[config][cnf] = average_clause_idle_wating_l3 / \
                average_clause_idle
            clause_idle_send_l1[config][cnf] = average_clause_idle_send_l1 / \
                average_clause_idle
            clause_idle_send_l3[config][cnf] = average_clause_idle_send_l3 / \
                average_clause_idle

            icnt_idle_cycle = data["icnt_statistics"]["idle_cycle"]
            icnt_busy_cycle = data["icnt_statistics"]["busy_cycle"]
            icnt_latency_count = data["icnt_statistics"]["average_latency"]["count"]
            icnt_latency_total = data["icnt_statistics"]["average_latency"]["total"]

            icnt_latency[config][cnf] = icnt_latency_total / icnt_latency_count
            icnt_idle_rate[config][cnf] = rate(
                icnt_idle_cycle, icnt_busy_cycle)

            pass

# %%


def print_data(data):
    print(data)
    real_data = all_stats[data]
    print("configs: ", end=" ")
    for config in tasks:
        print(config, end=" ")
    print()
    for cnf in cnfs:
        print(cnf, end=" ")
        for config in tasks:
            print(real_data[config][cnf], end=" ")
        print()


# %%
for data_to_print in all_stats:
    print_data(data_to_print)
    print()

# %%
