def add_digital_clock(td, name, start_state, freq, duty_cycle = 50):
    """Add a DigitalClock to the timing diagram.

    Args:
        name:        A string that specifies the clock name\n
        freq:        A double that specifies the frequency\n
        start_state: A string that specifies the start state\n
        duty_cycle:  An integer that specifies the duty cycle. Optional

    Returns:
        dclk: A reference to the newly created DigitalClock object

    Examples:
        dclk = add_digital_clock(td, 'CLK25', 25.0e6, 'H')

        dclk = add_digital_clock(td, 'CLK25', 25.0e6, 'H', 40)
    """

    dclk = td.addDigitalClock(name, start_state, freq, duty_cycle)

    return dclk

def add_digital_bus(td, name, start_state, format='Hex'):
    """Add a DigitalBus to the timing diagram

    Args:
        name:        A string the specifies the bus name\n
        start_state: A string that specifies the start state\n
        format:      A string that specifies the format of the data\n

        The bus name should be in the following format: addr_bus[15:0]\n
        The bus format should be one of the following: 'Hex', 'Bin', 'Dec', 'Text'

    Returns:
        dbus: A reference to the newly created DigitalBus object

    Examples:
        dbus = add_digital_bus(td, 'ADDR[15:0]', 'Z')

        dbus = add_digital_bus(td, 'ADDR[15:0]', 'Z', 'Bin')
    """

    dbus = td.addDigitalBus(name, start_state, format)

    return dbus


def add_digital_signal(td, name, start_state):
    """Add a DigitalSignal to the timing diagram

    Args:
        name:        A string that specifies the signal name\n
        start_state: A string that specifies the start state

    Returns:
        dsig: A reference to the newly created DigitalSignal object

    Example:
        dsig = add_digital_signal(td, 'ENABLE', 'L')
    """

    dsig = td.addDigitalSignal(name, start_state)

    return dsig


def add_pulse_width_label(td, e1, e2, label, label_pos='Center'):
    """Add a PulseWidthLabel to the timing diagram

    This functions adds a PulseWidthLabel between 2 edges in the
    timing diagram.

    Args:
        td:        A reference to the timing diagram\n
        e1:        A reference to the first Edge\n
        e2:        A reference to the second Edge\n
        label:     A string that specifies the title to be displayed\n
        label_pos: A string that specifies the position of the label\n
                   This is an optional argument. It not specified, the
                   default is 'Center'\n
                   'Left' or 'Right' are also valid options.

    Returns:
        pwl: A reference to the newly created PulseWidthLabel object

    Examples:
        pwl = add_pulse_width_label(td, ed1, ed2, 'Period_Min')

        pwl = add_pulse_width_label(td, ed1, ed2, 'Period_Min', 'Left')
    """

    pwl = td.addPulseWidthLabel(e1,e2,label,label_pos)
    return pwl

def add_part_jitter_margin(td, name, pos_jitter, neg_jitter, desc):
    """Add a Part JitterMargin to the file library

    Args:
        td: A reference to the TimingDiagram\n
        name: A string that specifies the name of the part jitter\n
        pos_jitter: A double that specifies the possible positive jitter change\n
        neg_jitter: A double that specifies the possible negative jitter change\n
        desc: A string that specifies the description of the Part JitterMargin

    Returns:
        pjm: A reference to newly created Part JitterMargin.

    Example:
        osc1_pjm = add_part_jitter_margin(td, 'OSC1_JITTER', 1.2, 1.4, 'XYZ Part Jitter')
    """

    pjm = td.addJitterMargin(name, pos_jitter * 1000, neg_jitter * 1000, desc)
    return pjm


def add_jitter_margin(ed, part_jitter_margin):
    """Add a JitterMargin to an Edge

    Jitter is added to an Edge. The minimum edge time is set to the edge
    time minus the negative jitter, and the maximum edge time to the edge
    time plus the positive jitter.

    Args:
        ed: A reference to the Edge\n
        part_jitter_margin: A reference to a Part JitterMargin defined in the file library

    Returns:
        jm: A reference to newly created JitterMargin.

    Example:
        jm = add_jitter_margin(ed1, osc1_pjm)
    """

    jm = ed.addJitterMargin(part_jitter_margin)
    return jm


