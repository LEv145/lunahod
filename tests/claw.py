from lunohod.claw import Claw, AngularServo90, AngularServo360


claw = Claw(
    base_servo=AngularServo360(23),
    claw_servo_1=AngularServo90(24),
    claw_servo_2=AngularServo90(25),
)

breakpoint()
