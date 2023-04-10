from BitVector import BitVector
import serial
from datetime import datetime
from middleman.api_client import APIPost
'''struct
{
    uint32_t Id;        // CAN Extended or Standard Id //11 bits is standard, 29 bits is extended
    uint8_t IsExtended; // 1 or 0, whether the frame is extended
    uint8_t IsRTR;        // 1 or 0, whether the frame is a remote transmission
    uint8_t Length;        // Number of bytes in the data
    #1 byte of space between header and data
    uint8_t Data[8];    // Payload of the CAN frame
};
uint8_t Bytes[16];'''
'''UNTESTED AS OF NOW: NEEDS A LOT OF TESTING'''
'''translates a SINGLE CAN frame to data that we can format/send to backend'''
'''assumption is that this function will decode a single CAN frame and decode all the CAN frames in a loop'''
'''this function assumes the buffer/sync frame stuff has already been done'''
def translate_CAN_frame(can_frame : BitVector) -> list:
    data_list = []
    data_dict = {}
    message_ID_length = 32 #length in bits
    data_hash_map = {"0x00000020": "BMS_temp_state", "0x00000120": "BMS_current_voltage", "0x00000071": "VESC_set_duty_cycle", "0x00000971" : "VESC_status_1", "0x00000E71" : "VESC_status_2", "0x00000F71" : "VESC_status_3", "0x00001071" : "VESC_status_4", "0x00001B71" : "VESC_status_5"} #is a hash map of key: value pairs where the key is a string of the message ID and the value is the corresponding type of data (like speed, temp etc)
    message_ID_bv = can_frame[0:message_ID_length] #stores message_ID_bits
    message_ID = str(message_ID_bv.get_bitvector_in_hex())

    data_dict["time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if message_ID in data_hash_map:
        if(data_hash_map[message_ID] == "VESC_set_duty_cycle"):
            data_list.append("VESC_set_duty_cycle")

            start_idx = 64
            end_idx = 64 + 32
            pack_current = can_frame[start_idx: end_idx].int_val() * 10000
            data_dict["dutyCycle"] = duty_cycle
        elif(data_hash_map[message_ID] == "VESC_status_1"):
            data_list.append("VESC_status_1")

            start_idx = 64
            end_idx = 64 + 32
            rpm = can_frame[start_idx: end_idx].int_val()
            data_dict["rpm"] = rpm

            start_idx += 16
            end_idx += 16
            current_consumed = can_frame[start_idx: end_idx].int_val() * 10
            data_dict["currentConsumed"] = current_consumed

            start_idx += 16
            end_idx += 16
            duty_cycle = can_frame[start_idx: end_idx].int_val() * 1000
            data_dict["dutyCycle"] = duty_cycle
        elif(data_hash_map[message_ID] == "VESC_status_2"):
            data_list.append("VESC_status_2")

            start_idx = 64
            end_idx = 64 + 32
            amp_hours_consumed = can_frame[start_idx: end_idx].int_val() * 10000
            data_dict["ampHoursConsumed"] = amp_hours_consumed

            start_idx += 32
            end_idx += 32
            amp_hours_regenerative = can_frame[start_idx: end_idx].int_val() * 10000
            data_dict["ampHoursRegenerative"] = amp_hours_regenerative
        elif(data_hash_map[message_ID] == "VESC_status_3"):
            data_list.append("VESC_status_3")

            start_idx = 64
            end_idx = 64 + 32
            watt_hours_consumed = can_frame[start_idx: end_idx].int_val() * 10000
            data_dict["wattHoursConsumed"] = watt_hours_consumed

            start_idx += 32
            end_idx += 32
            watt_hours_regenerative = can_frame[start_idx: end_idx].int_val() * 10000
            data_dict["wattHoursRegenerative"] = watt_hours_regenerative
        elif(data_hash_map[message_ID] == "VESC_status_4"):
            data_list.append("VESC_status_4")

            start_idx = 64
            end_idx = 64 + 16
            mosfet_temp = can_frame[start_idx: end_idx].int_val() * 10
            data_dict["mosfetTemp"] = mosfet 

            start_idx += 16
            end_idx += 16
            motor_temp = can_frame[start_idx: end_idx].int_val() * 10
            data_dict["motorTemp"] = motor_temp

            start_idx += 16
            end_idx += 16
            total_input_current = can_frame[start_idx: end_idx].int_val() * 10
            data_dict["totalInputCurrent"] = total_input_current

            start_idx += 16
            end_idx += 16
            pid_position = can_frame[start_idx: end_idx].int_val() * 10
            data_dict["pidPosition"] = pid_position
        elif(data_hash_map[message_ID] == "VESC_status_5"):
            data_list.append("VESC_status_5")

            start_idx = 64
            end_idx = 64 + 32
            tachometer = can_frame[start_idx: end_idx].int_val()
            data_dict["tachometer"] = tachometer

            start_idx += 16
            end_idx += 16
            input_voltage = can_frame[start_idx: end_idx].int_val() * 10
            data_dict["totalInputVoltage"] = input_voltage
        elif(data_hash_map[message_ID] == "BMS_temp_state"):
            data_list.append("BMS_temp_state")

            start_idx = 64
            end_idx = 64 + 16
            pack_temp = can_frame[start_idx: end_idx].int_val() 
            data_dict["packTemp"] = pack_temp

            start_idx += 16
            end_idx += 16
            highest_cell_temp = can_frame[start_idx: end_idx].int_val()
            data_dict["highestCellTemp"] = highest_cell_temp

            start_idx += 16
            end_idx += 16
            lowest_cell_temp = can_frame[start_idx: end_idx].int_val()
            data_dict["lowestCellTemp"] = lowest_cell_temp

            start_idx += 8
            end_idx += 8 
            relay_state = can_frame[start_idx: end_idx].int_val()
            data_dict["relayState"] = relay_state

            start_idx += 8
            end_idx += 8
            state_of_charge = can_frame[start_idx: end_idx].int_val() * 2
            data_dict["stateOfCharge"] = state_of_charge
        elif(data_hash_map[message_ID] == "BMS_current_voltage"):
            data_list.append("BMS_current_voltage")

            start_idx = 64
            end_idx = 64 + 16
            pack_current = can_frame[start_idx: end_idx].int_val() * 10
            data_dict["packCurrent"] = pack_current

            start_idx += 16
            end_idx += 16
            pack_voltage = can_frame[start_idx: end_idx].int_val() * 100
            data_dict["packVoltage"] = pack_voltage

            start_idx += 16
            end_idx += 16
            highest_cell_voltage = can_frame[start_idx: end_idx].int_val() * 10000
            data_dict["highestCellVoltage"] = highest_cell_voltage

            start_idx += 16
            end_idx += 16
            lowest_cell_voltage = can_frame[start_idx: end_idx].int_val() * 10000
            data_dict["lowestCellVoltage"] = lowest_cell_voltage
    else:
        print(f"ERROR: Could not find the messageID {message_ID} within the dataHashMap")
    data_list.append(data_dict)
    return data_list #list of lists
    '''
    example return value
    ["BMS_status_1", nested_dictionary]
    '''

'''this function returns a true or false depending on if the data stream is in sync or not'''
'''
based on example hex file given, I think SYNC frame is like this:
| S | Y | N | C | FF | FF | FF | FF | FF | FF | FF | FF | FF | FF | FF | FF |
so synchronization assumes this is the correct format
'''
def synchronize(serial_port: serial):
    letter = serial_port.read(1)
    while(True):
        if letter.hex() == 0x51: #check if byte is "S"
            letter = serial_port.read(1)
            if letter.hex() == 0x59: #check if byte is "Y"
                letter = serial_port.read(1)
                if letter.hex() == 0x4E: #check if byte is "N"
                    letter = serial_port.read(1)
                    if letter.hex() == 0x43: #check if byte is "C"
                        break
    serial_port.read(12) #reads in the rest of the 12 bytes
    return

def is_sync_frame(frame : BitVector) -> bool: #checks if the CAN frame we pulled is a sync frame. Returns True if it is, else returns False
    for i in range(0, frame.length() // 8): #check byte by byte of frame
        if (frame[ (i*8): (i*8) + 8].get_bitvector_in_hex() == 0x51): #if "S"
            i += 1
            if (frame[ (i*8): (i*8) + 8].get_bitvector_in_hex() == 0x59): #if "Y"
                i += 1
                if (frame[ (i*8): (i*8) + 8].get_bitvector_in_hex() == 0x4E): #if "N"
                    i += 1
                    if (frame[ (i*8): (i*8) + 8].get_bitvector_in_hex() == 0x4E): #if "C"
                        return True
    return False

'''
based on example hex file given, I think SYNC frame is like this:
| S | Y | N | C | FF | FF | FF | FF | FF | FF | FF | FF | FF | FF | FF | FF |
so sync frame validation function based off of this function
'''
def is_valid_sync_frame(frame: BitVector) -> bool: #checks if the SYNC frame pulled is a valid one. Returns True if it is, else returns False
    if (frame[0:8].get_bitvector_in_hex() == 0x51): #if "S"
            if (frame[8:16].get_bitvector_in_hex() == 0x59): #if "Y"
                if (frame[16:24].get_bitvector_in_hex() == 0x4E): #if "N"
                    if (frame[24:32].get_bitvector_in_hex() == 0x4E): #if "C"
                        if (frame[32:128].get_bitvector_in_hex() == 0): #if the rest of the bytes are "0"
                            return True
    return False
#UNTESTED: needs testing
'''
1) Setup Serial Port
2) Check if it's open
3) Synchronize stream initially
4) Wait until there's at least 16 bytes in the input buffer
5) Read in 16 bytes from the input buffer
6) Convert Bytes object to hex string and then make a bitvector from hex string
7) See if the CAN frame is a SYNC frame
8) If it is, then see if it's fully synchronized
9) If it is synchronized, then grab next CAN frame, else, synchronize stream
10) Call translateCANframe function with the bitvector which returns a list of [data_type, data]
11) TODO: Format data into respective sections
12) TODO: Call respective api
'''
def decrypt(ser):  #decrypt data from serial and process/format it for readable bytes
    synchronize(serial_port=ser)#infinite loops until SYNC frame is seen
    '''assumption is that we'll only have to sync once before looping'''
    while True:
        while (ser.in_waiting() < 16): #while the number of bytes in the input buffer is less than 16, infinite loop
            pass
        data = ser.read(16) #data is a Bytes Object
        data_bv = BitVector(hexstring = data.hex()) #converts hex string to bitVector
        '''
        TODO: TEST BELOW LOGIC
        Not sure if the below logic is needed but can test to see if needed
        because a sync frame is sent somewhat regularly, we have to detect it
        But if we detect a sync frame, we don't know if we're out of sync or not (it's possible we could get out of sync somehow)
        So we detect if a sync frame exists. If it does exist, we see if it's fully in sync.
        If it is fully in sync, then just restart the loop to skip the sync CAN frame
        If it's not in sync, then synchronize stream
        '''
        if(is_sync_frame(frame = data_bv)):                 
            if(is_valid_sync_frame(frame = data_bv)):
                continue
            else:
                synchronize(ser)
                continue
        data_info_list = translate_CAN_frame(can_frame = data_bv)
        '''data_info_list is a list of [data_type, data] as described in translateCANframe'''
        #TODO
        #format data into respective sections
        APIPost(data_info_list[0], data_info_list[1])
        #call respective api

#sets up serial port
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    timeout=1,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

#1)Makes sure serial port was created successfully and is open
if(ser.is_open):
    print("is open\n")
else:
    print("not open\n")
# Reading the data from the serial port. This will be running in an infinite loop.
decrypt(ser)