def add_delay(td, part_delay, edge_from, edge_to):
    """Add a Delay to the timing diagram


    Args:
        td: A reference to the TimingDiagram\n
        part_delay: A reference to a PartDelay defined in the file library
        edge_from: An Edge that specifies the source of the Delay\n
        edge_to: An Edge that specifies the destination of the Delay\n

    Returns:
        cnstrnt: A reference to newly created Constraint.

    Example:
        c1 = add_constraint(td, pc, ed1, ed2)
    """

    dly = td.addDelay(part_delay, edge_from, edge_to)
    return dly


def add_part_delay(td, name, min, typ, max, desc):
    """Add a PartDelay to file library

    This function is used to add a PartDelay to the file library.
    This could represent specifications from a manufacturer for a part.

    Args:
        name: A string the specifies the name of the PartDelay\n
        min: A double that specifies the minimum Delay time\n
        typ: A double that specifies the typical Delay time\n
        max: A double that specifies the maximum Delay time\n
        desc: A string that specifies the description of the PartDelay

    Returns:
        pd: A reference to newly created PartDelay.

    Example:
        pd = add_part_delay(td, 'tprop', 4, 7, 9)
    """

    pd = td.addPartDelay(name, min * 1000, typ * 1000, max * 1000, desc)
    return pd

def add_constraint(td, part_constraint, edge_from, edge_to):
    """Add a Constraint to the timing diagram


    Args:
        td: A reference to the TimingDiagram\n
        part_constraint: A reference to a PartConstraint defined in the file library
        edge_from: An Edge that specifies the source of the Constraint\n
        edge_to: An Edge that specifies the destination of the Constraint\n

    Returns:
        cnstrnt: A reference to newly created Constraint.

    Example:
        c1 = add_constraint(td, pc, ed1, ed2)
    """

    cnstrnt = td.AddConstraint(part_constraint, edge_from, edge_to)
    return cnstrnt


def add_part_constraint(td, name, min, max, desc):
    """Add a PartConstraint to file library

    This function is used to add a PartConstraint to the file library.
    This could represent specifications from a manufacturer for a part.

    Args:
        name: A string the specifies the name of the PartConstraint\n
        min: A double that specifies the minimum constraint time\n
        max: A double that specifies the maximum constraint time\n
        desc: A string that specifies the description of the PartConstraint

    Returns:
        pc: A reference to newly created PartConstraint.

    Example:
        pc = add_part_constraint(td, 'tsetup', 4, 7)
    """

    pc = td.addPartConstraint(name, min * 1000, max * 1000, desc)
    return pc

def add_statebar(td, edge, label, line_style, xoffset, yoffset):
    """Add a StateBar to an Edge

    This function adds a StateBar to an Edge in any signal.
    StateBars are vertical lines with labels that are displayed
    for a clock domain.

    Args:
        td: A reference to the TimingDiagram\n
        edge: A reference to the Edge\n
        label: A string that specifies the new state\n
        line_style: A string that specifies the line style. 'Solid' or 'Dashed'\n
        xoffset: An integer that specifies the label offset in pixels horizontally\n
        xoffset: An integer that specifies the label offset in pixels vertically\n


    Returns:
        sb: A reference to newly created StateBar.

    Example:
        sb = add_statebar(td, ed1, 'WAIT', 'Dashed', 0, 0)
    """

    sb = td.addStateBar(edge, label, line_style, xoffset, yoffset)
    return sb

def get_edge(sig, edge_num):
    """Get the specific Edge from the signal

    This function gets the x Edge from the signal. x is the index into the
    edge list stored in the signal.

    Args:
        sig: A reference to signal that contains the Edge\n
        edge_num: An integer that is the index of the signal edge list

    Returns:
        ed: A reference to Edge stored in the edge list at index edge_num

    Example:
        ed = get_edge(clk_ena, 1)
    """

    el = sig.getEdgeList()
    ed = el[edge_num]
    return ed

def get_edge_list(sig):
    """Get the edge list from the signal

    This function gets the edge list from the signal. This list contains
    all the Edges for the signal.

    Args:
        sig: A reference to signal that contains the edge list

    Returns:
        el: A reference to edge list

    Example:
        el = get_edge_list(clk_ena)
    """
    el = sig.getEdgeList()
    return el

