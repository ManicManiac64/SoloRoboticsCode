# PROGRAMMING LARRY: THE GUIDE

Let's say hypothetically you've been locked in a room and told to program Larry, 6343's swerve drive robot, with nothing but VSCode, Python, a computer, a charger (you'll be in there for a while), some food (you'll be in there for a while), some water (you'll be in there for a while), a television (gotta keep up with the news), and, of course, Larry. As I write this guide, I am not locked in a room, and I do not have food, drink, or Larry, because it's 2:30 in the morning because I've been staying up late programming. However, I do have all the other stuff, so let's program Larry, I guess. Larry has 4 swerve modules, each module with 2 Falcon 500 motors. To refer to these motors in code, you'll want to refer to the motor controller that controls them, i.e. the TalonFX. One motor drives the wheel (like a tank drive motor) and the other rotates the wheel. Now, how do we make swerve drive with these motors? Try and figure it out yourself.

If you couldn't figure it out, don't worry, I don't know how to either!

OK, I'm back after a long hiatus (somewhere between 4 hours and 2 millenia). Let's do this. But first, a quick little review/view of swerve drive.

Swerve drive is pretty neat, and it's been around for thousands of years. It was invented by the Greek Archimedes when King Hiero II got tired of mecanum drive robots. Swerve drive robots can do marvelous things, like turn water into wine, or move around the field in one direction while rotating. The moving is called translating, and the rotating is called...you know...

Rotating. It's called rotating. That's what it is.

Point is, King Hiero II is hypothetically back from the dead and he thinks you're Archimedes for some reason, and wants you to code stuff, I guess? I dunno, you got this, I guess.

## PROGRAMMING LARRY: THE GUIDE: THE MOVIE

Now, let's say hypothetically you've been asked to create a movie about this guide. I'd be flattered.

Let's start by programming a class for a swerve module.

```python
class SwerveModule:
    """
    Create a swerve module. __init__ takes drive motor and turn motor (TalonFXs). The drive motor drives the module, and the turn motor turns it using a PID controller.
    """

    def __init__(self, driveMotor: ctre.TalonFX, turnMotor: ctre.TalonFX):

        self.driveMotor = driveMotor
        self.turnMotor = turnMotor
```

This is cool and all (not really), but we're going to need a few more methods. The bare minimum we need are methods to set the speed of the drive motor and to set the angle of the turn motor. Let's add these methods.

```python
def setDirection(self, angle: float):
        """
        Change the direction the module is facing. Takes angle argument (degrees).
        """
        
        self.turnMotor.set(ctre.ControlMode.MotionMagic, self.degreesToSensorUnits(angle))
        
    def setSpeed(self, speed):
        """
        Change the speed of the module. speed argument should be between -1.0 (backward) and 1.0 (forward)
        """
        self.driveMotor.set(ctre.ControlMode.PercentOutput, speed)
```

For the uninitiated, MotionMagic is pretty cool. We can make stuff super smooth when moving the motor to a sensor position. Anyways, in this code things are quite simple. The drive motor uses PercentOutput to set values to the drive motor. The turn motor uses MotionMagic to move the wheel to the specified angle.

However, those with not very eagled eyes (botched that a little) will note that we use a method we haven't created in the setDirection method called 'degreesToSensorUnits'. We'll have to make that now. Thanks a lot, you meddling kids, you ruined my morning. That's a joke, I'm so sorry, I'm sure you're a lovely person and I just called you a meddling kid, I really don't mean to sound condescending, you're probably very mature, and- 

Moving on, the TalonFX takes values of "raw sensor units", not "degrees" (whatever those are), which is an issue when you want to pass degrees to the motor. Typically Talon motors will have either 4096 raw sensor units/rotation or 2048 units/rotation. The TalonFX has 2048. If there are 360 degrees per 2048 units, we can use dimensional analysis to convert degrees to units. (degrees/1) * (2048 units/360 degrees) means we can convert degrees to units with the formula deg * 2048/360. Let's define a method that will convert degrees to units. In my code, it is a static method, which means it can be called by a class or an instance of the class, but you don't have to make it static. Making it a class method (cls) or even just a instance method (self) is fine.

```python
@staticmethod
    def degreesToSensorUnits(deg: float) -> float:
        return deg * (2048/360)
```

Again, you really don't need to make this a static method. I did it because I want to be cool and #notlikeotherprogrammers. You don't have to be #notlikeotherprogrammers.

Whatever you do, that's basically the swerve module. It's done. It's over. You hopefully won't have to touch this again, because now it's time for the really hard part.

S W E R V E D R I V E

Can't be that hard, right?

## PROGRAMMING LARRY: THE GUIDE: THE MOVIE: THE VIDEO GAME

That's right, we're gaming now. Whether we're good at it or not is yet to be determined. On most swerve drive robots, the robot is controlled with three joystick values. The leftX and leftY values control the translation, while the rightX controls rotation. The rightX controls the speed of rotation, not the exact angle, which is neat and good. Swerve drive is very easy to drive, and also a living hell to code.