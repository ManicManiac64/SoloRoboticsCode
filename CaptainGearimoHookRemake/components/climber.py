import ctre
import magicbot

class Climber:
    """
    This climber component makes the robot climb the rungs on the field.
    """
    #scmotor is the motor for the short climber.
    SCMotor: ctre.WPI_TalonFX
    #tcmotor is for the tilted climber
    TCMotor: ctre.WPI_TalonFX

    #fun values for the climbers
    shortPercent = magicbot.will_reset_to(0)
    tiltedPercent = magicbot.will_reset_to(0)

    def setup(self):
        self.SCMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.TCMotor.setNeutralMode(ctre.NeutralMode.Brake)
    
    def changePercent(self, sPercent, tPercent):
        """
        Change the percent of the short climber motor
        """
        
        self.shortPercent = sPercent
        self.tiltedPercent = tPercent

    def execute(self):
        self.SCMotor.set(ctre.TalonFXControlMode.PercentOutput, self.shortPercent)
        self.TCMotor.set(ctre.TalonFXControlMode.PercentOutput, self.tiltedPercent)