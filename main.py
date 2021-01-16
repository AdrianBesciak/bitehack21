from motor_driver import MotorDriver
from time import sleep
from arduino import Arduino
from guest import Guest


def recognize_user(rfid_reader, guests):
    print("start scanning")
    while True:
        uuid = rfid_reader.get_rfid_value()
        print("received uuid: ", uuid)
        for guest in guests:
            if uuid[0:11] == guest.get_uuid():
                return guest


def follow_line(sensors, left_motor, right_motor):
    print('Started line following')
    while True:
        line = sensors.get_line_sensors()
        print(line + 'type: ' + str(type(line)))
        left_motor.spin(50)
        right_motor.spin(50)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arduino = Arduino('ttyUSB1')

    guests = [Guest('Kamil', 'Ptak', 'AD:6F:55:D9')]
    print("scan rfid")
    arrived_guest = recognize_user(rfid_reader=arduino, guests=guests)

    left_motor = MotorDriver(12, 20, 16)
    right_motor = MotorDriver(13, 5, 6)
    follow_line(arduino, left_motor, right_motor)
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
    arduino.close_connection()



