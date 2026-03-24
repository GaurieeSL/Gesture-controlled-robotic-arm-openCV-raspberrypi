import RPi.GPIO as GPIO
import time

# Use GPIO numbering
GPIO.setmode(GPIO.BCM)

# Servo pin
servo_pin = 18

# Setup pin
GPIO.setup(servo_pin, GPIO.OUT)

# PWM setup (50Hz for servo)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def set_angle(angle):
    duty = 2 + (angle / 18)
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        print("Moving to 0°")
        set_angle(0)
        time.sleep(2)

        print("Moving to 90°")
        set_angle(90)
        time.sleep(2)

        print("Moving to 180°")
        set_angle(180)
        time.sleep(2)

except KeyboardInterrupt:
    print("Stopped by user")

pwm.stop()
GPIO.cleanup()
