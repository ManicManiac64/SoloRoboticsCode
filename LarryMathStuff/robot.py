"""
import all needed modules, 
wpilib is basically like the base FRC module we use, 
magicbot is the framework this code uses, 
components.swervedrive is the swerve drive component, 
and constants is the file with all our constants
"""

import wpilib
import magicbot
import components.swervedrive
import constants

# create the robot class (inherits from MagicRobot, because this robot is a type of MagicRobot)

class Larry(magicbot.MagicRobot):

    # drive refers to a swerve drive

    drive: components.swervedrive.SwerveDrive
    
    # create all objects the robot needs

    def createObjects(self):
        """
        Create objects. Wow!!!
        """

        # four swerve modules that take the drive motor id and the turn motor id

        self.FRModule = components.swervedrive.SwerveModule(constants.FRDRIVE, constants.FRANGLE)
        self.FLModule = components.swervedrive.SwerveModule(constants.FLDRIVE, constants.FLANGLE)
        self.BLModule = components.swervedrive.SwerveModule(constants.BLDRIVE, constants.BLANGLE)
        self.BRModule = components.swervedrive.SwerveModule(constants.BRDRIVE, constants.BRANGLE)
        
        # the driverController is an XboxController used to control the robot. The gyro is a gyroscope, and calibrate() calibrates the gyroscope

        self.driverController = wpilib.XboxController(0)

        # self.gyro = wpilib.ADIS16470_IMU()

        # if wpilib.RobotBase.isReal():

        #     self.gyro.setYawAxis(wpilib.ADIS16470_IMU.IMUAxis.kZ)
        #     self.gyro.calibrate()

    def teleopPeriodic(self):
        """
        Called every time robot is in teleop
        """    

        #this move function takes joystick values, and the rotation of the gyro converted to degrees, and will give us the right values for the motors.

        # self.drive.move(self.driverController.getLeftX(), -self.driverController.getLeftY(), self.driverController.getRightX(), self.gyro.getAngle() % 360)

        self.drive.move(self.driverController.getLeftX(), -self.driverController.getLeftY(), self.driverController.getRightX())

if __name__ == '__main__':
    wpilib.run(Larry)