def add_edge(sig, edge_time, edge_state):
    """ Add a new Edge to the specified Signal

    This function adds a new Edge to the signal. The signal changes to the
    new state after the time specified.

    Args:
        sig: A reference to the signal for the new Edge\n
        edge_time: A double that specifies when the Edge is added and
        the signal changes state\n
        edge_state: A string that specifies the new state of the signal

    Returns:
        ed: A reference to newly created Edge

    Example:
        ed1 = add_edge(fast_clock, 110.0, 'H')

    """

    #print "add_edge time %d state %s" %(edge_time, edge_state)
    if sig.type == 'DigitalBus':
        if sig.allZs(edge_state) == True:
            edge_state = 'Z'
    ed = sig.addEdge(edge_time * 1000.0, edge_state)
    #ed = sig.addEdge(edge_time * 1000, edge_time_1 * 1000, edge_state)
    return ed

def add_edge_1(sig, edge_time, edge_state):
    #print "add_edge time %d state %s" %(edge_time, edge_state)
    ed = sig.addEdge(edge_time * 1000.0, edge_state)
    #ed = sig.addEdge(edge_time, edge_time_1, edge_state)
    return ed

def add_edge_margin(sig, edge_time_min, edge_time_max, edge_state):
    """ Add a new Edge with uncertainty to the specified Signal

    This function adds a new Edge to the signal. The state changes
    after the max time specified. This is used to show the uncertainty
    in time that it takes for signal to change state.

    Args:
        sig: A reference to the signal for the new Edge\n
        edge_time_min: A double that specifies when the minimum time of the Edge\n
        edge_time_max: A double that specifies when the maximum time of the Edge\n
        edge_state: A string that specifies the new state of the signal

    Returns:
        ed: A reference to newly created Edge

    Example:
        ed1 = add_edge_margin(clk_ena, 110.0, 114.0 'H')

    """

    ed = sig.addEdge(edge_time_min * 1000, edge_time_max * 1000, edge_state)
    return ed


def add_pulse(sig, pulse_start_time, pulse_end_time, pulse_state):
    add_edge(sig, pulse_start_time, pulse_state)
    add_edge(sig, pulse_end_time, get_state_at_time(sig,pulse_start_time))


def get_file_name(td):
    """Gets the name of the current timing diagram"""

    file_name = td.getFileName();
    return file_name


def get_edit_signal_list(td):
    """Get the list of signals that are selected in the timing diagram

    This function returns a list of selected signals from the timing diagram

    Args:
        td: A reference to the timing diagram

    Returns:
        sig_list: A list of signals selected in the timing diagram

    Example:
        sig_list = get_edit_signal_list(td)
    """

    sig_list = td.getEditSigList()
    return sig_list


def get_signal_list(td):
    """Get the list of signals from the timing diagram

    This function returns a list of visible signals from the timing diagram

    Args:
        td: A reference to the timing diagram

    Returns:
        sig_list: A list of signals displayed in the timing diagram

    Example:
        sig_list = get_signal_list(td)
    """

    sig_list = td.getSignalList()
    return sig_list


def get_state_at_time(sig, state_time):
    """Get the state of the signal at give time

    Args:
        sig: A reference to the Signal\n
        state_time: A long that specifies the time * 1000

    Returns:
        state: A string that specifies the state of the signal at the time

    Example:
        next_state = get_state_at_time(clk_ena, 335000)
    """

    state = sig.getStateAtTime(long(state_time * 1000.0))
    return state


def get_last_state(ed):
    ls = ed.getLastState()
    return ls

def get_next_state(ed):
    ns = ed.getNextState()
    return ns

def get_pt(ed, pos, case):
    """Get the Edge time at the position for the minimum or maximum case

    Args:
        ed: A reference to the Edge\n
        pos: An integer that specifies the edge postion. 1 or 2 or 3\n
        case: A string that specifies the case. 'min' or 'max'

    Returns:
        et: A long that is the time of the Edge

    Examples:
        et = get_pt(ed1, 1, 'min')

        et = get+pt(ed1, 2, 'max')
    """

    et = ed.getPt2Min()
    if pos == 1:
        if case == 'min':
           et = ed.getPt1Min()
        else:
            et = ed.getP1Max()
    elif pos == 2:
        if case == 'min':
            et = ed.getPt2Min()
        else:
            et = ed.getPt2Max()
    else:
        if case == 'min':
            et = ed.getPt3Min()
        else:
            et = ed.getPt3Max()

    et = et / 1000.0
    return et 


