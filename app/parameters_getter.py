from app.ai_model import AIModel
import json
import pandas as pd


class ParametersGetter:
    def __init__(self, ai_model):
        self.ai_model = ai_model

    def __get_data(self):
        keys = ["x", "y", "width", "height"]
        self.df = pd.DataFrame([
            {key: pred[key] for key in keys}  # pick only x, y, width, height
            for pred in self.ai_model["predictions"]  # loop through each prediction dict
        ])



    def __average_x_pos(self):
        avg_x = self.df['x'].mean()
        return avg_x

    def __average_y_pos(self):
        avg_y = self.df['y'].mean()
        return avg_y

    def __average_radius(self):
        avg_width = self.df['width'].mean()
        avg_height = self.df['height'].mean()
        r = min(avg_width, avg_height) / 2
        return r

    def __ripple_counts(self):
        return self.df.shape[0]

    def get_params(self):
        self.__get_data()
        avg_x_pos = self.__average_x_pos()
        avg_y_pos = self.__average_y_pos()
        avg_radius = self.__average_radius()
        ripple_counts = self.__ripple_counts()
        print([avg_x_pos, avg_y_pos, avg_radius, ripple_counts])
        return [avg_x_pos, avg_y_pos, avg_radius, ripple_counts]

