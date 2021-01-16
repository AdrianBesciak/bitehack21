from motor_driver import MotorDriver
from time import sleep
from arduino import Arduino
from guest import Guest


def recognize_user(rfid_reader, guests):
    while True:
        uuid = rfid_reader.get_rfid_value()
        for guest in guests:
            if uuid == guest.get_uuid():
                return guest


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arduino = Arduino('ttyACM0')

    guests = []
    guests.add(Guest('Kamil', 'Ptak', 'AD:6F:55:D9'))

    arrived_guest = recognize_user(rfid_reader=Arduino, guests=guests)

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
    arduino.close_connection()



