import sys
import platform

if platform.system() == "Windows":
    print("Windows")
else:
    rpi = True
    import driver

argument1 = sys.argv[1]  # component identifier 1 = elevator...
argument2 = sys.argv[2]  # command

stepper = driver.Stepper()

if argument1 == "1":
    # commands with elevator
    if argument2 == "0":  # zero elevator
        stepper.calibrate()

    elif argument2 == "1":  # moveUp function
        argument3 = sys.argv[3]  # steps
        spd = sys.argv[4]  # speed
        stepper.turn(1, argument3, spd)

    elif argument2 == "2":  # moveDown function
        argument3 = sys.argv[3]  # steps
        spd = sys.argv[4]  # speed
        stepper.turn(0, argument3, spd)