def get_pt1_min(ed):
    """Get the Edge time at point 1 for minimum case

    Args:
        ed: A reference to the Edge\n

    Returns:
        et: A long that is the time of the Edge at point 1 minimum case

    Examples:
        et = get_pt1_min(ed1)
    """

    pt1_min = ed.getPt1Min() / 1000.0
    return pt1_min


def get_pt2_min(ed):
    """Get the Edge time at point 2 for minimum case

    Args:
        ed: A reference to the Edge\n

    Returns:
        et: A long that is the time of the Edge at point 2 minimum case

    Examples:
        et = get_pt2_min(ed1)
    """

    pt2_min = ed.getPt2Min() / 1000.0
    return pt2_min 


def get_pt3_min(ed):
    """Get the Edge time at point 3 for minimum case

    Args:
        ed: A reference to the Edge\n

    Returns:
        et: A long that is the time of the Edge at point 3 minimum case

    Examples:
        et = get_pt3_min(ed1)
    """

    pt3_min = ed.getPt3Min() / 1000.0
    return pt3_min


def get_last_edge_pt2(sig):
    print "get_last_edge_pt2 %d" % sig.getLastEdgePt2()
    pt2 = sig.getLastEdgePt2() / 1000.0
    return pt2


def get_name(sig):
    """Get the name of a signal

    Args:
        sig: A reference that specifies the signal

    Returns:
        sig_name: A string that is the signal name

    Example:
        sig_name = get_name(clk1)
    """

    sig_name = sig.getSignalName().getName(1)
    return sig_name

def get_start_state(sig):
    """Get the start state of a signal

    Args:
        sig: A reference that specifies the signal

    Returns:
        ss: A string that is specifies the start state of the signal

    Example:
        ss = get_start_state(clk1)
    """

    ss = sig.getStartState()
    return ss

def get_time_scale(td):
    """Get the time scale of the timing diagram

    Args:
        td: A reference of the TimingDiagram

    Returns:
        ts: A double that is specifies the time scale

    Example:
        ts = get_time_scale(td)
    """

    ts = td.getTimeScale()
    return ts

def set_clock_start_delay(clk, dly_time):
    clk.setStartDelay(dly_time * 1000)

def set_end_time(td, end_time):
    td.setEndTime(end_time)

def set_rise_time(sig, rise_time):
    """Sets the rise time of a signal

    This function sets the time of the rising transistion.

    Args:
        sig: A reference that specifies the signal\n
        fall_time: A double that specifies the rise time

    Example:
        set_rise_time(clk1, 4)
    """

    sig.setRiseTime(rise_time * 1000)


def set_fall_time(sig, fall_time):
    """Sets the fall time of a signal

    This function sets the time of the falling transistion.

    Args:
        sig: A reference that specifies the signal\n
        fall_time: A double that specifies the fall time

    Example:
        set_fall_time(clk1, 4)
    """

    sig.setFallTime(fall_time * 1000)


def set_end_time(td, end_time):
    """Sets the end time of a TimingDiagram

    Args:
        td: A reference to the TimingDiagram\n
        end_time: A long that specifies the TimingDiagram end time\n
                  In the time scale set

    Example:
        set_end_time(td1, 1600)
    """

    td.setEndTime(end_time)


def set_start_time(td, start_time):
    """Sets the start time of a TimingDiagram

    Args:
        td: A reference to the TimingDiagram\n
        end_time: A long that specifies the TimingDiagram start time\n
                  In the time scale set

    Example:
        set_end_time(td1, 100)
    """

    td.setStartTime(start_time)

def start_script(td):
    """Start script disables the Graphics functions

    Args:
        td: A reference to the TimingDiagram\n

    Example:
        start_script(td1)
    """

    td.startScript()


def stop_script(td):
    """Stop script enable the Graphics functions

    Args:
        td: A reference to the TimingDiagram\n

    Example:
        start_script(td1)
    """

    td.stopScript()

def zoom_in_full(td):
    td.zoomFullCommand()
