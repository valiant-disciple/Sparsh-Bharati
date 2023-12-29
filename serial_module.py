import serial.tools.list_ports
import serial
import time

def find_arduino():
    # Get a list of all available serial ports
    available_ports = list(serial.tools.list_ports.comports())

    for port in available_ports:
        # Check if the description contains the keyword "Arduino"
        if "Arduino" in port.description:
            return port.device

    return None

def connect_serial():
    arduino_port = find_arduino()

    if arduino_port:
        try:
            ser = serial.Serial(arduino_port, baudrate=9600, timeout=1)
            print(f"Connected to Arduino on {arduino_port}")
            return ser
        except serial.SerialException as e:
            print(f"Error: {e}")
            return None
    else:
        print("Arduino not found.")
        return None

def instruction_send(instructions):
    ser = connect_serial()

    if ser:
        try:
            while True:
                ser.write(instructions)
                time.sleep(1)

        except KeyboardInterrupt:
            ser.close()
            print("Connection closed.")