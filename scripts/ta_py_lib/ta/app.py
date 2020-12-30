
def get_timing_diagram(taApp):
    """Get the current timing diagram

    This function returns a reference to the current
    timing diagram being displayed.

    Args:
        taApp: A reference to the TimingAnalyzer

    Returns:
        td: A reference to the displayed timing diagram

    Example:
        td = get_timing_diagram(taApp)
    """

    td = taApp.getTimingDiagram()

    return td



def new_timing_diagram(taApp, dir=None, file_name=None):
    """Start a new timing diagram.

    This function initializes a new timing diagram and 
    displays in the a new tabbed window.

    Args:
        dir: specifies the directory to save the timing diagram file\n
        file_name: Specifies the file name used for this new timing diagram.

    Returns:
        td: A reference to the new timing diagram

    Examples:
        td = new_timing_diagram(taApp) 

        td = new_timing_diagram(taApp, 'scripts', 'PCI_Read.tim')
    """

    if file_name == None:
        taApp.fileNew("TimingDiagram")
    else:
        taApp.fileNew("TimingDiagram",dir,file_name)

    td = taApp.getTimingDiagram()
    return td


def get_file_name(taApp):
    """Get the file name of the current timing diagram

    Args:
        taApp: A reference to the TimingAnalyzer 

    Returns: 
        file_name:  The file name String 

    Example:
        fn = get_file_name(taApp)
    """

    file_name = taApp.getFileName()

    return file_name


def get_abs_file_path(taApp):
    """Get the absolute file path for the current timing diagram

    Args:
        taApp: A reference to the TimingAnalyzer 

    Returns: 
        file_dir:  The directory path name String 

    Example:
        fp = get_abs_file_path(taApp)
    """

    td = taApp.getTimingDiagram()
    file_dir = td.getDirectory()

    return file_dir


def file_save(taApp):
    """Save the current timing diagram

    This function save the current timing diagram using the dir and file_name.

    Args:
        taApp: A reference to TimingAnalyzer

    Returns: 
        None: 

    Example:
        file_save(taApp)
    """

    taApp.fileSave()
