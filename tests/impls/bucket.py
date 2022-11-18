from lunohod.impls.bucket import Bucket, AngularServo90


ACTIVE_SERVO_PIN = 22


bucket = Bucket(
    active_servo=AngularServo90(ACTIVE_SERVO_PIN),
)

breakpoint()
