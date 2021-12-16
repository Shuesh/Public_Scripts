import re
import copy


def main():
    binary_string = Input_to_List('Day_16/Example4_16.txt')
    remaining_string = binary_string

    version_sum = 0
    while remaining_string:
        current_version = Get_Version(remaining_string)
        version_sum += current_version
        remaining_string = remaining_string[3:]
        current_type = Get_Type(remaining_string)
        remaining_string = remaining_string[3:]

    


def Input_to_List(path):

    # match_string = r"\d"

    file = open(path, 'r')
    #Treats it as hexadecimal
    line = file.readline().strip()
    # row = list(map(int,re.findall(match_string, line)))

    convert = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'
    }

    new_list = []


    for char in line:
        new_list.append(convert[char])

    binary_string = str(new_list)
            
    return binary_string



def Get_Version(packet):
    binary_version = packet[:3]

    decimal_version = 0
    for index, value in enumerate(reversed(binary_version)):
        decimal_version += (2 ** index) * int(value)

    return decimal_version
    


def Get_Type(packet):
    binary_type = packet[3:6]

    decimal_type = 0
    for index, value in enumerate(reversed(binary_type)):
        decimal_type += (2 ** index) * int(value)

    return decimal_type


def Get_Length(packet):
    if packet == '0':
        return 15
    else:
        return 11


def Literal(packet):
    start = 6
    end = 11
    packet_number = 1
    subpacket = packet[start:end]

    data = []

    while subpacket[0] == '1':
        data.append(subpacket[1:])
        packet_number += 1
        subpacket = packet[start*packet_number:end*packet_number]

    data.append(subpacket[1:])
    
    return data


def Operator(packet, bits_or_packets, length):
    current_packet = packet[:length]


if __name__ == '__main__':
    main()

