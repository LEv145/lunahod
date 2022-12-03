from lunohod_details.impls.hand import Hand, AngularServo360, AngularServo90


BASE_SERVO_PIN = 23
CLAW_SERVO_1_PIN = 24
CLAW_SERVO_2_PIN = 25


claw = Hand(
    base_servo=AngularServo360(BASE_SERVO_PIN),
    claw_servo_1=AngularServo90(CLAW_SERVO_1_PIN),
    claw_servo_2=AngularServo90(CLAW_SERVO_2_PIN),
)

breakpoint()
