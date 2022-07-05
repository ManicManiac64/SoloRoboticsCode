import wpilib
import ctre
import magicbot

class Intake:
    """
    Intake component. This can take balls in and pass them to the launcher or push balls out. It goes up and down using solenoids. Probably the most complex component on the robot.
    """

    intakeSolenoid: wpilib.DoubleSolenoid
    bottomMotor: ctre.WPI_TalonFX
    topMotor: ctre.WPI_TalonFX
    
    intakeUp = True
    
    bottom = magicbot.will_reset_to(0)
    top = magicbot.will_reset_to(0)

    def setup(self):
        self.bottomMotor.setNeutralMode(ctre.NeutralMode.Coast)
        self.topMotor.setNeutralMode(ctre.NeutralMode.Coast)

    def toggle(self):
        """
        Toggle whether intake is up or down.
        """
        self.intakeUp = not self.intakeUp

    def spinBottom(self, percent):
        self.bottomMotor.set(ctre.TalonFXControlMode.PercentOutput, percent)
        
    def spinTop(self, percent):
        self.topMotor.set(ctre.TalonFXControlMode.PercentOutput, percent)

    def execute(self):
        if not self.intakeUp:
            self.intakeSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        else:
            self.intakeSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)

        if self.bottom != 0:
            self.bottomMotor.set(self.bottom)

        if self.top != 0:
            self.topMotor.set(self.top)