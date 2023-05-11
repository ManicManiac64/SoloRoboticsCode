import wpilib
import ctre

class ChordBot(wpilib.TimedRobot):

    def robotInit(self):

        self.music0 = ctre.TalonFX(0)
        self.music1 = ctre.TalonFX(1)
        self.music2 = ctre.TalonFX(2)
        self.music3 = ctre.TalonFX(3)
    
        self.orchestra = ctre.Orchestra()
        self.orchestra.addInstrument(self.music0)
        self.orchestra.addInstrument(self.music1)
        self.orchestra.addInstrument(self.music2)
        self.orchestra.addInstrument(self.music3)

        self.orchestra.loadMusic()

    def teleopPeriodic(self):

        self.orchestra.play()

if __name__ == "__main__":

    wpilib.run(ChordBot)
