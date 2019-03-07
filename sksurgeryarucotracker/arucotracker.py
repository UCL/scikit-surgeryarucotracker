#  -*- coding: utf-8 -*-

"""A class for straightforward tracking with an ARuCo 
"""
from time import time
from numpy import full, nan
import cv2.aruco as aruco

class ARuCoTracker:
    """
    Base class for communication with trackers.
    Ideally all surgery tracker classes will implement
    this interface
    """
    def __init__(self):
        self._video_source = None
        self._aruco_dictionary = aruco.DICT_4X4_50
        self._marker_size = 50
        self._camera_projection_matrix = None
        self._camera_distortion = None
        self._estimate_pose = False
        self._state = None

    def connect(self, configuration):
        """
        Configures the ARuCO detector

        :param configuration: A dictionary containing details of the tracker, 
        will be device specific, for example:

            aruco dictionary: defaults to DICT_4X4_50

            marker size: defaults to 50 mm

            camera projection matrix: defaults to None

            camera distortion: defaults to None

        :raise Exception: 
        """
        if "aruco dictionary" in configuration:
            dictionary_name = self._aruco_dictionary
            from cv2.aruco import dictionary_name
            #try:
            #ex
            #self._aruco_dictionary = configuration.get("aruco dictionary")
        


    def close(self):
        """
        Closes the connection to the Tracker and
        deletes the tracker device.

        :raise Exception: ValueError
        """
        pass

    def get_frame(self):
        """Gets a frame of tracking data from the Tracker device.

        :return: A NumPy array. One row per rigid body. The specific 
        representation of the transform is left up to the derived class.
        """
        pass

    def get_tool_descriptions(self):
        """ Returns tool descriptions """
        pass
    def start_tracking(self):
        """
        Tells the tracking device to start tracking.
        :raise Exception: ValueError
        """
        pass
    def stop_tracking(self):
        """
        Tells the tracking devices to stop tracking.
        :raise Exception: ValueError
        """
        pass
