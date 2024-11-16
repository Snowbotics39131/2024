from PortMap24 import *
def drive_distance_or_time(distance: int, max_time=10000, then=Stop.HOLD):
    driveBase.straight(distance, then=then, wait=False)
    stop_watch = StopWatch()
    while not(driveBase.done()) and stop_watch.time() <= max_time:
        pass
    if not driveBase.done():
        hub.speaker.beep()
        print(f"Time limit of {max_time}ms exhausted while driving {distance}mm.")
        driveBase.stop()

if __name__ == '__main__':
    drive_distance_or_time(200, 3000)




#async def wood_chips(drive_base: DriveBase, distance: int, max_time=100, then=Stop.HOLD):
#    await drive_distance_or_time(drive_base, distance, max_time, then)