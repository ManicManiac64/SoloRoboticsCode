import wpilib
import magicbot
import components.swervedrive
import constants

class Larry(magicbot.MagicRobot):

    drive: components.swervedrive.SwerveDrive

    def createObjects(self):
        """
        Create objects. Wow!!!
        """

        self.FRModule = components.swervedrive.SwerveModule(constants.FRDRIVE, constants.FRANGLE)
        self.FLModule = components.swervedrive.SwerveModule(constants.FLDRIVE, constants.FLANGLE)
        self.BLModule = components.swervedrive.SwerveModule(constants.BLDRIVE, constants.BLANGLE)
        self.BRModule = components.swervedrive.SwerveModule(constants.BRDRIVE, constants.BRANGLE)
        
        self.driverController = wpilib.XboxController(0)
        self.gyro = wpilib.ADXRS450_Gyro()
        self.gyro.reset()

    def teleopPeriodic(self):
        """
        Called every time robot is in teleop
        """    

        self.drive.move(self.driverController.getLeftX(), -self.driverController.getLeftY(), self.driverController.getRightX(), self.gyro.getRotation2d().degrees() % 360)

if __name__ == '__main__':
    wpilib.run(Larry)