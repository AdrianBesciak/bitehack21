from motor_driver import MotorDriver
from time import sleep
from arduino import Arduino
from guest import Guest
from time import time


def recognize_user(rfid_reader):
    print("start scanning")
    guests = Guest.get_guests()
    while True:
        uuid = rfid_reader.get_rfid_value()
        print("received uuid: ", uuid)
        for guest in guests:
            if uuid[0:11] == guest.get_uuid():
                return guest


def follow_line(sensors, left_motor, right_motor):
    print('Started line following')
    while True:
        print(time())
        line = sensors.get_line_sensors()
        print(time(), line)
        count = 0
        for letter in line:
            if letter == '1':
                count += 1
        if len(line) < 6:
            print('Otrzymano ', len(line), 'znakow od arduino')
            continue
        if count == 0 or count > 1:
            continue

        if line[0] == '1':
            left_motor.spin(0)
            right_motor.spin(100)

        elif line[1] == '1':
            left_motor.spin(40)
            right_motor.spin(100)
        elif line[2] == '1':
            left_motor.spin(80)
            right_motor.spin(100)
        elif line[3] == '1':
            left_motor.spin(100)
            right_motor.spin(80)
        elif line[4] == '1':
            left_motor.spin(100)
            right_motor.spin(40)
        elif line[5] == '1':
            left_motor.spin(100)
            right_motor.spin(0)
        else:
            left_motor.spin(20)
            right_motor.spin(20)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arduino = Arduino('ttyUSB0')

    print("scan rfid")
    arrived_guest = recognize_user(rfid_reader=arduino)

    left_motor = MotorDriver(13, 5, 6)
    right_motor = MotorDriver(12, 20, 16)
    follow_line(arduino, left_motor, right_motor)

    arduino.close_connection()

