from userInterfaceAndInput import GUI
from serialCommunication import getPort
from serialCommunication import Pump
from serialCommunication import destroyPrompt

port = getPort()
pump = Pump(port[0])
destroyPrompt(port[1])

if pump.checkConnection():
	myGUI = GUI(pump)
	
	
else:
	#pump.errorMessage()
	myGUI = GUI(pump)

	