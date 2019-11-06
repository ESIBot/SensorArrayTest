import pygame, serial, time, sys
from pygame.locals import *

puerto = '/dev/ttyACM0'
velocidad = 115200

numSensors = 8
pixelSize = 100

SCREEN_WIDTH = numSensors*pixelSize
SCREEN_HEIGHT = pixelSize

def main():
	print("Configuración actual:")
	print("Puerto: %s" % puerto)
	print("BPS = %d" % velocidad)
	print("Nº de sensores: %d" %numSensors)

	try:
		arduino = serial.Serial(puerto, baudrate=velocidad, timeout=1.0)
		arduino.setDTR(False)
		time.sleep(1)
		arduino.flushInput()
		arduino.setDTR(True)
	except (ImportError, serial.SerialException):
		print('ERROR: Placa no encontrada.\nConfigura tu puerto editando este archivo.')
		sys.exit()

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Sensor array test (en %s)" % puerto)

	while True:
		line = arduino.readline()
		sensorValues = line.decode('ascii', errors='replace').split(',')

		if(len(sensorValues) >= 8):
			for i in range(numSensors):
				if(sensorValues[i] != '\r\n' and sensorValues[i] != ''):
					value = int(sensorValues[i])
					color=(value,value,value)
					pygame.draw.rect(screen,color,(i*pixelSize,0,pixelSize,pixelSize))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit()
		pygame.display.update()

if __name__ == "__main__":
    main()
