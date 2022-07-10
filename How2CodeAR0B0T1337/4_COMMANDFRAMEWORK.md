## THE COMMAND FRAMEWORK (AND WHY I DON'T CARE FOR IT)

The command-based framework is the first framework we'll be going over, because it's the one we used during Rapid React. It's very important to know how it works, because it's the framework most used by people programming robots with Java and C++, the two most popular languages to code with in FRC.

However, I don't like the command-based framework in Python. I'll talk about why after I've gone over the pros and cons of this framework, as well as the next one I'll go over, the MagicBot Framework. We'll get to that later. For now, let's learn about the command-based framework.

## FILE STRUCTURE

Every framework has a different file structure. The command-based framework breaks robots down into subsystems and commands. Subsystems are basic units of the robot like the drivetrain, the climber, and the intake. Commands are simply, well, commands, that cause the subsystems to perform actions. You could have a drivetrain subsystem with motors, and then a command to drive the drivetrain subsystem with joysticks. It breaks code apart into easily manageable pieces.

Something you should probably start doing when you have multi-file projects is use a `constants` file. This will allow you to put all your important constants throughout your project into one file where you can easily change values. For example, the `constants` file for that tank drive code you wrote earlier might look like this:

```
FRONT_LEFT = 0
BACK_LEFT = 1
FRONT_RIGHT = 2
BACK_RIGHT = 3

DRIVER_CONTROLLER_PORT = 0
```

The values are in all caps to show that they are constants. You could also show that they are constants by putting a lowercase 'k' in front of them, like this:

```
kfrontLeft = 0
kbackLeft = 1
kfrontRight = 2
kbackRight = 3

kdriverControllerPort = 0
```

I disa