import sys
import platform
import time

#if platform.system() == "Windows":
#    print("Windows")
#else:
rpi = True
import driver
import solenoid

argument1 = sys.argv[1]  # component identifier 1 = elevator...
argument2 = sys.argv[2]  # command

stepper = driver.Stepper(
        dir=23,
        step=24,
        enable=27,
        zero=26,
    )

if argument1 == "1":
    stepper.enableMotor()
    # commands with elevator
    if argument2 == "0":  # zero elevator
        stepper.calibrate()

    elif argument2 == "1":  # moveUp function
        argument3 = sys.argv[3]  # steps
        spd = sys.argv[4]  # speed
        stepper.turn(1, int(argument3), int(spd))

    elif argument2 == "2":  # moveDown function
        argument3 = sys.argv[3]  # steps
        spd = sys.argv[4]  # speed
        stepper.turn(0, int(argument3), int(spd))

    elif argument2 == "3":  #Disable motor
        stepper.disableMotor()
        print("motor disabled")

    elif argument2 == "4":  #Enable motor
        print("motor enabled")
    #stepper.disableMotor()
elif argument1 == "2":
    n = int(argument2)
    solenoid.launch(n) #3 = bottom left
elif argument1 == "3":
    #test protocol
    stepper.enableMotor()

    stepper.calibrate()

    stepper.turn(1, 50, 400)
    solenoid.launch(3)

    time.sleep(3.0)
    stepper.calibrate()
    stepper.turn(1, 2420, 400)
    time.sleep(5.0)
    stepper.disableMotor()

