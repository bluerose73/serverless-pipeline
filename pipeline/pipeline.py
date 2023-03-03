# Quick Start:
#
# from pipeline import pipeline
#
# pipeline.enter_stage(0)
# do something
# pipeline.exit_stage(0)
#
# pipeline.enter_stage(1)
# do something
# pipeline.exit_stage(1)

from threading import Semaphore
import json

class Pipeline:
    def __init__(self, capacity_list) -> None:
        self.capacity_list = capacity_list
        self.sema_list = []
        for capacity in self.capacity_list:
            self.sema_list.append(Semaphore(capacity))

    def enter_stage(self, id):
        self.sema_list[id].acquire()

    def exit_stage(self, id):
        self.sema_list[id].release()

with open("pipeline_config.json") as config_file:
    config = json.load(config_file)

pipeline = Pipeline(**config)