Server
	|<-----> Websocket <-----> ESP32-CAM
									|-----> ULN2004 #1 ----> Stepper Motor #1
									|-----> ULN2004 #2 ----> Stepper Motor #2
									|<----- Camera
									|<----> I2C <-----> MCP23017 <-----> GPIO
																		   	|-----> Motor Driver (Nav)
																						|------> Firing Motor 1
																						|------> Firing Motor 2

