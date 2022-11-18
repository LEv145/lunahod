from gpiozero import AngularServo


class AngularServo90(AngularServo):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(min_angle=-45, max_angle=45, *args, **kwargs)
