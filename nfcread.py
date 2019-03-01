import serial
import signal

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    f.close()
    ser.close()
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

ser = serial.Serial('/dev/ttyACM0')

while True:
    line = ser.readline()
    print(line)
    f = open('data.txt', 'a')
    f.write(str(line))
