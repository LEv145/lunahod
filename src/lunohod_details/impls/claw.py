from lunohod_details.common import AngularServo90, AngularServo90Plus


class Claw():
    def __init__(
        self,
        active_servo: AngularServo90,
        rotation_servo: AngularServo90Plus,
    ) -> None:
        self._active_servo = active_servo
        self._rotation_servo = rotation_servo

    def activate(self) -> None:
        self._active_servo.max()

    def deactivate(self) -> None:
        self._active_servo.min()


    def set_angle(self, angle: int) -> None:
        self._rotation_servo.angle = angle

    def set_min_angle(self) -> None:
        self._rotation_servo.min()

    def set_mid_angle(self) -> None:
        self._rotation_servo.mid()

    def set_max_angle(self) -> None:
        self._rotation_servo.max()
