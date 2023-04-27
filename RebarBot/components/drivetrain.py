# wpilib is kinda required when we do anything with robots in frc, sooooooo
import wpilib
# wpilib.drive contains stuff great for tank drive! :D :D :D :D :D (those are happy faces)
import wpilib.drive
# ctre contains stuff for using TalonFXs on the robot, like TalonFX(). Kinda straightforward.
import ctre
# magicbot, for magic bots!
import magicbot


# the actual class
class Drivetrain:
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
        
        # define differential drive (we'll use it for our tank drive)
        self.drive = wpilib.drive.DifferentialDrive(self.FLMotor, self.FRMotor)

        wpilib.SmartDashboard.putBooleanArray("L, R", [self.FLMotor.getInverted(), self.FRMotor.getInverted()])

    def move(self, left, right):
        # these values will be used in execute, making this a setter/control function
        self.left = left if abs(left) >= 0.05 else 0  # this is a deadband. google it
        self.right = right if abs(right) >= 0.05 else 0  # deadband, more like one direction, ha get it? 'cause they're a d-oh whatever, moving on

        wpilib.SmartDashboard.putNumberArray("L, R", [self.left, self.right])

    # this is what actually does stuff, w-w-w-w-woah! cool beans B)
    def execute(self):
        self.drive.tankDrive(self.left, self.right)
