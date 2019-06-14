from userInterfaceAndInput import GUI
from userInterfaceAndInput import graph
from serialCommunication import getPort
from serialCommunication import Pump

port = getPort()
pump = Pump(port)

if pump.isOpen()
	myGUI = GUI()
	

