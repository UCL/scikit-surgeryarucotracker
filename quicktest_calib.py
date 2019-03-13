#! /usr/bin/python3.6

from sksurgeryarucotracker.arucotracker import ArUcoTracker
from numpy import array, float32

config1={'video source' : 'data/output.avi',
        'camera projection matrix' : array([[560.0, 0.0, 320.0],
                                      [0.0, 560.0, 240.0],
                                      [0.0, 0.0, 1.0]], dtype = float32)

        }

tracker=ArUcoTracker(config1)
tracker.start_tracking()
print (tracker.get_tool_descriptions())
for i in range (10):
    phs, tss , fns, tracking, qls = tracker.get_frame()
    print (phs, tss, fns,tracking, qls)

tracker.stop_tracking()
tracker.close()
del tracker

