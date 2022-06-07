"""
main robot file (it does stuff)
"""

#import modules
import wpilib
import magicbot
import ctre
#import components.drivetrain
#import components.swervemodule
#import constants


class MagicSwerve(magicbot.MagicRobot):
    """
    Now we're gaming
    """
    
    drivetrain: components.drivetrain.Drivetrain
    
    #create the objects?!?!11?! now we're gaming
    def createObjects(self):
        #modules
        
        #self.FLModule = components.swervemodule.SwerveModule(ctre.WPI_TalonFX(constants.FLDrive), ctre.WPI_TalonFX(constants.FLTurn))
        #self.BLModule = components.swervemodule.SwerveModule(ctre.WPI_TalonFX(constants.BLDrive), ctre.WPI_TalonFX(constants.BLTurn))
        #self.FRModule = components.swervemodule.SwerveModule(ctre.WPI_TalonFX(constants.FRDrive), ctre.WPI_TalonFX(constants.FRTurn))
        #self.BRModule = components.swervemodule.SwerveModule(ctre.WPI_TalonFX(constants.BRDrive), ctre.WPI_TalonFX(constants.BRTurn))
        
        #controller
        
        #self.driverController = wpilib.XboxController(constants.driverControllerPort
        
        pass
        
    def teleopPeriodic(self):
        #self.drivetrain.move(-self.driverController.getLeftY(), self.driverController.getLeftX(), self.driverController.getRightX())
        pass
      
if __name__ == "__main__":
  wpilib.run(MagicSwerve)
