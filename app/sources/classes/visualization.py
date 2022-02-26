"""

Class: Visualization

"""

# Importing packages and modules
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.io as pio
pio.renderers.default = "browser"

# Visualization class
class Visualization:

    # Constructor
    def __init__(self):
        self.figures = {}

    # Time features plot
    def plot_time_features(self, time_features):
        rows = len(time_features)
        cols = 1
        keys = list(time_features)
        fig = make_subplots(rows=rows, cols=cols, subplot_titles=tuple(keys))
        for i in range(rows):
            key = keys[i]
            fig.add_trace(go.Scatter(y=time_features[key], mode="lines"), row=i+1, col=1)
        self.figures["time_features"] = fig.to_json()
        return fig

    # Spectrum plot
    def plot_spectrum(self, frequency_features):
        spectrum = frequency_features["spectrum"]
        bins = frequency_features["bins"]
        fig = go.Figure()
        y = np.zeros(spectrum.shape[1])
        for i in range(len(spectrum)):
            fig.add_trace(go.Scatter3d(x=bins, y=y, z=spectrum[i], mode='lines'))
            y += 1
        self.figures["spectrum"] = fig.to_json()
        return fig

    # Figures generation
    def run(self, processing):
        self.plot_time_features(processing.time_features)
        self.plot_spectrum(processing.frequency_features)