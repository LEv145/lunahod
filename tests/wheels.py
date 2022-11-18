from lunohod.wheels import Wheels, VNH3SP30Motor, AngularServo90


wheels = Wheels(
    motor=VNH3SP30Motor(IN_A=16, IN_B=20, PWM=21, EN=12),
    servo=AngularServo90(7),
)

breakpoint()
