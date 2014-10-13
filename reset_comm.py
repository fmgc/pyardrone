import libardrone
import time

drone = libardrone.ARDrone()

drone.takeoff()
drone.hover()
drone.land()
drone.halt()