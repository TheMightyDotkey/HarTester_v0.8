import ctypes

def Down(progType):

    x = progType

    if progType is 'Ford1fan':
        progLoc = 'W:\\Nick Wilczewski\\NX Data\\Programs\\Live Programs\\Ford_1fan_v1.2.nxf'
    
    elif progType is 'Ford2fan':
        progLoc = 'W:\\Nick Wilczewski\\NX Data\\Programs\\Live Programs\\Ford_2fan_v1.2.nxf'

    elif progType is 'NonFord1fan065':
        progLoc = 'W:\\Nick Wilczewski\\NX Data\\Programs\\Live Programs\\NonFord_1fan_v1.2.nxf'

    elif progType is 'NonFord2fan065':
        progLoc = 'W:\\Nick Wilczewski\\NX Data\\Programs\\Live Programs\\NonFord_2fan_v1.2.nxf'

    elif progType is 'NonFord1fan827':
        progLoc = 'W:\\Nick Wilczewski\\NX Data\\Programs\\Live Programs\\NonFord_1fan_v1.3.nxf'

    elif progType is 'NonFord2fan827':
        progLoc = 'W:\\Nick Wilczewski\\NX Data\\Programs\\Live Programs\\NonFord_2fan_v1.3.nxf'

    elif progType is 'Vactor':
        progLoc = 'W:\\Nick Wilczewski\\NX Data\\Programs\\Live Programs\\Vactor_v0.8.nxf'

    elif progType is 'VTEC2':
        progLoc = 'W:\\Nick Wilczewski\\NX Data\\Programs\\Live Programs\\VTEC2_131_845.nxf'

    elif progType is 'VTEC2REV2':
        progLoc = 'W:\\Nick Wilczewski\\NX Data\\Programs\\Live Programs\\VTEC2_REDU_REV4.nxf'


    nxtDll = ctypes.CDLL(r"C:\Program Files (x86)\Dynalab\NX Editor\NXComm.dll")

    nxtApiProto = ctypes.CFUNCTYPE (
        ctypes.c_int,
        ctypes.c_wchar_p,
        ctypes.c_char_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_uint,
        ctypes.c_bool
        )
    nxtApiParams = (1, "p1", 0), (1, "p2", 0), (1, "p3", 0), (1, "p4", 0), (1, "p5", 0), (1, "p6", 0),

    nxtApi = nxtApiProto (("NXDownloadEx", nxtDll), nxtApiParams)

    nxtApi('COM3', None, progLoc, None, 0, 0)

