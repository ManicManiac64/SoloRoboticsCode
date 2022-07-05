# ctre contains stuff for using TalonFXs on the robot, like TalonFX(). Kinda straightforward.
import ctre
# magicbot, for magic bots!
import magicbot

# the actual class
class Drivetrain:
    """
    This drivetrain component utilizes tank drive.
    """
    # define front left, back left, front right, back right motors
    FLMotor: ctre.WPI_TalonFX
    BLMotor: ctre.WPI_TalonFX
    FRMotor: ctre.WPI_TalonFX
    BRMotor: ctre.WPI_TalonFX

    # fun left and right values. these are class attributes but can still kinda sorta be used like
    # an instance attribute, so who needs __init__ anyways, hahahahaha
    left = magicbot.will_reset_to(0)
    right = magicbot.will_reset_to(0)

    # setup for the drivetrain (woah!)
    def setup(self):

        # back motors follow front motors in tank drive, this way we have less work :)
        self.BLMotor.follow(self.FLMotor)
        self.BRMotor.follow(self.FRMotor)

        #right motors must be inverted
        self.FRMotor.setInverted(True)
        self.BRMotor.setInverted(True)

        #set neutral mode to brake
        self.FLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.FRMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BRMotor.setNeutralMode(ctre.NeutralMode.Brake)

    def userDrive(self, left, right, percent):
        """
        Drive the drivetrain.
        """
        # these values will be used in execute, making this a setter/control function
        self.left = left * percent if abs(left) >= 0.05 else 0  # this is a deadband. google it
        self.right = right * percent if abs(right) >= 0.05 else 0  # deadband, more like one direction, ha get it? 'cause they're a d-oh whatever, moving on

    # this is what actually does stuff, w-w-w-w-woah! cool beans B)
    def execute(self):
        self.FLMotor.set(ctre.TalonFXControlMode.PercentOutput, self.left)
        self.FRMotor.set(ctre.TalonFXControlMode.PercentOutput, self.right)
