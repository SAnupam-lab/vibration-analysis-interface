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
        self.max_spectrum = 20
        self.colors = ["#0099ff", "#ff9900", "#009933", "#990099"]
        self.maps = ["RMS", "Variance", "Peak-to-peak"]
        self.figure = None

    # Time features plot
    def plot_time_features(self, time_features):
        rows = len(time_features)
        cols = 1
        keys = list(time_features)
        fig = make_subplots(rows=rows, cols=cols, subplot_titles=tuple(self.maps))
        for i in range(rows):
            key = keys[i]
            fig.add_trace(go.Scatter(y=time_features[key], mode="lines", line=dict(color=self.colors[i])), row=i+1, col=1)
        fig.update_layout(autosize=True, showlegend=False)
        self.figure = fig.to_json()
        return fig

    # Spectrum plot
    def plot_spectrum(self, frequency_features):
        spectrum = frequency_features["spectrum"]
        bins = frequency_features["bins"]
        if len(spectrum) > self.max_spectrum:
            indexes = np.linspace(0, len(spectrum) - 1, self.max_spectrum, dtype="int")
            spectrum = spectrum[indexes]
        fig = go.Figure()
        y = np.zeros(spectrum.shape[1])
        for i in range(len(spectrum)):
            fig.add_trace(go.Scatter3d(x=bins, y=y, z=spectrum[i], mode='lines', line=dict(color=self.colors[-1])))
            y += 1
        fig.update_layout(autosize=True, showlegend=False,
        scene=dict(
            xaxis=dict(title="Frequency (Hz)", zeroline=False),
            yaxis=dict(title='Time (samples)', zeroline=False),
            zaxis=dict(title='Amplitude', zeroline=False),
            aspectmode='manual', 
            aspectratio=dict(x=1.0, y=1.2, z=0.6)))
        self.figure = fig.to_json()
        return fig

    # Figures generation
    def run(self, processing, figure):
        if figure == "time-features":
            self.plot_time_features(processing.time_features)
        elif figure == "spectrum":
            self.plot_spectrum(processing.frequency_features)
