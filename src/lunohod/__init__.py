from lunohod.common import AngularServo360, AngularServo90, AngularServo90Plus
from lunohod.impls.wheels import Wheels
from lunohod.impls.bucket import Bucket
from lunohod.impls.claw import Claw
from lunohod.impls.hand import Hand


class Lunohod():
    def __init__(
        self,
        wheels: Wheels,
        hand_1: Hand,
        hand_2: Hand,
        bucket: Bucket,
        claw: Claw
    ) -> None:
        self.wheels = wheels
        self.hand_1 = hand_1
        self.hand_2 = hand_2
        self.bucket = bucket
        self.claw = claw
