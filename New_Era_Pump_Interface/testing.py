from userInterfaceAndInput import GUI
from serialCommunication import getPort
from serialCommunication import Pump
from serialCommunication import destroyPrompt
port = getPort()
pump = Pump(port[0])
myGUI = GUI(pump)


