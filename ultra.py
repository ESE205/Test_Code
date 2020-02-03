import RPi.GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 15


def ultrasonic_init(Trigger, Echo):
    # set up the input and output pins
    GPIO.setup(Trigger, GPIO.OUT)
    GPIO.output(Trigger, False)
    GPIO.setup(Echo, GPIO.IN)
    # let the sensor initialize
    time.sleep(0.5)


def ultrasonic_read(Trigger, Echo):
    # trigger a reading
    GPIO.output(Trigger, True)
    time.sleep(0.00001)
    GPIO.output(Trigger, False)

    # find the start and end of the ultrasonic pulse
    while GPIO.input(Echo) == 0:
        start_time = time.time()
    while GPIO.input(Echo) == 1:
        end_time = time.time()

    # Speed of sound 34300 cm/sec
    total_distance = (end_time - start_time) * 34300
    # Divide by 2, account for return trip for signal
    return round(total_distance / 2, 1)


ultrasonic_init(TRIG, ECHO)

while True:
    print("=== Ultrasonic Sensor ===")
    print(ultrasonic_read(TRIG, ECHO))
    time.sleep(0.5)
