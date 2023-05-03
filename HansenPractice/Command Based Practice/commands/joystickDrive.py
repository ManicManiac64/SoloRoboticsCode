import commands2, wpilib
from subsystems.drivetrain import Drivetrain

class JoystickDrive(commands2.CommandBase):

    def __init__(self, train: Drivetrain, left, right):

        super().__init__()

        self.train = train

        self.leftFunc = left
        self.rightFunc = right

        self.addRequirements([self.train])

    def execute(self):

        self.left = self.leftFunc()
        self.right = self.rightFunc()

        self.train.joystickDriving(self.left, self.right)

    def end(self, interrupted):

        self.train.joystickDriving(0, 0)

    def isFinished(self):
        
        return False