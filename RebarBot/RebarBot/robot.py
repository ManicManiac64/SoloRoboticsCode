"""
main robot file (it does stuff)
"""

# import the needed modules
import wpilib
import magicbot
import ctre
import components.drivetrain
import constants


class RebarBot(magicbot.MagicRobot):

    # beans. drivetrain is a Drivetrain, how cool is that woah
    drivetrain: components.drivetrain.Drivetrain

    # Create objects, wow! Yeah it's very self-explanatory
    def createObjects(self):
        # motors
        self.FLMotor = ctre.WPI_TalonFX(constants.FLMotorPort)
        self.BLMotor = ctre.WPI_TalonFX(constants.BLMotorPort)
        self.FRMotor = ctre.WPI_TalonFX(constants.FRMotorPort)
        self.BRMotor = ctre.WPI_TalonFX(constants.BRMotorPort)

        # controller
        self.driverController = wpilib.PS4Controller(constants.driverControllerPort)

    def teleopInit(self):
        '''When teleop starts, this will be called'''
        pass
        # haha jkkkk

    def teleopPeriodic(self):
        '''For every certain time interval teleop occurs, this is called'''
        # MOVE AAAAAAAAAAAAAAAAAAAAAAA
        self.drivetrain.move(-self.driverController.getLeftY(), -self.driverController.getRightY())
        wpilib.SmartDashboard.putNumber("LeftY", self.driverController.getLeftY())
        wpilib.SmartDashboard.putNumber("RightY", self.driverController.getRightY())

if __name__ == '__main__':
    # RUN AAAAAAAAAAAAAAAAAAAAAAAAAA
    wpilib.run(RebarBot)
