import sys
import csv

# -----------------------STATIC_DATA---------------------------------------------------#
filename = "scripts/data.csv"
# -------------------------------------------------------------------------------------#
# -----------------------DYNAMIC_DATA--------------------------------------------------#
data_c_be = {}
counter = 1
cycles_flag = 0
line_mod = {}
# -------------------------------------------------------------------------------------#

# ----------------------Read csv file--------------------------------------------------#
with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        line_mod['Data'] = line['Data'][1:]
        line_mod['C_BE'] = line['C_BE'][1:]
        line_mod['TRDY'] = int(line['TRDY'])
        line_mod['Repeated'] = False
        data_c_be["c" + str(counter)] = line_mod.copy()

        if line_mod['TRDY'] == 1:
            cycles_flag += 1
            line_mod['TRDY'] = 0
            line_mod['Repeated'] = True
            counter += 1
            data_c_be["c" + str(counter)] = line_mod.copy()
        counter += 1
# --------------------------------------------------------------------------------------#

print(cycles_flag)
data_words = len(data_c_be)
#data_c_be['c2']['TRDY']=0
#data_c_be['c3']['TRDY']=0

cycles_flag = 0
cycles_num = data_words + cycles_flag + 3

print(data_c_be, len(data_c_be))

sys.path.append('./TimingAnalyzer.jar')
sys.path.append('jlib/freehep-graphicsio-2.4.jar')
sys.path.append('jlib/freehep-io-2.0.2.jar')
sys.path.append('jlib/freehep-graphics2d-2.4.jar')
sys.path.append('jlib/freehep-graphicsio-ps-2.4.jar')
sys.path.append('jlib/freehep-graphicsio-pdf-2.4.jar')
sys.path.append('jlib/freehep-graphicsio-emf-2.4.jar')
sys.path.append('jlib/freehep-graphicsio-svg-2.4.jar')
sys.path.append('jlib/jython.jar')
sys.path.append('./scripts')

from org.dmad.ta import TimingAnalyzer

taApp = TimingAnalyzer()

from ta_py_lib.ta.app import *
from ta_py_lib.td.logic import *
from ta_py_lib.td.commands import *

td = new_timing_diagram(taApp)
start_script(td)

clk_freq = 33.0e6
clk_per  = 1.0e9 / clk_freq

clk     = add_digital_clock(td, "CLK", "H", clk_freq)
frame   = add_digital_signal(td, "FRAME", "H")
ad      = add_digital_bus(td, "AD[31:0]", "Z", "Text")
c_be    = add_digital_bus(td, "C/BE[3:0]", "Z", "Text")
trdy    = add_digital_signal(td, "TRDY", "H")
irdy    = add_digital_signal(td, "IRDY", "H")
devsel  = add_digital_signal(td, "DEVSEL", "H")

trdy_high=0
def add_edges(clk_cycle, length, pas=0):
   global trdy_high
   fe_time = (clk_cycle * clk_per) + (clk_per / 2.0) + 2.0
   re_time = clk_cycle * clk_per + 2.0

   if clk_cycle == 0:
       add_edge(frame, fe_time, "L")
       add_edge(ad, fe_time, "ADD")
       add_edge(c_be, fe_time, "READ")
   elif clk_cycle == 1:
       add_edge(ad, fe_time, "Z")
       add_edge(c_be, fe_time, data_c_be["c1"]["C_BE"])
       add_edge(irdy, fe_time, "L")

   elif clk_cycle == 2:
       add_edge(ad, fe_time, data_c_be["c1"]["Data"])
       add_edge(devsel, fe_time, "L")
       add_edge(trdy, fe_time, "L")

   elif clk_cycle == length:
       pass

   elif clk_cycle == length-1:
       add_edge(ad, fe_time, "Z")
       add_edge(c_be, fe_time, "Z")
       add_edge(trdy, fe_time, "H")
       add_edge(irdy, fe_time, "H")
       add_edge(devsel, fe_time, "H")
   elif clk_cycle == length-2:
       add_edge(frame, fe_time, "H")
       add_edge(ad, fe_time, data_c_be["c" + str(clk_cycle - 1)]['Data'])
       add_edge(c_be, fe_time, data_c_be["c" + str(clk_cycle - 1)]['C_BE'])

   elif data_c_be["c" + str(clk_cycle)]['Repeated']:
       #add_edge(ad, fe_time, data_c_be["c" + str(clk_cycle)]['Data'])
       #add_edge(c_be, fe_time, data_c_be["c" + str(clk_cycle)]['C_BE'])
       add_edge(trdy, fe_time, "H")
       trdy_high=1
       return

   else:
       if trdy_high == 1:
           trdy_high=0
           add_edge(trdy, fe_time, "L")

       add_edge(ad, fe_time, data_c_be["c"+str(clk_cycle-1)]['Data'])
       add_edge(c_be, fe_time, data_c_be["c"+str(clk_cycle-1)]['C_BE'])


trdy_high=0
print(cycles_num-1)
clk_cycle_delay = 0
for clk_cycle in range(0, cycles_num):
    #fe_time = (clk_cycle * clk_per) + (clk_per / 2.0) + 2.0

    #if 1 < clk_cycle < cycles_num-1 and data_c_be["c" + str(clk_cycle - 1)]['TRDY'] == 1:
    #    trdy_high=1
        #clk_cycle -= 1
    #    add_edge(trdy, fe_time, "H")
    #    add_edge(trdy, fe_time, "L")


    #if trdy_high == 1:
    #    trdy_high = 0
    #    add_edge(trdy, fe_time, "L")

    add_edges(clk_cycle, cycles_num)

#state_list = ['NU','S1','S2','S2','S2','S3','S0']

#clk_cycle = 0
#for clk_edge in get_edge_list(clk):
#    if clk_cycle == 7:
#        break
#    if get_next_state(clk_edge) == "H":
#        add_statebar(td, clk_edge,state_list[clk_cycle],"Dashed",0,0)
#        clk_cycle += 1

set_end_time(td, 400)
stop_script(td)

