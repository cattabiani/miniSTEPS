from miniSTEPS.reaction import Reaction
from miniSTEPS.compartment import Compartment
from miniSTEPS.simulator import Simulator


r1 = Reaction("reac1", {"A": 2}, {"B": 1, "C": 1}, 1.2e12)
r2 = Reaction("reac2", {"B": 1, "C": 1}, {"A": 1}, 1.2e12)
r3 = Reaction("reac3", {}, {"A": 1}, 0.7)

c = Compartment("comp1", 3e-12, {"A": 1e6, "B": 1e6, "C": 1e6, "D": 1e6})
s = Simulator("sim", c, [r1, r2, r3])
s.run(1000)

s.records.plot()
