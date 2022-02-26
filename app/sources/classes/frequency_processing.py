"""

Class: FrequencyProcessing

"""

# Importing packages and modules
from scipy.fft import fft, fftfreq
import numpy as np

# Frequency processing class
class FrequencyProcessing():

    # Constructor
    def __init__(self, sampling_frequency):
        self.sampling_frequency = sampling_frequency

    # Fast Fourier Transform (FFT)
    def fast_fourier_transform(self, samples):
        n = samples.shape[-1]
        spectrum = 2.0/n * np.abs(fft(samples)[:, 0:n//2])
        bins = fftfreq(n, self.sampling_frequency)[:n//2]
        return spectrum, bins

    # Frequency features calculation
    def run(self, samples):
        spectrum, bins = self.fast_fourier_transform(samples)
        self.features = {
            "spectrum": spectrum,
            "bins": bins
        }
    