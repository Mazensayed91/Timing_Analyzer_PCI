
import os

def set_output_file(filename, dir=None):
    """ use for file outputs from dir  
        use file.write() and file.writelines() to write to the output file.
    """ 
    if dir == None:
        f = open(os.path.join('.',filename), "w")
    else:
        f = open(os.path.join(dir,filename), "w")
    return f

def get_time_scale_text(timescale):
    timescales = {
        1.0e-3:  "ms",
        1.0e-6:  "us",
        1.0e-9:  "ns",
        1.0e-12: "ps"
    }
    return timescales.get(timescale)

def get_ts_text(timescale):
    texts = {
        1e-3:  "e-3",
        1e-6:  "e-6",
        1e-9:  "e-9",
        1e-12: "e-12"
    }
        
    return texts.get(timescale)

def invert(state):
    states = {
        "H": "L",
        "1": "L",
        "L": "H", 
        "0": "H",
        "Z": "Z",
        "X": "X"
    }
    return states.get(state)


def get_voltage(state):
    states = {
        "H": 5.0,
        "1": 5.0,
        "L": 0.0, 
        "0": 0.0,
        "Z": 2.5
    }
    return states.get(state)

def get_state_format(bus):
    sf = bus.getStateFormat()
    return sf

def get_num_bits(bus):
    nb = bus.getNumBits()
    return nb

def get_end_time(timing_diagram):
    end_time = timing_diagram.getTimingDiagramEndTime()
    #print end_time
    return end_time

def get_ls_bit(name):
    beg_pos = name.find("[")
    mid_pos = name.find(":")
    end_pos = name.find("]")
    #print name[mid_pos+1:end_pos]
    return int(name[mid_pos+1:end_pos])

def get_ms_bit(name):
    beg_pos = name.find("[")
    mid_pos = name.find(":")
    end_pos = name.find("]")
    #print "beg_pos mid_pos end_pos %d %d %d" % (beg_pos,mid_pos,end_pos) 
    return int(name[beg_pos+1:mid_pos])

def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    # This commented-out version might be slightly faster as there are less
    # operations.
    #b = "".join([d[int(digit)] for digit in oct(n)])
    b = "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])
    return b

def hex2bin(n):
    b = int2bin(int(n, 16))
    return b

def convert_format(state, old_format, new_format, num_bits):
    """Converts a string to/from Hex or Bin"""

    if state == 'Z':
        return state

    if old_format == "Hex":
        int_value = int(state, 16)

    elif old_format == "Dec":
        int_value = int(state)

    elif old_format == "Bin":
        int_value = int(state, 2)

    if new_format == "Bin":
        bin_value = int2bin(int_value, num_bits)
        #if (num_bits > len(bin_value):
        #    for i in range(0, num_bits - len(bin_value):
        #        bin_value = '0' + bin_value;
        return bin_value
    #elif (new_format == "Hex"):
    #    hex_value = hex(int_value)
    #    if (num_bits > len(hex_value):
    #        for i in range(0, num_bits - len(hex_value):
    #            hex_value = '0' + hex_value;
    #    return hex_value
