class ReactionError(Exception):
    pass


class Reaction:
    def __init__(self, name, reactants, products, k):
        self.name = name
        self.reactants = reactants  # {"A":2} molecule: A, stochiometry: 2
        self.products = products  # {"A":2} molecule: A, stochiometry: 2
        self.k = k

    def rate(self, concentrations):
        ans = self.k
        for i in concentrations.keys() & self.reactants.keys():
            ans *= concentrations[i] ** self.reactants[i]

        return ans

    def update_molecule_counts(self, simulator):
        for k, v in self.reactants.items():
            simulator.compartment.molecule_counts[k] -= v
        for k, v in self.products.items():
            simulator.compartment.molecule_counts[k] += v

    def __str__(self):
        res = f"Reaction: {self.name} (k: {self.k})\n"
        res += " + ".join(
            [f"{v if v != 1 else ''}{k}" for k, v in self.reactants.items()]
        )
        res += f" -> "
        res += " + ".join(
            [f"{v if v != 1 else ''}{k}" for k, v in self.products.items()]
        )

        return res
