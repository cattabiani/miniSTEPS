from miniSTEPS.direct_engine import DirectEngine
from miniSTEPS.record import Record

import pandas as pd


class Simulator:
    def __init__(self, name, compartment, reactions, records=None):
        self.name = name
        self.compartment = compartment
        self.reactions = {reaction.name: reaction for reaction in reactions}

        # self.records = {i : [] for i in records} if records is not None else {i : [] for i in
        #                                                                       self.compartment.molecule_counts.keys()}
        # self.records['t'] = []

        self.records = Record(
            records
            if records is not None
            else list(self.compartment.molecule_counts.keys()),
            list(self.reactions.keys()),
        )

        self.current_time = 0.0
        self.engine = DirectEngine(self)

    def run(self, end_time):
        if len(self.reactions) == 0:
            self.current_time = self.end_time
            return

        self.engine.__init__(self)
        self.records.record_data_point(
            self.compartment.molecule_counts, self.current_time
        )
        while self.current_time < end_time:
            reaction = self.engine.advance(self, end_time)
            self.records.record_reaction(reaction)
            self.records.record_data_point(
                self.compartment.molecule_counts, self.current_time
            )
            print(f"Current time: {self.current_time}")
