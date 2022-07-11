import commands2

from subsystems.drivetrain import Drivetrain

class JoystickDrive(commands2.CommandBase):

    def __init__(self, drive: Drivetrain, leftY: float, rightY: float):
        
        super().__init__()

        self.drive = drive
        self.leftY = leftY
        self.rightY = rightY

        self.addRequirements([self.drive])

    def execute(self):

        self.drive.userDrive(self.leftY, self.rightY)