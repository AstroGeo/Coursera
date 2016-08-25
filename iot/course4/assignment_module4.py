import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(21,GPIO.IN)



while True:
	 input = GPIO.input(21)
	 if input == False:
	        GPIO.output(13, True)
        	time.sleep(0.1)
        	GPIO.output(13, False)
        	time.sleep(0.1)
	 elif input == True:
		GPIO.output(13, True)
