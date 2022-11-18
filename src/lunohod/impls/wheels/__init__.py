from lunohod.common_details import AngularServo90
from .VNH3SP30_motor import VNH3SP30Motor


class Wheels():
    def __init__(self, motor: VNH3SP30Motor, servo: AngularServo90) -> None:
        self._motor = motor
        self._servo = servo


    def set_min_angle(self) -> None:
        self._servo.min()

    def set_mid_angle(self) -> None:
        self._servo.mid()

    def set_max_angle(self) -> None:
        self._servo.max()


    def set_angle(self, angle: int) -> None:
        self._servo.angle = angle

    def set_speed(self, value: int) -> None:
        self._motor.set_speed(value)

    def get_speed(self) -> int:
        return self._motor.get_speed()


    def backward(self) -> None:
        self._motor.backward()

    def forward(self) -> None:
        self._motor.forward()

    def reverse(self) -> None:
        self._motor.reverse()


    def stop(self) -> None:
        self._motor.stop()
