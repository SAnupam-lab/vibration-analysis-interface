"""

Class: TimeProcessing

"""

# Importing packages and modules
import numpy as np

# Time processing class
class TimeProcessing():

    # Constructor method
    def __init__(self):
        pass

    # Root mean square
    def root_mean_square(self, samples):
        rms = np.sqrt(np.mean(np.square(samples), axis=1))
        return rms

    # Variance
    def variance(self, samples):
        var = np.mean(np.square(samples - np.mean(samples)), axis=1)
        return var

    # Peak-to-peak
    def peak_to_peak(self, samples):
        pkpk = np.max(samples, axis=1) - np.min(samples, axis=1)
        return pkpk

    # Time features calculation
    def run(self, samples):
        rms = self.root_mean_square(samples)
        var = self.variance(samples)
        pkpk = self.peak_to_peak(samples)
        self.features = {
            "rms": rms,
            "var": var,
            "pkpk": pkpk
        }




