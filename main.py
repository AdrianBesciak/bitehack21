from motor_driver import MotorDriver
from time import sleep


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    left_motor = MotorDriver(12, 20, 16)
    right_motor = MotorDriver(13, 5, 6)
    print('start running motor')
    while True:
        left_motor.spin(50)
        right_motor.spin(-100)
        sleep(2)
        left_motor.spin(100)
        right_motor.spin(100)
        sleep(1)
        left_motor.spin(0)
        right_motor.spin(100)
        sleep(0.5)


    print('stop running motor')


