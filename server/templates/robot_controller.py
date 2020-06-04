'''
Robot controllers

written by Brett Stoddard for the neato robot ChairBot

uses formatting based on this article
    https://realpython.com/documenting-python-code/

uses calulations from this related project
    https://github.com/charisma-lab/neato_localization/blob/master/scripts/localizing_tracked_markers.py

TODO change docstrings to match epydoc format for easy documentation generation
    http://epydoc.sourceforge.net/epytext.html

Changelogs:
- 6/4 started class. Wrote basic public interfaces
-

'''


class RobotController:
    """
    A class used to track multi-robot information

    This is the main class used by the outside world

    Attributes
    ----------
    robots : dictionary < RobotEntity >
        dictionary of robots indexed by fiducial/robot id
    originId : int
        fiducial id of the origin reference used
    originLocation : tuple < int, int >
        x,y coordinates of the origin fiducial
    goals : dictionary < tuple < int, int > >
        dictionary of robot goals indexed by fiducial/robot id containing a tuple
        with x,y coordinates
    socket : ???
        socket used to send commands

    Public Methods
    -------
    calculateCommand( id: int ) -> Command
        calculates which command to send to the robot (eg turn, forward)
    sendCommand( command: Command)
        sends a command to the robot
    """

    def __init__(self, fiducialIds, originId, originCoords=None):
        """
        Parameters
        ----------
        robotIds : array < int >
            array of fiducial/robot ids that may be active in the scene
        originId : int
            fiducial id of the origin point
        originCoords : tuple <int, int>, optional
        """

        self.originId = origin_id
        self.originCoords = originCoords
        self.robots = {x : RobotEntity(x) for x in fiducialIds}

    def updateRobotLocation(self, coords, robotId):
        """ Updates a robots saved location which can then be used to calculate
        robot movements

        Parameters
        ----------
        coords : tuple < int, int >
            x,y coordinates of the origin's coordinates in the system
        """

        self.robots[robotId].updateCoords(coords)

    def updateOriginLocation(self, coords):
        """ Updates origin's saved location which can then be used to calculate
        robot movements

        Parameters
        ----------
        coords : tuple < int, int >
            x,y coordinates of the origin's coordinates in the system
        """

        self.originCoords = coords


    def calculateCommand(self, robotId, newRobotCoords=None): #TODO finish writing
        """Calculates a robots best move in order to move toward it's goal
        based on it's last saved coordinates

        this method can be called right after setting the robots location
        and that command can be sent in a loop until the next time a location is
        passed

        Parameters
        ----------
        robotId : int
            The sound the animal makes (default is None)
        newRobotCoords : tuple <int,int>, optional
            x,y coordinates for this robot's new location. If not provided, then
            last saved location of the robot will be used

        Raises
        ------
        SystemError
            If origin or robot coordinates are not defined (falsy)
        """

        if not self.originCoords:
            raise SystemError('Origin coordinates not found (or falsey). \
                Command cannot be calculated without a reference')

        robotCords = newRobotCoords
        if not newRobotCoords:
            robotCords = (0,0) # TODO get coords from RobotEntity class

        if not robotCords:
            raise SystemError('Robot coordinates not found (or falsey). \
                Command cannot be calculated without a reference')

        # TODO calcualte and return command



class CommandClass:
    """
    A class used to contain command messages sent to the robots

    Attributes
    ----------
    command : str
        command string interperable by robot

    Methods
    ----------
    generateCommand(id)
        generates a command for a robot of specific ID
    """

    commandString = '{} SEND TO {}' # NOTE this is a placeholder

    def __init__(self, command):
        """ Initializes a specific type of command
        Parameters
        ----------
        commmand : str
            command string interperable by robot
        """

        self.command = command


    def generateCommand(self, id):
        """ Generates command datastricture that is interperable by robot client
        Parameters
        ----------
        id : int
            robot/fiducial id of the robot recieving command
        """

        return commandString.format(self.command, str(id))



class RobotEntity:
    """
    A class used to contain data about a specific robot

    Attributes
    ----------
    coords : tuple <int,int>
        x,y coordinates of the robot
    id : int
        the id assigned to this robot. Could be related to fiducial id

    Methods
    ----------
    updateCoords()
        update the internally saved coordinates for this robot
    updateCoordinates()
        see updateCoords
    """

    commandString = '{} SEND TO {}' # NOTE this is a placeholder

    def __init__(self, id, coords=None):
        """ Initializes a robot entity

        Parameters
        ----------
        id : int
            command string interperable by robot
        coords : tuple <int,int>, optional
            starting x,y coordinates of the robot
        """

        self.id = id
        self.coords = coords


    def generateCommand(self, id):
        """ Generates command datastricture that is interperable by robot client
        Parameters
        ----------
        id : int
            robot/fiducial id of the robot recieving command
        """

        return commandString.format(self.command, str(id))
