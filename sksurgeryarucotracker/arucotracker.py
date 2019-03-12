#  -*- coding: utf-8 -*-

"""A class for straightforward tracking with an ARuCo
"""
from time import time
from numpy import full, nan, nditer
import cv2.aruco as aruco
from cv2 import VideoCapture

class ArUcoTracker:
    """
    Base class for communication with trackers.
    Ideally all surgery tracker classes will implement
    this interface
    """
    def __init__(self, configuration):
        """
        Initialises and Configures the ArUco detector

        :param configuration: A dictionary containing details of the tracker.

            video source: defaults to 0

            aruco dictionary: defaults to DICT_4X4_50

            marker size: defaults to 50 mm

            camera projection matrix: defaults to None

            camera distortion: defaults to None

        :raise Exception: ImportError
        """

        self._video_source = 0
        self._ar_dictionary_name = getattr (aruco, 'DICT_4X4_50')
        self._ar_dict = None
        self._marker_size = 50
        self._camera_projection_matrix = None
        self._camera_distortion = None
        self._estimate_pose_using_calibration = False
        self._state = None
        self._capture = VideoCapture()
        self._frame_number = 0

        if "video source" in configuration:
            self._video_source = configuration.get("video source")

        if "aruco dictionary" in configuration:
            dictionary_name = configuration.get("aruco dictionary")
            try:
                self._ar_dictionary_name = getattr (aruco, dictionary_name)
            except AttributeError:
                raise ImportError('Failed when trying to import {} from cv2.aruco. Check dictionary exists.'.format(dictionary_name))

        self._ar_dict = aruco.getPredefinedDictionary ( self._ar_dictionary_name )

        if "marker size" in configuration:
            self._marker_size = configuration.get("marker size")

        if "camera projection matrix" in configuration:
            self._camera_projection_matrix = configuration.get("camera projection matrix")

        if "camera distortion" in configuration:
            self._camera_distortion = configuration.get("camera distortion")

        self._estimate_pose_using_calibration = self._pose_estimation_ok()

        if self._capture.open(self._video_source):
            self._state = "ready"
        else:
            raise HardwareError ('Failed to open video source {}'.format(self._video_source))

    def _pose_estimation_ok(self):
        """Checks that the camera projection matrix and camera distortion
        matrices can be used to estimate pose"""
        if self._camera_projection_matrix != None:
            return True
        else:
            return False


    def close(self):
        """
        Closes the connection to the Tracker and
        deletes the tracker device.

        :raise Exception: ValueError
        """
        self._capture.release()
        del self._capture
        self._state = None

    def get_frame(self):
        """Gets a frame of tracking data from the Tracker device.

        :return: A NumPy array. One row per rigid body. The specific
        representation of the transform is left up to the derived class.
        :raise Exception: ValueError
        """
        if self._state != "tracking":
            raise ValueError ('Attempted to get frame, when not tracking')

        ret, frame = self._capture.read()

        marker_corners, marker_ids, _ = aruco.detectMarkers(frame, self._ar_dict)

        port_handles=[]
        time_stamps=[]
        frame_numbers=[]
        tracking_quality=[]

        timestamp = time()
        for marker in nditer(marker_ids):
            port_handles.append(marker.item())
            time_stamps.append(timestamp)
            frame_numbers.append(self._frame_number)
            tracking_quality.append(nan)

        self._frame_number += 1

        if self._estimate_pose_using_calibration:
            tracking = self._get_poses_with_calibration ( marker_corners )
        else:
            tracking = self._get_poses_without_calibration ( marker_corners )

        return port_handles, time_stamps, frame_numbers, tracking_quality, marker_ids, marker_corners

    def _get_poses_with_calibration ( self, marker_corners ):
        rvecs, tvecs, _ = \
            aruco.estimatePoseSingleMarkers(marker_corners,
                                                    self._marker_size,
                                                    self._camera_projection_mat,
                                                    self._camera_distortion)

    def _get_poses_without_calibration ( self, marker_corners ):
        for tracking in nditer ( marker_corners ):
            print (tracking)


    def get_tool_descriptions(self):
        """ Returns tool descriptions """
        return self._video_source

    def start_tracking(self):
        """
        Tells the tracking device to start tracking.
        :raise Exception: ValueError
        """
        if self._state == "ready":
            self._state = "tracking"
        else:
            raise ValueError ('Attempted to start tracking, when not ready')
    def stop_tracking(self):
        """
        Tells the tracking devices to stop tracking.
        :raise Exception: ValueError
        """
        if self._state == "tracking":
            self._state = "ready"
        else:
            raise ValueError ('Attempted to stop tracking, when not tracking')

