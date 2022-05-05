import math
import random
import bisect


class DirectEngine:
    def __init__(self, simulator):
        self.reactions = list(simulator.reactions.keys())
        self.rates = [0] * len(self.reactions)
        self.partial_sums = [0] * len(self.reactions)
        self.update_rates(simulator)

    def update_rates(self, simulator):
        self.rates = [
            simulator.reactions[r].rate(simulator.compartment.concentrations())
            for r in self.reactions
        ]
        self.partial_sums = self.rates
        self.partial_sums = [
            i + (self.partial_sums[idx - 1] if idx != 0 else 0)
            for idx, i in enumerate(self.partial_sums)
        ]

    def update_molecule_counts(self, simulator, reaction_name):
        reaction = simulator.reactions[reaction_name]
        reaction.update_molecule_counts(simulator)

    def advance(self, simulator, end_time):
        sum = self.partial_sums[-1]

        r1 = random.uniform(0, 1)
        delta_t = math.log(1 / r1) / sum

        if delta_t + simulator.current_time > end_time:
            simulator.current_time = end_time
            return

        r2 = random.uniform(0, sum)

        ir = bisect.bisect_left(self.partial_sums, r2)
        reaction = self.reactions[ir]

        self.update_molecule_counts(simulator, reaction)
        self.update_rates(simulator)

        simulator.current_time += delta_t

        return reaction

    def __str__(self):
        res = f"DirectEngine\n"
        z = [i for i in zip(self.reactions, self.rates)]
        res += f"Reaction/rates: " + z.__str__() + "\n"
        res += f"Partial sums: " + self.partial_sums.__str__() + "\n"
        return res
