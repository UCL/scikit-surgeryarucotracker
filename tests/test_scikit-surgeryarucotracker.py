# coding=utf-8

"""scikit-surgerytracker tests"""

from sksurgeryarucotracker.arucotracker import ArUcoTracker
from numpy import array, float32
import pytest

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
                                                 [0.0, 0.0, 1.0]], dtype = float32),
             'marker size' : 50,
             'camera distortion' : array ([0.1, 0.1, 0.0, 0.0, 0.0], dtype = float32)
            }

    tracker=ArUcoTracker(config1)
    tracker.start_tracking()
    for _ in range (10):
        port_handles, timestamps , framenumbers, tracking, quality = tracker.get_frame()

    tracker.stop_tracking()
    tracker.close()

def test_throw_on_bad_source():
    config={'video source' : 'data/nofile.xxxx',
        'aruco dictionary' : 'DICT_6X6_250'}

    with pytest.raises(OSError):
        tracker=ArUcoTracker(config)

def test_throw_on_bad_calibration():
    config={'video source' : 'data/output.avi',
            'camera projection matrix' : array([[560.0, 0.0],
                                                 [0.0, 560.0],
                                                 [0.0, 0.0]], dtype = float32)
            }

    with pytest.raises(ValueError):
        tracker=ArUcoTracker(config)


def test_invalid_dictionary():
    config={'video source' : 'data/12markers.png',
        'aruco dictionary' : 'DICT_7X6_250'}

    with pytest.raises(ImportError):
        tracker=ArUcoTracker(config)

def test_throw_when_get_frame_not_tracking():
    config={'video source' : 'data/output.avi'}
    
    tracker=ArUcoTracker(config)
    with pytest.raises(ValueError):
        port_handles, timestamps , framenumbers, tracking, quality = tracker.get_frame()
    tracker.close()

def test_get_tool_descriptions():
    config={'video source' : 'data/output.avi'}
    
    tracker=ArUcoTracker(config)
    tracker.get_tool_descriptions();
    tracker.close()

def test_start_tracking_throws_value_error():
    config={'video source' : 'data/12markers.png'}
    tracker=ArUcoTracker(config)
    tracker.start_tracking()
    
    with pytest.raises(ValueError):
        tracker.start_tracking()

    tracker.close()


def test_stop_tracking_throws_value_error():
    config={'video source' : 'data/12markers.png'}
    tracker=ArUcoTracker(config)
    
    with pytest.raises(ValueError):
        tracker.stop_tracking()

    tracker.close()


