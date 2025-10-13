#========== HEADER ===================================================================
"""
Document: parameters_getter.py
Function: Module for getting the needed parameters for encryption.
Author: PURA, Joshua Elijah L.
Date Created: October 6, 2025
Date Updated: October 13, 2025
Version: 0.0.2
"""
#======================================================================================

#============ LIBRARIES ===============================================================
import pandas as pd
#======================================================================================

#============ CLASS ===================================================================
class ParametersGetter:
    def __init__(self, ai_model):
        self.ai_model = ai_model

    def __get_data(self):
        """
        Function: __get_data
        Description: This private function process the data from the ai_model
                     in a more presentable and processable format using pandas
        Arguments:
            none.
        Returns:
            none.
        Raises:
            none
        """
        keys = ["x", "y", "width", "height"]
        self.df = pd.DataFrame([
            {key: pred[key] for key in keys}  # pick only x, y, width, height
            for pred in self.ai_model["predictions"]  # loop through each prediction dict
        ])



    def __average_x_pos(self):
        """
        Function: __average_x_pos
        Description: This private function gets the average of the X axis position
                     of all the detected rain ripple in the model.
        Arguments:
            none.
        Returns:
            avg_x (float): The average X axis position of the detected rain ripple
        Raises:
            none
        """
        avg_x = self.df['x'].mean()
        return avg_x

    def __average_y_pos(self):
        """
        Function: __average_y_pos
        Description: This private function gets the average of the Y axis position
                     of all the detected rain ripple in the model.
        Arguments:
            none.
        Returns:
            avg_x (float): The average Y axis position of the detected rain ripple
        Raises:
            none
        """
        avg_y = self.df['y'].mean()
        return avg_y

    def __average_radius(self):
        """
        Function: __average_x_pos
        Description: This private function gets the average radius of the detected
                     rain ripple.
        Arguments:
            none.
        Returns:
            r (float): The average radius of the detected rain ripple
        Raises:
            none
        """
        avg_width = self.df['width'].mean()
        avg_height = self.df['height'].mean()
        r = min(avg_width, avg_height) / 2
        return r

    def __ripple_counts(self):
        """
        Function: __ripple_counts
        Description: This private function gets total count of the rain ripple detected
                     in the AI model.
        Arguments:
            none.
        Returns:
            self.df.shape[0]: The total count of the rain ripple detected
        Raises:
            none
        """
        return self.df.shape[0]

    def get_params(self):
        """
        Function: get_params
        Description: This public function is responsible for serving the needed parameters
                     in a list format.
        Arguments:
            none.
        Returns:
            (list): A list containing all the needed parameters for the encryption
        Raises:
            none
        """
        self.__get_data()
        avg_x_pos = self.__average_x_pos()
        avg_y_pos = self.__average_y_pos()
        avg_radius = self.__average_radius()
        ripple_counts = self.__ripple_counts()
        print([avg_x_pos, avg_y_pos, avg_radius, ripple_counts])
        return [avg_x_pos, avg_y_pos, avg_radius, ripple_counts]

#============= END OF SOURCE CODE =================================================