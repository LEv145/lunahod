from gpiozero import AngularServo


class AngularServo90Plus(AngularServo):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(min_angle=0, max_angle=90, *args, **kwargs)
