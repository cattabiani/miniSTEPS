import scipy.constants as spc


class Compartment:
    def __init__(self, name, volume, molecule_counts={}):
        self.name = name
        self.volume = volume
        self.molecule_counts = molecule_counts

    def concentrations(self):
        return {k: v / (spc.N_A * self.volume) for k, v in self.molecule_counts.items()}

    def __str__(self):
        res = f"Compartment: {self.name} (volume: {self.volume})\n"
        res += self.molecule_counts.__str__()
        return res
