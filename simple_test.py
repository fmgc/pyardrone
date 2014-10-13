import libardrone
import time

print 1
drone = libardrone.ARDrone()
time.sleep(0.1)
print 2
drone.takeoff()
time.sleep(0.1)
print 3
drone.hover()
time.sleep(0.1)
print 4
drone.land()
print 5