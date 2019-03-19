# coding=utf-8

"""scikit-surgerytracker tests"""

from sksurgeryarucotracker.arucotracker import ArUcoTracker
from numpy import array, float32

def test_on_video_with_single_tag():
    config={'video source' : 'data/output.avi'}
    
    tracker=ArUcoTracker(config)
    tracker.start_tracking()
    for _ in range (10):
        port_handles, timestamps , framenumbers, tracking, quality = tracker.get_frame()

    tracker.stop_tracking()
    tracker.close()

def test_on_static_muti_tag():
    config={'video source' : 'data/12markers.png',
        'aruco dictionary' : 'DICT_6X6_250'}

    tracker=ArUcoTracker(config)
    tracker.start_tracking()

    port_handles, timestamps , framenumbers, tracking, quality = tracker.get_frame()

    tracker.stop_tracking()
    tracker.close()

def test_on_video_with_calib():
    config1={'video source' : 'data/output.avi',
        'camera projection matrix' : array([[560.0, 0.0, 320.0],
                                      [0.0, 560.0, 240.0],
                                      [0.0, 0.0, 1.0]], dtype = float32)}

    tracker=ArUcoTracker(config1)
    tracker.start_tracking()
    for _ in range (10):
        port_handles, timestamps , framenumbers, tracking, quality = tracker.get_frame()

    tracker.stop_tracking()
    tracker.close()

