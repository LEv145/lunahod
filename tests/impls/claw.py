from lunohod_details.impls.claw import Claw, AngularServo90, AngularServo90Plus


ACTIVE_SERVO_PIN = 23
ROTATION_SERVO_PIN = 24


claw = Claw(
    active_servo=AngularServo90(ACTIVE_SERVO_PIN),
    rotation_servo=AngularServo90Plus(ROTATION_SERVO_PIN),
)

breakpoint()
