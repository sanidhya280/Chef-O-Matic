import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
motor_rice_release1 = 18
motor_rice_release2 = 22

rotate_slider_pin1 = 21
rotate_slider_pin2 = 19
rotate_strainer_pin1 = 33
rotate_strainer_pin2 = 35


GPIO.setup(motor_rice_release1, GPIO.OUT)
GPIO.setup(motor_rice_release2, GPIO.OUT)
GPIO.setup(rotate_slider_pin1, GPIO.OUT)
GPIO.setup(rotate_slider_pin2, GPIO.OUT)
GPIO.setup(rotate_strainer_pin1, GPIO.OUT)
GPIO.setup(rotate_strainer_pin2, GPIO.OUT)


def Release_Rice(n):
	for index in range(n):
		gate_riceStorage_open()
		gate_riceStorage_close()

def wash_rice():
	sprinkler_on()
	rotate_slider()
	rotate_strainer()


def gate_riceStorage_open():
	GPIO.output(motor_rice_release1, GPIO.HIGH)
	GPIO.output(motor_rice_release2, GPIO.LOW)
	time.sleep(10)

def gate_riceStorage_close():
	GPIO.output(motor_rice_release1, GPIO.LOW)
	GPIO.output(motor_rice_release2, GPIO.HIGH)
	time.sleep(10)

def sprinkler_on():
	GPIO.output(motor_rice_release1, GPIO.LOW)
	GPIO.output(motor_rice_release2, GPIO.HIGH)
	time.sleep(10)


def rotate_slider():
	GPIO.output(rotate_slider_pin1, GPIO.HIGH)
	GPIO.output(rotate_slider_pin2, GPIO.LOW)
	time.sleep(10)
	GPIO.output(rotate_slider_pin1, GPIO.LOW)
	GPIO.output(rotate_slider_pin2, GPIO.HIGH)
	time.sleep(10)

def rotate_strainer():
	GPIO.output(rotate_strainer_pin1, GPIO.HIGH)
	GPIO.output(rotate_strainer_pin2, GPIO.LOW)
	time.sleep(10)
	GPIO.output(rotate_strainer_pin1, GPIO.LOW)
	GPIO.output(rotate_strainer_pin2, GPIO.HIGH)
	time.sleep(10)
	
def main():
	print ("hello")
	Release_Rice(5)
	wash_rice()


if __name__ == '__main__':
	main()