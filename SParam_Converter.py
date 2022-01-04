import re
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from numpy.core.defchararray import isdigit

s_parameter_enum = 2
freq_unit = 'MHz'


def Main():
    print('Please select the S Parameter file you\'d like to convert')
    try:
        input_format, input_headings, sparam_list = Input_to_list(Gui_file_path().strip())
        attenuation_magnitudes = Attenuation_snp(input_headings, input_format[2], sparam_list)
        Plot_attenuation(attenuation_magnitudes)
        
        low_freq = None
        high_freq = None
        while(type(low_freq) is not float):
            try: 
                low_freq = float(input(f'Low end of frequency range in {freq_unit} (e notation is valid ex: 4.8e9): '))
            except ValueError:
                print('That wasn\'t a valid number. Please try again\n')
        while(type(high_freq) is not float):
            try:
                high_freq = float(input(f'High end of frequency range in {freq_unit} (e notation is valid ex: 4.8e9): '))
            except ValueError:
                print('That wasn\'t a valid number. Please try again\n')
        Range_stats(low_freq, high_freq, attenuation_magnitudes)
        input('\nPress enter to exit')
    except:
        print("Exception occurred. Exiting.")


def Gui_file_path():
    Tk().withdraw()
    filename = askopenfilename()
    return filename


def Input_to_list(path):
    #find_start_pattern = r'^(?![#|!|\s]).*/gm'
    #find_start_reg = re.compile(find_start_pattern)
    start_data = False
    has_headings = False
    input_list = []

    with open (path, 'rt') as input_text:
        for line in input_text:
            if(not start_data):             #line starts with a #. This is the first useful data
                if (line[0] == '#'):
                    start_data = True
                    input_sparam_format = line
            elif (line.strip()[0].isnumeric()):     #line starts with a value/number after finding the # line
                input_list.append(line.strip())
            else:                           #line starts with a ! after finding the # (appears to only occur once, only in some files)
                input_sparam_headings = line
                has_headings = True

    input_format = re.findall( r'(?<=\s)[\d\w]+', input_sparam_format.strip())
    if (has_headings):
        input_headings = re.findall(r'(?<=\s\s)[\d\w]*(?=\s)|(?<=\s)[\d\w]*(?=\s\s)|(?<=\s)[\d\w]*(?=$)', input_sparam_headings.strip())
    else:
        if (path[-2] == '1'):
            input_headings = ['Freq','S11','S11_2']
        elif (path[-2] == '2'):
            input_headings = ['Freq','S11','S11_2','S21','S21_2','S12','S12_2','S22','S22_2']
        elif (path[-2] == '3'):
            input_headings = ['Freq','S11','S11_2','S21','S21_2','S31','S31_2','S12','S12_2','S22','S22_2','S32','S32_2','S13','S13_2','S23','S23_2','S33','S33_2']
        elif (path[-2] == '4'):
            input_headings = ['Freq','S11','S11_2','S21','S21_2','S31','S31_2','S41','S41_2','S12','S12_2','S22','S22_2','S32','S32_2','S42','S42_2','S13','S13_2','S23','S23_2','S33','S33_2','S43','S43_2','S14','S14_2','S24','S24_2','S34','S34_2','S44','S44_2']
        elif (path[-2] == '5'):
            input_headings = ['Freq','S11','S11_2','S21','S21_2','S31','S31_2','S41','S41_2','S51','S51_2','S12','S12_2','S22','S22_2','S32','S32_2','S42','S42_2','S52','S52_2','S13','S13_2','S23','S23_2','S33','S33_2','S43','S43_2','S53','S53_2','S14','S14_2','S24','S24_2','S34','S34_2','S44','S44_2','S54','S54_2','S15','S15_2','S25','S25_2','S35','S35_2','S45','S45_2','S55','S55_2']

    #find number of values per line
    find_values_pattern = re.compile(r'-?\d+\.\d+e-\d+|-?\d+\.\d+|\-?\d+')
    find_values_match = re.findall(find_values_pattern, input_list[2])
    values_per_line = len(find_values_match)
    sparam_list = np.zeros((len(input_list),values_per_line)) #Accessed as follows: [line #][parameter]

    for line_number, line in enumerate(input_list):
        delimited = re.findall(find_values_pattern, line)
        for parameter_number,number in enumerate(delimited):
            sparam_list[line_number][parameter_number] = number
    
    global freq_unit
    freq_unit = input_format[0]
    return input_format, input_headings, sparam_list


