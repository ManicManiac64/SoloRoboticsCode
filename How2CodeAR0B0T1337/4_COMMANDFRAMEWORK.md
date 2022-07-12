RobotPy does not provide documentation for the command-based framework as of 2022, but you can look at the [C++/Java docs](https://docs.wpilib.org/en/stable/docs/software/commandbased/index.html) for further information.

# THE COMMAND-BASED FRAMEWORK

The command-based framework is the framework we'll be going over, because it's the one we used during Rapid React. I love another framework, the MagicBot framework, but it's not something I've mastered, so I don't think I'm ready to teach it just yet, especially because I'm already not exactly an expert at teaching. If you want to learn more about it, however, here's the [documentation](https://robotpy.readthedocs.io/en/latest/frameworks/magicbot.html) for it, and I'm happy to try and help you with anything regarding it, since documentation isn't perfect.

## FILE STRUCTURE

Every robot framework has a different file structure. The command-based framework breaks robots down into subsystems and commands. Subsystems are basic units of the robot like the drivetrain, the climber, and the intake. Commands are simply, well, commands. They're state machines that cause the subsystems to perform actions. On that note, a state machine is essentially an abstract machine that changes states based on input, in this case, something like the state of a motor based on joystick input. You could have a drivetrain subsystem with motors, and then a command to drive the drivetrain subsystem with joysticks. It breaks code apart into easily manageable pieces.

Something you should probably start doing when you have multi-file projects like this is using a `constants` file. This will allow you to put all your important constants throughout your project into one file where you can easily change values. For example, the `constants` file for that tank drive code you wrote earlier might look like this:

```
kFL = 0
kBL = 1
kFR = 2
kBR = 3

kdriverControllerPort = 0
```

This notation (prefixing constants with 'k') is what we usually use on the team, although the history behind it is a bit odd, in that there really isn't much history behind it. We use it mainly just because everybody else does, so it's a bit of an unofficial standard. There's a lot of people online who'll tell you it's because constant in Hungarian, or German, or something, is 'konstant', but that's not really true. It does stem back to something called *Hungarian notation*, a way to declare the types of variables which was invented by a Hungarian. But using *k* to mean a constant in computer science didn't come along until later. Very weird history.

Went on a bit of a tangent there, let's get back to the framework.

This is what the file structure for the command-based framework generally looks like:

```
robot folder
    commands folder
        (all your commands go here)
    subsystems folder
        (all your subsystems here)
    constants.py
    robot.py
    robotcontainer.py
```

That `robotcontainer` thing is another can of worms. It's essentially where we make the controller, make the timer, create the command chooser, and do a lot of other stuff. It does most of the heavy lifting instead of the `robot` file.

## TANK DRIVE (YET AGAIN)

I don't like that passive-aggressiveness coming from you, disembodied header.

Anyway, let's try programming that tank drive from before in the command-based framework. First, we'll create a drivetrain subsystem. Create a `drivetrain.py` file in your `subsystems` folder.

In this file, we'll inherit from `wpilib`, `ctre`, `commands2` (for the command-based framework), and a `constants` file. You can just create a `constants..py` file and copy the constants from above if you haven't already.

Next, we need to create a class for the drivetrain that inherits from `commands2.SubsystemBase`. This class is exactly what it sounds like: a base for subsystems. Wow! We'll then create an `__init__` function for the subsystem that begins by calling the `__init__` function of `SubsystemBase`. We can accomplish this by doing `super().__init__()`, `super()` referring to the parent class.

The rest of your code initializing the subsystem can just be copied and pasted from your tank drive code, but with your constants added in. Here's what it should look like so far:

```python
import wpilib
import ctre
import commands2

import constants

class Drivetrain(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        self.FLMotor = ctre.TalonFX(constants.kFL)
        self.BLMotor = ctre.TalonFX(constants.kBL)
        self.FRMotor = ctre.TalonFX(constants.kFR)
        self.BRMotor = ctre.TalonFX(constants.kBR)

        self.BLMotor.follow(self.FLMotor)
        self.BRMotor.follow(self.FRMotor)

        self.FLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.FRMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BRMotor.setNeutralMode(ctre.NeutralMode.Brake)

        self.FRMotor.setInverted(True)
        self.BRMotor.setInverted(True)
```

Next, we'll create a method in the subsystem to be called while we drive the robot. I'll call mine `userDrive`. Your method should have parameters of the left value and the right value, so we can pass them to the motors. Then, we can just (more or less) copy and paste the code from our old file, changing the `-self.driverController.getLeftY()` and `-self.driverController.getRightY()` to our left and right values. Here's your finished drivetrain code:

```python
import wpilib
import ctre
import commands2

import constants

class Drivetrain(commands2.SubsystemBase):
    
    def __init__(self):
        
        super().__init__()

        self.FLMotor = ctre.TalonFX(constants.kFL)
        self.BLMotor = ctre.TalonFX(constants.kBL)
        self.FRMotor = ctre.TalonFX(constants.kFR)
        self.BRMotor = ctre.TalonFX(constants.kBR)

        self.BLMotor.follow(self.FLMotor)
        self.BRMotor.follow(self.FRMotor)

        self.FLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BLMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.FRMotor.setNeutralMode(ctre.NeutralMode.Brake)
        self.BRMotor.setNeutralMode(ctre.NeutralMode.Brake)

        self.FRMotor.setInverted(True)
        self.BRMotor.setInverted(True)

    def userDrive(self, leftY: float, rightY: float):
        
        self.FLMotor.set(ctre.ControlMode.PercentOutput, -leftY)
        self.FRMotor.set(ctre.ControlMode.PercentOutput, -rightY)
```

By the way, in case you didn't know, that colon followed by 'float' is just telling the program leftY and rightY are expected to be floats. It's called 'type hinting'.

Now, let's create a command to drive the robot with the joysticks.

Creating commands is very easy to do. First, import `commands2`. Next import the drivetrain class from your drivetrain file. This way, we can use it for type hinting.

Next, create your command class, and make it inherit from `commands2.CommandBase`.

We'll now create an `__init__` method that takes a drivetrain, a leftY value, and a rightY value as parameters. The drivetrain type should be your drivetrain class, and the y values should be floats. The next step is calling the `__init__` function of `CommandBase` using `super().__init__()`.

Here's what we have so far:

```python
import commands2

from subsystems.drivetrain import Drivetrain

class JoystickDrive(commands2.CommandBase):

    def __init__(self, drive: Drivetrain, leftY: float, rightY: float):
        
        super().__init__()
```

Now, create attributes of the class: `self.drive`, `self.leftY`, and `self.rightY`, and have them get their values from the arguments of the `__init__` function. I know that might sound confusing coming out of my mouth, that's not because it's hard, it's just because I don't know how to phrase this right. You've probably done this before, I just mean this:

```python
self.drive = drive
self.leftY = leftY
self.rightY = rightY
```

Now, we need to use the `addRequirements` method of the parent class. Its arguments should be all the subsystems the command uses. In this case, we just use the `drive` attribute we defined in our initializing method:

```python
self.addRequirements([self.drive])
```

Here's the entire `__init__` method:

```python
def __init__(self, drive: Drivetrain, leftY: float, rightY: float):
        
    super().__init__()

    self.drive = drive
    self.leftY = leftY
    self.rightY = rightY

    self.addRequirements([self.drive])
```

Next, we'll create an `execute` method that will be called when the command is actually run. In it, we'll just use the `userDrive` method we defined earlier in our drivetrain class. This is all you need to do for the `execute` method.

```python
def execute(self):

    self.drive.userDrive(self.leftY, self.rightY)
```

Putting it all together, here's the code for our command:

```python
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
```

Feel free to take a short break now.

The next thing we need to create is the `robotcontainer` file.

First, we need to import `wpilib`, `commands2`, our `constants` file, our drivetrain subsystem, and our command.

Here's what that'll probably look like:

```python
import wpilib
import commands2

import constants

from subsystems.drivetrain import Drivetrain
from commands.joystick_drive import JoystickDrive
```

Next, let's create our robot container class. It won't inherit from anything. In the `__init__` method, we will initialize our driver controller like normal. Then, we will create a drivetrain instance. Finally, we will set the default command of this drivetrain using the `setDefaultCommand` method.

Here's what the code looks like:

```python
import wpilib
import commands2

import constants

from subsystems.drivetrain import Drivetrain
from commands.joystick_drive import JoystickDrive

class RobotContainer:
    def __init__(self):

        self.driverController = wpilib.XboxController(constants.kdriverControllerPort)
        
        self.drive = Drivetrain()

        self.drive.setDefaultCommand(JoystickDrive(self.drive, lambda: self.driverController.getLeftY(), lambda: self.driverController.getRightY()))
```

For some reason, we have to use lambdas in front of values we pass to the command that aren't the subsystem. Do I know why? No. Still, we have to do it anyways.

Speaking of anyways (the perfect segue), let's get into the `robot` file.

We'll start off importing `wpilib`, `commands2`, and our robot container from the `robotcontainer` file, or more accurately speaking, module. The file is `robotcontainer.py`, the module is `robotcontainer`. Doesn't really matter, but I'm pedantic.

Anyways, next we'll create our robot class. Make a class, and call it whatever you want, as long as it inherits from `commands2.TimedCommandRobot`. I'll call mine `CommandTankBot` because it's a command-based tank drive robot. No, I'm not very fun at parties, that is, if I ever went to any. I could go on a tangent about how I think the notion of high school parties are a conspiracy theory and that they don't exist anymore, but I'm probably just too cool to be invited to any.

Getting off that tangent/near-tangent, let's create our `robotInit` method, where we'll create our robot container. I'll call my variable `self.container`, because, again, I'm not fun at parties. This container should obviously be an instance of our robot container class.

Next, we'll just add our `if __name_ == "__main__"` line.

Here's something neat: In this case, there shouldn't be anything else we have to do. `commands2` does basically everything for us, which means you're basically done, probably! 

Probably......

...

...

...

Yeah, no, you're done, I just wanted to seem ominous. There'd be a bit more we'd have to do, in the `robotcontainer` file and in the `robot` file if we wanted to do other, more complicated things, like autonomous mode (which we'll go over soon), but in this case, nothing to really do.

Here's what your final `robot` code should look like:

```python
import wpilib
import commands2

from robotcontainer import RobotContainer

class CommandTankBot(commands2.TimedCommandRobot):
    
    def robotInit(self):
        self.container = RobotContainer()

if __name__ == "__main__":
    wpilib.run(CommandTankBot)
```

So there you have it, your first multi-file robot thingy in the command, uh, you know. But wait, there's more!

## REALLY?

No. Moving on, we'll be going over implementing autonomous commands. They're commands, but autonomous?!?!?!?!