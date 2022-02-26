"""

Class: Visualization

"""

# Importing packages and modules
import plotly.graph_objects as go

# Visualization class
class Visualization:

    # Constructor
    def __init__(self):
        self.figures = {}

    # Time features plot
    def plot_time_features(self):
        fig = go.Figure()
        self.figures["time_features"] = fig.to_json()
        return fig

    # Spectrum plot
    def plot_spectrum(self):
        fig = go.Figure()
        self.figures["spectrum"] = fig.to_json()
        return fig

    # Figures generation
    def run(self, processing):
        self.plot_time_features()
        self.plot_spectrum()