def Attenuation_snp(headings, snp_format, sparameters): #j at the end of a number is complex/imaginary
    number_of_ports = np.sqrt(len(headings)) - 1   #input/output port order is not consistent. Check headings
    
    if (snp_format.upper() == 'RI'): #Real/Imaginary
        RI_magnitude = np.zeros((int((len(headings)-1)/2 + 1),len(sparameters))) #Access as follows: [S-Parameter (enumerated) + 1 for a freq column][line #]
        for line,measurement in enumerate(sparameters):
            RI_magnitude[0][line] = measurement[0]
            for index in range(1,len(measurement)-1,2):
                RI_magnitude[int(np.ceil(index/2))][line] = 20*np.log10(np.sqrt(measurement[index]**2 + measurement[index+1]**2))
        return RI_magnitude
    elif (snp_format.upper() == 'MA'): #Magnitude/Angle
        MA_magnitude = np.zeros((int((len(headings)-1)/2 + 1),len(sparameters)))
        for line,measurement in enumerate(sparameters):
            MA_magnitude[0][line] = measurement[0]
            for index in range(1,len(measurement)-1,2):
                MA_magnitude[int(np.ceil(index/2))][line] = 20*np.log10(measurement[index])
        return MA_magnitude
    elif (snp_format.upper() == 'DB'): #Magnitude in Decibels/Phase
        DB_magnitude = np.zeros((int((len(headings)-1)/2 + 1),len(sparameters)))
        for line,measurement in enumerate(sparameters):
            DB_magnitude[0][line] = measurement[0]
            for index in range(1,len(measurement)-1,2):
                DB_magnitude[int(np.ceil(index/2))][line] = measurement[index]
        return DB_magnitude
    else:
        print('Format error. Please edit to include one of the following input formats: RI, MA, DB')
    


def Plot_attenuation(sparam_magnitudes):
    #one_port = ['S11']
    #two_port = ['S11','S21','S12','S22']
    #three_port = ['S11','S21','S31','S12','S22','S32','S13','S23','S33']
    #four_port = ['S11','S21','S31','S41','S12','S22','S32','S42','S13','S23','S33','S43','S14','S24','S34','S44']
    #five_port = ['S11','S21','S31','S41','S51','S12','S22','S32','S42','S52','S13','S23','S33','S43','S53','S14','S24','S34','S44','S54','S15','S25','S35','S45','S55']
    x = sparam_magnitudes[0][:]
    y = sparam_magnitudes[s_parameter_enum][:]
    plt.plot(x,y)
    plt.xlabel(freq_unit)
    plt.ylabel('dB')
    plt.title('Attenuation')
    plt.show(block=False)


def Range_stats(low_freq, high_freq, attenuations):
    low_index = 0
    while (attenuations[0][low_index] < low_freq): #the 0 will always be for the frequency array
        low_index += 1

    high_index = low_index
    while (attenuations[0][high_index] < high_freq):
        high_index += 1
    high_index -= 1

    min_freq = attenuations[0][low_index]
    max_freq = attenuations[0][low_index]
    min = attenuations[s_parameter_enum][low_index] #these are for initializing the min and max to some value for the s parameter we want to evaluate
    max = attenuations[s_parameter_enum][low_index]
    dB_total = 0
    power_total = 0
    for index in range(low_index, high_index):
        dB_total += attenuations[s_parameter_enum][index]
        power_total += 10**(attenuations[s_parameter_enum][index]/20)
        if (attenuations[s_parameter_enum][index] < min):
            min = attenuations[s_parameter_enum][index]
            min_freq = attenuations[0][index]
        if(attenuations[s_parameter_enum][index] > max):
            max = attenuations[s_parameter_enum][index]
            max_freq = attenuations[0][index]

    num_of_indices = high_index - low_index + 1
    dB_avg = dB_total / num_of_indices
    power_avg = 20*np.log10(power_total / num_of_indices)

    print(f'\nStatistics between {low_freq} {freq_unit} and {high_freq} {freq_unit}:\nMin: {min} @ {min_freq} {freq_unit}\nMax: {max} @ {max_freq} {freq_unit}\nAverage Power: {power_avg}')


if __name__ == '__main__':
    Main()