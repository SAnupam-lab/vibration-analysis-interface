"""

Class: DAO

"""

# Importing packages and modules
import pickle
import json

# Data access class
class DAO():

    # Constructor
    def __init__(self, dataset_id, channel):
        self.dataset_id = dataset_id
        self.channel = channel
        self.dataset_path = f"./datasets/{dataset_id}/{channel}.pickle"
        self.info_path = f"./datasets/{dataset_id}/info.json"

    # Sampling frequency reading
    def read_sampling_frequency(self):
        with open(self.info_path, "rb") as file:
            data = json.load(file)
        sampling_frequency = data["sampling_frequency"]
        return sampling_frequency

    # Samples reading
    def read_samples(self, slice_start, slice_end):
        with open(self.dataset_path, "rb") as file:
            data = pickle.load(file)
        start = int(len(data) * (slice_start/100))
        end = int(len(data) * (slice_end/100))
        samples = data[start:end]
        return samples
            