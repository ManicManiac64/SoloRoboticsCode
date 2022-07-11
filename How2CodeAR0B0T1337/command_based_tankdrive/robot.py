import wpilib
import commands2

from robotcontainer import RobotContainer

class CommandTankBot(commands2.TimedCommandRobot):
    
    def robotInit(self):
        self.container = RobotContainer()

if __name__ == "__main__":
    wpilib.run(CommandTankBot)