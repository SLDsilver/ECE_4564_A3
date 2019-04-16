import RPi.GPIO as GPIO

class LED:
    def __init__(self):
        self.LED_RED = 17
        self.LED_GREEN = 27
        self.LED_BLUE = 22
        self.status = 'off'
        self.color = 'red'
        self.intensity = 0

        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.LED_RED, GPIO.OUT)
        GPIO.setup(self.LED_GREEN, GPIO.OUT)
        GPIO.setup(self.LED_BLUE, GPIO.OUT)

        self.p_red = GPIO.PWM(self.LED_RED, 1000)
        self.p_green = GPIO.PWM(self.LED_GREEN, 1000)
        self.p_blue = GPIO.PWM(self.LED_BLUE, 1000)
        self.p_red.start(0)
        self.p_green.start(0)
        self.p_blue.start(0)

    def set_status(self, s):
        if s == 'on' or s == 'off':
            self.status = s

    def set_color(self, c):
        if c == 'red' or c == 'green' or c == 'blue':
            self.color = c

    def set_intensity(self, i):
        if i >= 0 and i <= 100:
            self.intensity = i

    def update(self):
        self.p_red.ChangeDutyCycle(0)
        self.p_green.ChangeDutyCycle(0)
        self.p_blue.ChangeDutyCycle(0)
        if self.status == 'on':
            if self.color == 'red':
                self.p_red.ChangeDutyCycle(self.intensity)
            elif self.color == 'green':
                self.p_green.ChangeDutyCycle(self.intensity)
            elif self.color == 'blue':
                self.p_blue.ChangeDutyCycle(self.intensity)
