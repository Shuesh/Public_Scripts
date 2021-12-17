import re
import copy


def main():
    binary_string = Input_to_List('Day_16/Input_16.txt')
    version_sum = Recursive_Packet(binary_string)
    print(version_sum)


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

    binary_string = ''
    for char in new_list:
        binary_string += char
            
    return binary_string


def Bin_to_Dec(string):
    decimal_version = 0
    for index, value in enumerate(reversed(string)):
        decimal_version += (2 ** index) * int(value)
    return decimal_version


def Get_Version(packet):
    binary_version = packet[:3]

    decimal_version = Bin_to_Dec(binary_version)

    return decimal_version
    

def Get_Type(packet):
    binary_type = packet[3:6]

    decimal_type = Bin_to_Dec(binary_type)

    return decimal_type


def Get_Length_Type(packet):
    if packet[6] == '0':
        return 15
    else:
        return 11


#Type 4
def Literal(packet):
    start = 6
    end = 11
    packet_number = 1
    subpacket = packet[start:end]

    data = []

    while subpacket[0] == '1':
        data.append(subpacket[1:])
        packet_number += 1
        subpacket = packet[start+5*(packet_number-1):end+5*(packet_number-1)]

    data.append(subpacket[1:])

    endpoint = 6 + 5*packet_number
    
    data_string = ''
    for term in data:
        data_string += term
    
    return data_string, endpoint



def Operator(packet):
    packet_type = Get_Type(packet)
    length_type = Get_Length_Type(packet)
    
    #total length of subpackets in bits
    if (length_type == 15):
        bit_length = Bin_to_Dec(packet[7:22])
        data, endpoint = Parse_Subpackets_bits(packet[22:22+bit_length])
        endpoint_total = 22 + endpoint

    #total number of subpackets immediately contained in this packet
    else:
        num_subpackets = Bin_to_Dec(packet[7:18])
        data, endpoint = Parse_Subpackets_Count(packet[18:], num_subpackets)
        endpoint_total = 18 + endpoint

    for index,term in enumerate(data):
        if type(term) is not int:
            data[index] = Bin_to_Dec(term)

    total = 0
    #Type 0
    if packet_type == 0:
        for subpacket in data:
            total += subpacket
    #Type 1
    elif packet_type == 1:
        total = 1
        for subpacket in data:
            total *= subpacket
    #Type 2
    elif packet_type == 2:
        total = min(data)
    #Type 3
    elif packet_type == 3:
        total = max(data)
    #Type 5
    elif packet_type == 5:
        if data[0] > data[1]:
            total = 1
        else:
            total = 0
    #Type 6
    elif packet_type == 6:
        if data[0] < data[1]:
            total = 1
        else:
            total = 0
    #Type 7
    elif packet_type == 7:
        if data[0] == data[1]:
            total = 1
        else:
            total = 0

    return total, endpoint_total


def Parse_Subpackets_bits(packet):
    endpoint_total = 0
    end_points = []
    data = []
    types = []
    
    while packet:
        current_type = Get_Type(packet)
        types.append(current_type)
        if current_type == 4:
            data_term, endpoint = Literal(packet)
            data.append(data_term)
        else:
            data_term, endpoint = Operator(packet)
            data.append(data_term)
        
        end_points.append(endpoint)
        packet = packet[endpoint:]
    
    for term in end_points:
        endpoint_total += term

    return data, endpoint_total


def Parse_Subpackets_Count(packet, num_packets):
    endpoint_total = 0
    packet_count = 0
    end_points = []
    data = []
    types = []
    
    while packet and packet_count < num_packets:
        current_type = Get_Type(packet)
        types.append(current_type)
        if current_type == 4:
            data_term, endpoint = Literal(packet)
            data.append(data_term)
        else:
            data_term, endpoint = Operator(packet)
            data.append(data_term)

        packet_count += 1
        
        end_points.append(endpoint)
        packet = packet[endpoint:]


    for term in end_points:
        endpoint_total += term

    return data, endpoint_total


def Recursive_Packet(packet):
    version_sum = 0
    
    current_type = Get_Type(packet)
    if current_type == 4:
        version_total, endpoint = Literal(packet)
        version_sum += version_total
    else:
        version_total, endpoint = Operator(packet)
        version_sum += version_total

    return version_sum




if __name__ == '__main__':
    main()

