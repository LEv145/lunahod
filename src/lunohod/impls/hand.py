from lunohod.common_details import AngularServo90, AngularServo360


class Hand():
    def __init__(
        self,
        base_servo: AngularServo360,
        claw_servo_1: AngularServo90,
        claw_servo_2: AngularServo90,
    ):
        self._base_servo = base_servo
        self._claw_servo_1 = claw_servo_1
        self._claw_servo_2 = claw_servo_2


    def set_x_angle(self, angle: int) -> None:
        self._base_servo.angle = angle

    def set_x_min_angle(self) -> None:
        self._base_servo.min()

    def set_x_mid_angle(self) -> None:
        self._base_servo.mid()

    def set_x_max_angle(self) -> None:
        self._base_servo.max()


    def set_y_angle(self, angle: int) -> None:
        self._claw_servo_1.angle = angle
        self._claw_servo_2.angle = angle

    def set_y_min_angle(self) -> None:
        self._claw_servo_1.min()
        self._claw_servo_2.min()

    def set_y_mid_angle(self) -> None:
        self._claw_servo_1.mid()
        self._claw_servo_2.mid()

    def set_y_max_angle(self) -> None:
        self._claw_servo_1.max()
        self._claw_servo_2.max()
