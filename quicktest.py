#! /usr/bin/python3.6

from sksurgeryarucotracker.arucotracker import ArUcoTracker

config1={'video source' : 'data/output.avi'}

print ("no config")
tracker=ArUcoTracker(config1)
tracker.start_tracking()
print (tracker.get_tool_descriptions())
for i in range (10):
    phs, tss , fns, qls, ids, corners = tracker.get_frame()
    print (tss, fns, phs, qls)
    print (corners)

tracker.stop_tracking()
tracker.close()
del tracker

