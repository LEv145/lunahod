from gpiozero import Motor, PWMOutputDevice


class VNH3SP30Motor():
    def __init__(
        self,
        IN_A: int,
        IN_B: int,
        PWM: int,
        EN: int,
    ) -> None:
        self._motor = Motor(IN_A, IN_B, enable=EN, pwm=False)
        self._pwm = PWMOutputDevice(PWM)


    def set_speed(self, value: int) -> None:
        self._pwm.value = value

    def get_speed(self) -> int:
        return self._pwm.value


    def backward(self) -> None:
        self._motor.backward()

    def forward(self) -> None:
        self._motor.forward()

    def reverse(self) -> None:
        self._motor.reverse()


    def stop(self) -> None:
        self._motor.stop()
