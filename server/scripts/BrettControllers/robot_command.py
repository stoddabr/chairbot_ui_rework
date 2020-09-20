'''
Robot command class

written by Brett Stoddard for the neato robot ChairBot

uses formatting based on this article
  https://realpython.com/documenting-python-code/

Changelogs:
- 6/4 Brett started class. Wrote basic public interfaces
- 6/20 Brett continued class. extended class to include ROS interface
'''


class CommandClass:
    """
    A class used to contain and execute command messages sent to the robots

    command strings:
    Nothing:  do nothing
    Forward:  move forward
    Backward: move backward
    Right:    turn right
    Left:     turn left

    Attributes
    ----------
    command : str
      command string interperable by robot

    Methods
    ----------
    generateCommand(id)
      generates a command for a robot of specific ID
    """

    def __init__(self, command):
        """ Initializes a specific type of command

        Parameters
        ----------
        commmand : str
          command string interperable by robot
        """

        self.commandString = command

    def generateCommand(self, id):
        """ Generates command datastricture that is interperable by robot client
        Parameters
        ----------
        id : int
          robot/fiducial id of the robot recieving command
        """

        # TODO match format server is expecting
        commandTemplate = '{} SEND TO {}'  # NOTE this is a placeholder
        return commandTemplate.format(self.commandString, str(id))

    def isNothing(self):
        """ Checks if command is to do nothing

        Returns boolean
            true if the command is do nothing
        """

        return self.commandString == "Nothing"
