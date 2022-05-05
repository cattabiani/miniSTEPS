import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


class Record:
    def __init__(self, traces, reactions):
        self.traces = {i: [] for i in traces}
        self.traces["t"] = []
        self.reactions = {i: 0 for i in reactions}

    def record_data_point(self, molecule_counts, current_time):
        self.traces["t"].append(current_time)

        for i in set(self.traces.keys()) & set(molecule_counts.keys()):
            self.traces[i].append(molecule_counts[i])

    def record_reaction(self, reaction):
        if reaction:
            self.reactions[reaction] += 1

    def plot(self):
        fig, ax = plt.subplots(2, 1)

        df = pd.DataFrame(self.traces)
        df.plot("t", ax=ax[0])

        x = list(self.reactions.keys())
        y = [self.reactions[i] for i in x]
        ax[1].plot(y, "o")
        plt.sca(ax[1])
        plt.xticks(range(len(x)), x)
        plt.ylim([0, None])

        fig.tight_layout()
        plt.show()
