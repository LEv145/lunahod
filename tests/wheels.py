from lunohod_details.impls.wheels import Wheels, VNH3SP30Motor, AngularServo90


IN_A_PIN = 16
IN_B_PIN = 20
PWM_PIN = 21
EN_PIN = 12
SERVO_PIN = 7


wheels = Wheels(
    motor=VNH3SP30Motor(IN_A=IN_A_PIN, IN_B=IN_B_PIN, PWM=PWM_PIN, EN=EN_PIN),
    servo=AngularServo90(7),
)

breakpoint()
