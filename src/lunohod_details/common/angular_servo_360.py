from gpiozero import AngularServo


class AngularServo360(AngularServo):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(min_angle=-360, max_angle=360, *args, **kwargs)
