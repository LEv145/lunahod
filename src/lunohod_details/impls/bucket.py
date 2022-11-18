from lunohod_details.common import AngularServo90


class Bucket():
    def __init__(self, active_servo: AngularServo90) -> None:
        self._active_servo = active_servo


    def activate(self) -> None:
        self._active_servo.min()

    def deactivate(self) -> None:
        self._active_servo.max()
