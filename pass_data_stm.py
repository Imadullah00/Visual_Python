import serial
import time 
stmData = serial.Serial('com4', 115200,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)             #whatever com port you are on
time.sleep(1)
stmData.flush()
can_accept_input = False

while True:
    # Wait for data to become available
    while stmData.in_waiting == 0:
        pass
         #time.sleep(0.05)
          # Hang here until new data is available

    # Read the data once available
    dataPacket = stmData.readline().decode()
    dataPacket = dataPacket.strip('\n')

    # Print the received line
    print(dataPacket)  # Print each line as it arrives

    # Check for the prompt 
    if "here:" in dataPacket:
        can_accept_input = True  # Set the flag to true, allowing input


    # Allow input only if the flag is set
    if can_accept_input:
        cmd = input()  # Read user input directly, without additional prompt
        cmd += '\n'  # Add a newline character
        #print(f'Sending command: {cmd}')  # Debugging line
        stmData.write(cmd.encode())
        stmData.flushOutput()
        # Send the command back to STM32
        #stmData.flushInput()   # Flush the input buffer
        can_accept_input = False