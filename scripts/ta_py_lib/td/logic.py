from org.dmad.ta.logic import And2
import java.util.ArrayList as ArrayList

def add_dff_re(td, din, clk, q_name, setup, hold, clk2q):
    period = clk.getPeriod() / td.getTimeScale() * 1000.0
    ls = din.getStartState()  
    qout = td.addDigitalSignal(q_name, ls)
    clk_ed_list = clk.getEdgeList()
    for clk_ed in clk_ed_list:
        if clk_ed.getNextState() == "H":
            clk_et_min = clk_ed.getPt2Min()
            clk_et_max = clk_ed.getPt2Max()
            ns = din.getStateAtTime(clk_et_min)
            #print "edge time %d next state %s" % (et,ns)
            if (ns != ls):
                sigQ_edge = qout.addEdge(clk_et_min,ns)
                td.addDelay(clk2q,clk_ed,sigQ_edge)
                din_led = din.getLastEdge(clk_et_min)
                din_let_max = din_led.getPt2Max() 
                if clk_et_min - din_let_max < period:
                	c1 = td.addConstraint(setup, din_led, clk_ed)
                	c1.setYPos(din.getLowY() + 10)
                din_ned = din.getNextEdge(clk_et_max)
                if (din_ned != None):
                    din_net_min = din_ned.getPt2Min()
                    if din_net_min - clk_et_max < period:
                        td.addConstraint(hold, clk_ed, din_ned) 
            ls = ns
    return qout


def add_comb_logic(td, sin, so_name, pd):
    cl_out = td.addDigitalSignal(so_name, sin.getStartState())
    for sin_ed in sin.getEdgeList():
        cl_ed = cl_out.addEdge(sin_ed.getPt2Min(), sin_ed.getNextState())
        td.addDelay(pd, sin_ed, cl_ed)

    return cl_out

def add_and2(td, ain, bin, c_name, tpd):
    c_out = td.addDigitalSignal(c_name, ain.getStartState() and bin.getStartState())

def add_and2(td, s1, s2, sn, tplh_pdly, tphl_pdly):
    sig_list = ArrayList() 
    sig_list.add(s1);
    sig_list.add(s2);
    a2 = And2(td, sig_list, sn, tplh_pdly, tphl_pdly)
    td.addToSignalList(a2)
    td.repaintDiagram()

