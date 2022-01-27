from machine import Pin, PWM

"""
Copyleft (C) Alexandria Pettit, GNU GPLv3
A Servo library providing easier generic servo support, as well as servo support for some specific models.
Loosely based on: https://github.com/sandbo00/picoservo
"""

# These are generic values that will work for many servos, but may need to be overridden for specific subclasses

# Generic minimum duty value
_DEFAULT_DUTY_MIN = 2500
# Generic maximum duty value
_DEFAULT_DUTY_MAX = 7500
# Generic PWM frequency
_DEFAULT_PWM_FREQ = 50


class BaseServo:
    """ BaseServo -- Base class for Servos
    """

    duty_min: int  # minimum duty value
    duty_max: int  # maximum duty value
    duty_diff: int  # difference between minimum and maximum values
    pos: float  # servo position between 0 and 1
    pin_num: int  # integer representing pin
    pwm: PWM  # PWM object
    pin: Pin  # Pin object

    def __init__(self, pin_num: int,
                 duty_min: int = _DEFAULT_DUTY_MIN,
                 duty_max: int = _DEFAULT_DUTY_MAX,
                 pwm_freq: int = _DEFAULT_PWM_FREQ):
        """ Creates a new Servo object
        :param pin_num: Pin int number, or Pin/PWM object
        :param duty_min: Minimum duty value of servo
        :param duty_max: Maximum duty value of servo
        """

        self.set_pin(pin_num, pwm_freq)
        self.duty_min = duty_min
        self.duty_max = duty_max
        self.duty_diff = self.duty_max - self.duty_min

    def deinit(self) -> None:
        """ Disables the PWM output
        """
        self.pwm.deinit()

    def set_pin(self, pin_num: int, pwm_freq: int) -> None:
        self.pin_num = pin_num
        self.pin = Pin(pin_num, Pin.OUT)
        self.pwm = PWM(self.pin)
        self.pwm.freq(pwm_freq)

    def set_pos(self, pos: float) -> None:
        """ Moves the servo to a given position
        :param pos: Target position (between 0 and 1, inclusive)
        """
        # Sanity check
        if pos > 1:
            pos = 1
        elif pos < 0:
            pos = 0

        # Calculate duty value by scaling diff and adding minimum value
        duty = int(pos * self.duty_diff + self.duty_min)
        # Ship it off to lower abstraction layer
        # This will send this duty cycle continuously until we send another update
        self.pwm.duty_u16(duty)

    def set_pos_pcnt(self, pos: float) -> None:
        """ Moves the servo to a given position
        :param pos: Target position (between 0 and 100, inclusive)
        """
        # Scale pos against 100
        self.set_pos(pos / 100)

    def set_pos_to_middle(self) -> None:
        """ Moves the servo to the middle position
        """
        self.set_pos(0.5)

    def set_pos_to_beginning(self) -> None:
        """ Moves the servo to the starting position
        """
        self.set_pos(0)

    def set_pos_to_end(self) -> None:
        """ Moves the servo to the end position
        """
        self.set_pos(1)

    def off(self) -> None:
        """ Turn off motor, allowing it to spin/move freely
        """
        self.pwm.duty_u16(0)


class LinearServo(BaseServo):
    linear_range_mm: float

    def __init__(self, pin: int,
                 linear_range_mm: float,
                 duty_min: int = _DEFAULT_DUTY_MIN,
                 duty_max: int = _DEFAULT_DUTY_MAX,
                 pwm_freq: int = _DEFAULT_PWM_FREQ):
        self.linear_range_mm = linear_range_mm
        # can override min, max, or freq here
        super().__init__(pin, duty_min, duty_max, pwm_freq)

    def set_pos_mm(self, pos_mm: float) -> None:
        """ Set position in millimeters
        :param pos_mm: Position in millimeters
        """
        self.set_pos(pos_mm / self.linear_range_mm)


class LinearMicroServo(LinearServo):
    """ A linear microservo my wife bought. TODO: measure servo and set linear range correctly
    """
    linear_range_mm = 2
