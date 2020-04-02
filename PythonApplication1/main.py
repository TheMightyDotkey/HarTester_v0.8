print('Startup')
import PySimpleGUI as sg
import NXDown as nxd
import threading
import subprocess
import sys

def Splash():
    
    print('a dead cat')

    layout = [[sg.Text('Harness Tester Program Selector')]]
    window = sg.Window('Title', layout, no_titlebar = True, auto_close = True, auto_close_duration = 3)
    window.Read()

    return

#This function gathers the data on what harnesses are being tested from the operator.
#It returns events and values

def CheckBoxWindowVactor():

    layout = [
        
        [sg.Text('Select All Harnesses to Be Tested', font = ('Helvetica', 24))],
		[sg.Checkbox('269022 - Dual Pressure ', key = '-269022-')],
		[sg.Checkbox('269024 - Ground', key = '-269024-', default = True)],
		[sg.Checkbox('269025 - Temperature', key = '-269025-', default = True)],
		[sg.Checkbox('269026 - Pressure', key = '-269026-', default = True)],
		[sg.Checkbox('269028 - Generator', key = '-269028-')],
	    #[sg.Checkbox('269030 / 269300 / 269308 in PTO', key = '-PTO-')],
		[sg.Checkbox('269030 / 269300 / 269308 in AUX', key = '-AUX-', default = True)],
		[sg.Radio('269828 - Underhood', "UH", key = '-269828-'), sg.Radio('269840 - Underhood', "UH", key = '-269840-'), sg.Radio('273434 - Underhood', "UH", key = '-273434-', default = True), sg.Radio('273620 - Underhood', "UH", key = '-273620-')],
        [sg.Radio('274339 - Underhood', "UH", key = '-274339-'), sg.Radio('274340 - Underhood', "UH", key = '-274340-'), sg.Radio('277136 - Underhood', "UH", key = '-277136-')],
        [sg.Checkbox('275469 - Display', key = '-275469-', default = True)],
        [sg.Radio('276206 - J1939', "J1939", key = '-276206-'), sg.Radio('276757 - J1939', "J1939", key = '-276757-'), sg.Radio('None - J1939', "J1939", key = '-NoneJ1939-', default = True)],
        [sg.Checkbox('277319 - Remote Start', key = '-277319-')],
        [sg.Checkbox('277896 - Generator and Aux. Hydro. Splitter', key ='-277896-')],
        [sg.Checkbox('277898 - Hydraulic', key ='-277898-')],
        [sg.Checkbox('278610 - Muncie PTO PWM', key = '-278610-')],
        [sg.Checkbox('279202 - Vactor Remote Start', key = '-279202-', default = True)],
        [sg.Checkbox('279372 - PTO Vactor', key = '-279372-', default = True)],
		[sg.OK(pad = (20, 20)), sg.Cancel(pad = (20, 20))]

        ]

    window = sg.Window('Vactor Harnesses', layout)

    event, values = window.Read()

    print(event, values)

    window.Close()

    return (event, values)

#This function gathers the data on what harnesses are being tested from the operator.
#It returns events and values

def CheckBoxWindowVTEC2():

    layout = [
        
        [sg.Text('Select All Harnesses to Be Tested', font = ('Helvetica', 24))],
		[sg.Checkbox('279173 - Generator ', key = '-279173-')],
		[sg.Checkbox('279174 - Standard Temp & Press', key = '-279174-', default = True)],
		[sg.Checkbox('279174 - Redundant Temp & Press', key = '-279174R-', default = False)],
		[sg.Checkbox('279184 / 279187 & 279860 - PTO 1', key = '-PTO1-', default = True)],
        [sg.Checkbox('279184 / 279187 & 279652 - PTO 2', key = '-PTO2-', default = False)],
		[sg.Checkbox('279274 - Remote Start', key = '-279274-')],
		[sg.Checkbox('279275 - Dual PSI', key = '-279275-', default = False)],
        [sg.Checkbox('279600 & 279859 - No Load', key = '-279600-', default = False)],
        [sg.Checkbox('280298 - Oil Sensor', key = '-280298-', default = False)],
        [sg.Radio('279175 / 279886 / 279983 / 280423 - J1939', "J1939", key = '-279175-', default = True), sg.Radio('279943 - J1939', "J1939", key = '-279943-'), sg.Radio('None - J1939', "J1939", key = '-NoneJ1939-')],
		[sg.OK(pad = (20, 20)), sg.Cancel(pad = (20, 20))]

        ]

    window = sg.Window('V-TEC II Harnesses', layout)

    event, values = window.Read()

    print(event, values)

    window.Close()

    return (event, values)


#This function gathers the data on what harnesses are being tested from the operator.
#It returns events and values

def CheckBoxWindowVTEC2REV2():

    layout = [
        
        [sg.Text('Select Relevant Options', font = ('Helvetica', 24))],
		[sg.Checkbox('278610 - PWM PTO', key = '-278610-')],
        [sg.Radio('Brushed Fan(s)', "Fans", key = '-brushedfan-', default = True), sg.Radio('Brushless Fan(s)', "Fans", key = '-brushlessfan-', default = True)],
        [sg.Radio('279175 / 279886 / 279983 / 280423 / NonMRS - J1939', "J1939", key = '-279175-', default = True), sg.Radio('279943 MRS - J1939', "J1939", key = '-279943-')],
		[sg.OK(pad = (20, 20)), sg.Cancel(pad = (20, 20))]

        ]

    window = sg.Window('V-TEC II Harnesses', layout)

    event, values = window.Read()

    print(event, values)

    window.Close()

    return (event, values)

#This function gathers the data on what harnesses are being tested from the operator.
#It returns events and values

def CheckBoxWindowFord():
    """This function gathers the data on which harnesses
    are being tested and what fan config"""

    layout = [
		[sg.Text('Select Fan Setup', font = ('Helvetica', 24))],
        [sg.Radio('Single Fan', "FAN", key = '-SingleFan-', default = True), sg.Radio('Dual Fan', "FAN", key = '-DualFan-')],
        [sg.Radio('Fan w/ Aftercooler', "FAN", key = '-FanAftercooler-'), sg.Radio('Dual Fan w/ Dual Aftercooler', "FAN", key = '-DualFanDualAftercooler-')],
        [sg.Text('Select All Harnesses to Be Tested', font = ('Helvetica', 24))],
		[sg.Checkbox('269022 - Dual Pressure ', key = '-269022-')],
		[sg.Checkbox('269024 - Ground', key = '-269024-', default = True)],
		[sg.Checkbox('269025 - Temperature', key = '-269025-', default = True)],
		[sg.Checkbox('269026 - Pressure', key = '-269026-', default = True)],
		[sg.Checkbox('269028 - Generator', key = '-269028-')],
		[sg.Checkbox('269030 / 269300 / 269308 in PTO', key = '-PTO-', default = True)],
		[sg.Checkbox('269030 / 269300 / 269308 in AUX', key = '-AUX-')],
		[sg.Checkbox('269991 - Ford Underhood', key = '-269991-', default = True)],
        [sg.Checkbox('275469 - Display', key = '-275469-', default = True)],
        [sg.Checkbox('277896 - Generator and Aux. Hydro. Splitter', key ='-277896-')],
        [sg.Checkbox('277898 - Hydraulic', key ='-277898-')],
        [sg.Checkbox('278610 - Muncie PTO PWM', key = '-278610-', default = True)],
        
		[sg.OK(pad = (20, 20)), sg.Cancel(pad = (20, 20))]
		]

    window = sg.Window('Ford Harnesses', layout)

    event, values = window.Read()

    print(event, values)

    window.Close()

    return (event, values)

#This function gathers the data on what harnesses are being tested from the operator.
#It returns events and values

def CheckBoxWindowNonFord():

    """This function gathers the data using a GUI on which
    harnesses are being tested and what fan config
    specifically for NonFords"""

    layout = [
        [sg.Text('Select Fan Setup', font = ('Helvetica', 24))],
        [sg.Radio('Single Fan', "FAN", key = '-SingleFan-', default = True), sg.Radio('Dual Fan', "FAN", key = '-DualFan-')],
        [sg.Radio('Fan w/ Aftercooler', "FAN", key = '-FanAftercooler-'), sg.Radio('Dual Fan w/ Dual Aftercooler', "FAN", key = '-DualFanDualAftercooler-')],
		[sg.Text('Select All Harnesses to Be Tested', font = ('Helvetica', 24))],
		[sg.Checkbox('269022 - Dual Pressure ', key = '-269022-')],
		[sg.Checkbox('269024 - Ground', key = '-269024-', default = True)],
		[sg.Checkbox('269025 - Temperature', key = '-269025-', default = True)],
		[sg.Checkbox('269026 - Pressure', key = '-269026-', default = True)],
		[sg.Checkbox('269028 - Generator', key = '-269028-')],
		[sg.Checkbox('269030 / 269300 / 269308 in PTO', key = '-PTO-', default = True)],
		[sg.Checkbox('269030 / 269300 / 269308 in AUX', key = '-AUX-')],
		[sg.Radio('269828 - Underhood', "UH", key = '-269828-'), sg.Radio('269840 - Underhood', "UH", key = '-269840-', default = True), sg.Radio('273434 - Underhood', "UH", key = '-273434-'), sg.Radio('273620 - Underhood', "UH", key = '-273620-')],
        [sg.Radio('274339 - Underhood', "UH", key = '-274339-'), sg.Radio('274340 - Underhood', "UH", key = '-274340-'), sg.Radio('277136 - Underhood', "UH", key = '-277136-')],
        [sg.Radio('275065 - Trunk', "TK", key = '-275065-', default = True), sg.Radio('279827 - Trunk', "TK", key = '-279827-')],
        [sg.Checkbox('275469 - Display', key = '-275469-', default = True)],
        [sg.Radio('276206 - J1939', "J1939", key = '-276206-', default = True), sg.Radio('276757 - J1939', "J1939", key = '-276757-'), sg.Radio('None - J1939', "J1939", key = '-NoneJ1939-')],
        [sg.Checkbox('277319 - Remote Start', key = '-277319-')],
        [sg.Checkbox('277896 - Generator and Aux. Hydro. Splitter', key ='-277896-')],
        [sg.Checkbox('277898 - Hydraulic', key ='-277898-')],
        [sg.Checkbox('278610 - Muncie PTO PWM', key = '-278610-')],
		[sg.OK(pad = (20, 20)), sg.Cancel(pad = (20, 20))]
		]

    window = sg.Window('Non-Ford Harnesses', layout)

    event, values = window.Read()

    print(event, values)

    window.Close()

    return(event, values)

#This function takes the data from the events and values passed by the
#Check box window function and makes a popup window stating
#which program the operator should run. It returns the name
#of the program to be run.

def FordHarnessHash(n):

    """This function takes the data from the events and values
    passed by the checkbox window function and makes a popup window
    stating which program the operator should run.  It returns the
    name of the program to be run.  Ford specific."""

    hash = 'Unsupported combination.  Please retry or contact Engineering.'

    if not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and not n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-SingleFan-'):
        hash = 'Program: Ford_1fan, ID: Ford Standard'
    
    elif not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-SingleFan-'):
        hash = 'Program: Ford_1fan, ID: Ford w/Generator'

    elif n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and not n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-SingleFan-'):
        hash = 'Program: Ford_1fan, ID: Ford w/DualPress'

    elif n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-SingleFan-'):
        hash = 'Program: Ford_1fan, ID: Ford w/GenDP'
    
    elif not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and n.get('-277896-') and not n.get('-277898-') and n.get('-SingleFan-'): 
        hash = 'Program: Ford_1fan, ID: Ford w/GenAuxHdySw'

    elif n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and n.get('-277896-') and n.get('-277898-') and n.get('-SingleFan-'):
        hash = 'Program: Ford_1fan, ID: Ford w/GenDPAuxHydSw'

    elif not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and not n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-DualFan-'):
        hash = 'Program: Ford_2fan, ID: Ford Standard'
    
    elif not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-DualFan-'):
        hash = 'Program: Ford_2fan, ID: Ford w/Generator'

    elif n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and not n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-DualFan-'):
        hash = 'Program: Ford_2fan, ID: Ford w/DualPress'

    elif n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-DualFan-'):
        hash = 'Program: Ford_2fan, ID: Ford w/GenDP'
    
    elif not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and n.get('-277896-') and not n.get('-277898-') and n.get('-DualFan-'): 
        hash = 'Program: Ford_2fan, ID: Ford w/GenAuxHdySw'
    
    elif n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and n.get('-277896-') and n.get('-277898-') and n.get('-DualFan-'):
        hash = 'Program: Ford_2fan, ID: Ford w/GenDPAuxHydSw'


    return hash
        
    

#This function takes the data from the events and values passed by the
#Check box window function and makes a popup window stating
#which program the operator should run. It returns the name
#of the program to be run.

def NonFordHarnessHash(n):

    """This function takes the data from the events and values
    passed by the checkbox window function and makes a popup window
    stating which program the operator should run.  It returns the
    name of the program to be run. NonFord specific."""

    #269022 is DP - Dual Pressure
    #269028 is GEN - Generator
    #277319 is REM - Remote Engage
    #277896 & 277898 are HYD - Hyrdaulic
    #278610 is PWM PTO - Pulse Width Modulation PTO

    hash = 'Unsupported combination.  Please retry or contact Engineering.'

    if n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') \
    and n.get('-PTO-') and n.get('-AUX-') and n.get('-275469-') and n.get('-277136-') and n.get('-277319-') and n.get('-277896-') and n.get('-277898-') and n.get('-278610-'): 

        layoutnep = [
            [sg.Image(r'C:\Program Files (x86)\HarnessSelect\main\img\tumblr_nkfr27M3lv1uofb9ho1_500.png')]
            ]

        window = sg.Window('NEP', layoutnep)

        window.Read()

    if n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-275469-') and n.get('-SingleFan-'):  #Checks to see if the harness is a regular full setup single fan.  They all get these EXTs.        
        
        #Checks if the harness is "Standard".  No extras.		
        if not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):   
            
            if n.get('-269828-'):
                hash = 'Program: NonFord_1fan, ID: Standard UH269828'
                
            elif n.get('-269840-'):
                hash = 'Program: NonFord_1fan, ID: Standard UH269840'
            
            elif n.get('-273620-'):
                hash = 'Program: NonFord_1fan, ID: Standard UH273620'

            elif n.get('-274340-'):
                hash = 'Program: NonFord_1fan, ID: Standard UH274340'



        #Checks if the harness is "NO PTO". Standard - PTO. This is a Dodge Harness Assy.
        elif not n.get('-269022-') and not n.get('-269028-') and not n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):
        
            if n.get('-277136-'):
                hash = 'Program: NonFord_1fan, ID: NO PTO UH277136'
        
        #Checks if the harness is "PWM PTO". Standard + PWM module		
        elif not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):  
            
            if n.get('-269840-'):
                hash = 'Program: NonFord_1fan, ID: PWM PTO UH269840'
            elif n.get('-273620-'):
                hash = 'Program: NonFord_1fan, ID: PWM PTO UH273620'
            elif n.get('-273434-'):
                hash = 'Program: NonFord_1fan, ID: PWM PTO UH273434'
            elif n.get('-274339-'):
                hash = 'Program: NonFord_1fan, ID: PWM PTO UH274339'

        #Checks if the harness is "GEN". Standard + GEN.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):   		

            if n.get('-273434-'):
                hash = 'Program: NonFord_1fan, ID: GEN UH273434'
            elif n.get('-274339-'):
                hash = 'Program: NonFord_1fan, ID: GEN UH274339'
            elif n.get('-274340-'):
                hash = 'Program: NonFord_1fan, ID: GEN UH274340'

         #Checks if the harness is "GEN AUX". Standard + GEN + AUX.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):   		

            if n.get('-269840-'):
                hash = 'Program: NonFord_1fan, ID: GEN AUX UH269840'
        
        #Checks if the harness is "GEN PWM PTO". Standard + GEN + PWM PTO.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):   

            if n.get('-274340-'):
                hash = 'Program: NonFord_1fan, ID: GEN PWM PTO UH274340' 

        #Checks if the harness is "GEN AUX HYD". Standard + GEN + HYDRO + AUX.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and n.get('-AUX-') \
        and not n.get('-277319-') and n.get('-277896-') and n.get('-277898-') and not n.get('-278610-'):
            
            if n.get('-274339-'):
                hash = 'Program: NonFord_1fan, ID: GEN AUX HYD UH274339'


        #Checks if the harness is "GEN REM". Standard + GEN + REM.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):
            
            if n.get('-269840-'):
                hash = 'Program: NonFord_1fan, ID: GEN REM UH269840'

        #Checks if the harness is "DP". Standard + DP.
        elif n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-273434-'):
                hash = 'Program: NonFord_1fan, ID: DP UH273434'
        
        #Checks if the harness is "DP GEN". Standard + DP + GEN.
        elif n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-274340-'):
                hash = 'Program: NonFord_1fan, ID: DP GEN UH274340'

        #Checks if the harness is "DP GEN NO PTO". Standard + DP + GEN - PTO. This is a Dodge Harness Assy.
        elif n.get('-269022-') and n.get('-269028-') and not n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):
        
            if n.get('-277136-'):
                hash = 'Program: NonFord_1fan, ID: DP GEN NO PTO UH277136'

        #Checks if the harness is "DP PWM PTO". Standard + DP + PWM PTO.
        elif n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):

            if n.get('-269840-'):
                hash = 'Program: NonFord_1fan, ID: DP PWM PTO UH269840'
            elif n.get('-274340-'):
                hash = 'Program: NonFord_1fan, ID: DP PWM PTO UH274340'

        #Checks if the harness is "AUX". Standard + AUX.
        elif not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-269840-'):
                hash = 'Program: NonFord_1fan, ID: AUX UH269840'

        #Checks if the harness is "REM".
        elif not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-269840-'):
                hash = 'Program: NonFord_1fan, ID: REM UH269840'

        #Checks if the harness is "REM PWM PTO". Standard + REM + PWM PTO.
        elif not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):

            if n.get('-274340-'):
                hash = 'Program: NonFord_1fan, ID: REM PWM PTO UH274340'

    elif n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-275469-') and n.get('-DualFan-'):  #Checks to see if the harness is a regular full setup dual fan.  They all get these EXTs.        
        
        #Checks if the harness is "Standard".  No extras.		
        if not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):   
            
            if n.get('-269828-'):
                hash = 'Program: NonFord_2fan, ID: Standard UH269828'
                
            elif n.get('-269840-'):
                hash = 'Program: NonFord_2fan, ID: Standard UH269840'

            elif n.get('-273434-'):
                hash = 'Program: NonFord_2fan, ID: Standard UH273434'
            
            elif n.get('-273620-'):
                hash = 'Program: NonFord_2fan, ID: Standard UH273620'

            elif n.get('-274339-'):
                hash = 'Program: NonFord_2fan, ID: Standard UH274339'

            elif n.get('-274340-'):
                hash = 'Program: NonFord_2fan, ID: Standard UH274340'

        #Checks if the harness is "NO PTO". Standard - PTO. This is a Dodge Harness Assy.
        elif not n.get('-269022-') and not n.get('-269028-') and not n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):
        
            if n.get('-277136-'):
                hash = 'Program: NonFord_2fan, ID: NO PTO UH277136'
        
        #Checks if the harness is "PWM PTO". Standard + PWM module		
        elif not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):  
            
            if n.get('-269840-'):
                hash = 'Program: NonFord_2fan, ID: PWM PTO UH269840'
            elif n.get('-273620-'):
                hash = 'Program: NonFord_2fan, ID: PWM PTO UH273620'
            elif n.get('-273434-'):
                hash = 'Program: NonFord_2fan, ID: PWM PTO UH273434'
            elif n.get('-274339-'):
                hash = 'Program: NonFord_2fan, ID: PWM PTO UH274339'

        #Checks if the harness is "GEN". Standard + GEN.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):   		

            if n.get('-273434-'):
                hash = 'Program: NonFord_2fan, ID: GEN UH273434'
            elif n.get('-274339-'):
                hash = 'Program: NonFord_2fan, ID: GEN UH274339'
            elif n.get('-274340-'):
                hash = 'Program: NonFord_2fan, ID: GEN UH274340'
            elif n.get('-269840-'):
                hash = 'Program: NonFord_2fan, ID: GEN UH269840'
        
        #Checks if the harness is "GEN PWM PTO". Standard + GEN + PWM PTO.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):   

            if n.get('-274340-'):
                hash = 'Program: NonFord_2fan, ID: GEN PWM PTO UH274340'

        #Checks if the harness is "GEN AUX HYD". Standard + GEN + HYDRO + AUX.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and n.get('-AUX-') \
        and not n.get('-277319-') and n.get('-277896-') and n.get('-277898-') and not n.get('-278610-'):
            
            if n.get('-274339-'):
                hash = 'Program: NonFord_2fan, ID: GEN AUX HYD UH274339'

         #Checks if the harness is "GEN REM". Standard + GEN + REM.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):
            
            if n.get('-269840-'):
                hash = 'Program: NonFord_2fan, ID: GEN REM UH269840'

        #Checks if the harness is "DP". Standard + DP.
        elif n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-273434-'):
                hash = 'Program: NonFord_2fan, ID: DP UH273434'

            elif n.get('-274340-'):
                hash = 'Program: NonFord_2fan, ID: DP UH274340'
        
        #Checks if the harness is "DP GEN". Standard + DP + GEN.
        elif n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-274340-'):
                hash = 'Program: NonFord_2fan, ID: DP GEN UH274340'

        #Checks if the harness is "DP GEN REM". Standard + DP + GEN + REM.
        elif n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-269840-'):
                hash = 'Program: NonFord_2fan, ID: DP GEN REM UH269840'

        #Checks if the harness is "DP GEN NO PTO". Standard + DP + GEN - PTO. This is a Dodge Harness Assy.
        elif n.get('-269022-') and n.get('-269028-') and not n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):
        
            if n.get('-277136-'):
                hash = 'Program: NonFord_2fan, ID: DP GEN NO PTO UH277136'

        #Checks if the harness is "DP PWM PTO". Standard + DP + PWM PTO.
        elif n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):

            if n.get('-269840-'):
                hash = 'Program: NonFord_2fan, ID: DP PWM PTO UH269840'
            elif n.get('-274340-'):
                hash = 'Program: NonFord_2fan, ID: DP PWM PTO UH274340'

        #Checks if the harness is "AUX". Standard + AUX.
        elif not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-269840-'):
                hash = 'Program: NonFord_2fan, ID: AUX UH269840'

        #Checks if the harness is "REM PWM PTO". Standard + REM + PWM PTO.
        elif not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):

            if n.get('-274340-'):
                hash = 'Program: NonFord_2fan, ID: REM PWM PTO UH274340'



    return hash


def VactorHarnessHash(n):

    """This function takes the data from the events and values
    passed by the checkbox window function and makes a popup window
    stating which program the operator should run.  It returns the
    name of the program to be run. Vactor Specific."""

    #269022 is DP - Dual Pressure
    #269028 is GEN - Generator
    #277319 is REM - Remote Engage
    #277896 & 277898 are HYD - Hyrdaulic
    #278610 is PWM PTO - Pulse Width Modulation PTO

    hash = 'Unsupported combination.  Please retry or contact Engineering.'

    if not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') \
    and not n.get('-269028-') and n.get('-AUX-') and not n.get('-269828-') and not n.get('-269840-') \
    and n.get('-273434-') and not n.get('-273620-') and not n.get('-274339-') and not n.get('-274340-') \
    and not n.get('-277136-') and n.get('-275469-') and not n.get('-277319-') and not n.get('-277896-') \
    and not n.get('-277898-') and not n.get('-278610-') and n.get('-279202-') and n.get('-279372-'): 

        hash = 'Program: Vactor, ID: Standard'

   

    return hash

def VTEC2HarnessHash(n):

    """This function takes the data from the events and values
    passed by the checkbox window function and makes a popup window
    stating which program the operator should run.  It returns the
    name of the program to be run. VTEC2 Specific."""

    hash = 'Unsupported combination.  Please retry or contact Engineering.'

    if n.get('-279174-') and n.get('-PTO1-') and n.get('-279175-'): #Checks to see if it is a normal format NONFord.

        if n.get('-279173-') and n.get('-279275-') and not n.get('-279174R-') and not n.get('-PTO2-') \
        and not n.get('-279274-') and not n.get('-279600-') and not n.get('-280298-'): #GEN DPSI

            hash = 'Program: VTEC2_131_845, ID: GENDPSI'

        elif not n.get('-279173-')  and not n.get('-279174R-') and not n.get('-PTO2-') \
        and not n.get('-279274-') and not n.get('-279275-') and not n.get('-279600-')  and not n.get('-280298-'): #Standard No Frills NONFord

            hash = 'Program: VTEC2_131_845, ID: Standard'

        elif n.get('-279173-')  and not n.get('-279174R-') and not n.get('-PTO2-') \
        and not n.get('-279274-') and not n.get('-279275-') and n.get('-279600-')  and not n.get('-280298-'): #GENNOL NONFord

            hash = 'Program: VTEC2_131_845, ID: GENNOL'

        elif n.get('-279173-')  and not n.get('-279174R-') and n.get('-PTO2-') \
        and n.get('-279274-') and n.get('-279275-') and n.get('-279600-')  and not n.get('-280298-'): #GENERATOR DUAL PSI REMOTE DUAL PTO NO LOAD NONFord

            hash = 'Program: VTEC2_131_845, ID: GENdpsiREMdptoNLOAD'

    return hash

def VTEC2REV2HarnessHash(n):

    """This function takes the data from the events and values
    passed by the checkbox window function and makes a popup window
    stating which program the operator should run.  It returns the
    name of the program to be run. VTEC2 Specific."""

    hash = 'Unsupported combination.  Please retry or contact Engineering.'

    if n.get('-brushedfan-'):

        if n.get('-279175-') and not n.get('-278610-'):

            hash = 'Program: VTEC2_REDU, ID: NonFord'

        elif n.get('-279175-') and n.get('-278610-'):

            hash = 'Program: VTEC2_REDU, ID: NonFord PWMPTO'

        elif n.get('-279943-') and not n.get('-278610-'):

            hash = 'Program: VTEC2_REDU, ID: Ford'

        elif n.get('-279943-') and n.get('-278610-'):

            hash = 'Program: VTEC2_REDU, ID: Ford PWMPTO'

    elif n.get('-brushlessfan-'):

        if n.get('-279175-') and not n.get('-278610-'):

            hash = 'Program: VTEC2_REDU, ID: NonFord Brushless'

        elif n.get('-279175-') and n.get('-278610-'):

            hash = 'Program: VTEC2_REDU, ID: NonFord PWMPTO Brushless'

        elif n.get('-279943-') and not n.get('-278610-'):

            hash = 'Program: VTEC2_REDU, ID: Ford Brushless'

        elif n.get('-279943-') and n.get('-278610-'):

            hash = 'Program: VTEC2_REDU, ID: Ford PWMPTO Brushless'


    return hash

   

def DLorNo(hash):

    """This function creates a GUI that displays
    the program to run and checks to see if the
    user wants to download the main program or not"""

    
    ans = False

    #Layout for Program download window.
    layout = [
        [sg.Text(hash)],
        [sg.OK(), sg.Button(button_text = "Download Main Program", key = '-DOWNLOAD-')]
        ]

    window = sg.Window('Program Download', layout)

    while True: #Downloads the program if download is clicked.  If OK is clicked loops back to main.
        #If X then exit.

        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == '-DOWNLOAD-':
            ans = True
            break
        if event == 'OK':
            break

    window.close()

    #Returns a True/False that triggers nxdown in harness()
    return(ans)

def harness():

    """Creates the initial GUI where either Ford, NonFord or Vactor is selected.
    Moves the program through the rest of the GUIs"""

    keepGoing = True

    while keepGoing is True:



        #This function makes the first radio popup menu and guides through the rest of the menus.
        Fordpop = 0
        NonFordpop = 0
        Vactorpop = 0
        VTEC2pop = 0
        VTEC2REV2pop = 0
        FordHarnesses_event = 0
        NonFordHarnesses_event = 0
        VactorHarnesses_event = 0
        VTEC2Harnesses_event = 0
        VTEC2REV2pop = 0
        localrepo = 'C:\\Users\\nwilczewski\\source\\repos\\TheMightyDotkey\\HarTester_v0.8\\PythonApplication1'

        layout = [
	        [sg.Radio('Ford', "MAKERADIO", key = '-FORD-', default = True, pad = (32, 10)),
	        sg.Radio('Non-Ford', "MAKERADIO", key = '-NONFORD-', pad = (32, 10)), sg.Radio('Vactor', "MAKERADIO", key = '-VACTOR-', pad = (32, 10)),
            sg.Radio('V-TEC2', "MAKERADIO", key = '-VTEC2-', pad = (32, 10), disabled = 0), sg.Radio('V-TEC2 REV02', "MAKERADIO", key = '-VTEC2REV2-', pad = (32, 10), disabled = 0)], 
	        [sg.Submit(pad = (140, 10)), sg.Exit(pad = (170, 10))]
        ]

        window = sg.Window('Harness Selector', layout, size = (750, 100))

        event, values = window.Read()

        window.Close()

        print(values)


        if values['-FORD-'] is True and event not in ('Exit', None):  #Checks if window is canceled or closed
            FordHarnesses_event, FordHarnesses_values = CheckBoxWindowFord() #Returns the Ford Harness Tag

            if FordHarnesses_event not in ('Cancel', None):  
             
                Fordpop = FordHarnessHash(FordHarnesses_values)

                downloadQuestion = DLorNo(Fordpop) #Checks to see if the user wants to download the main program
                
                if downloadQuestion is True:

                    if FordHarnesses_values.get('-SingleFan-'):
                        nxd.Down('Ford1fan')

                    elif FordHarnesses_values.get('-DualFan-'):
                        nxd.Down('Ford2fan')

                    sg.PopupOKCancel(Fordpop, title = 'Ford Program')
            
            
           

        elif values['-NONFORD-'] is True and event not in ('Exit', None):   #Checks if window is canceled or closed
            NonFordHarnesses_event, NonFordHarnesses_values = CheckBoxWindowNonFord() #Returns the Non-Ford Harness Tag
        
            if NonFordHarnesses_event not in ('Cancel', None):  
            
                NonFordpop = NonFordHarnessHash(NonFordHarnesses_values)

                downloadQuestion = DLorNo(NonFordpop) #Checks to see if the user wants to download the main program
                
                if downloadQuestion is True:

                    if NonFordHarnesses_values.get('-SingleFan-') and NonFordHarnesses_values.get('-275065-'):
                        nxd.Down('NonFord1fan065')

                    elif NonFordHarnesses_values.get('-SingleFan-') and NonFordHarnesses_values.get('-279827-'):
                        nxd.Down('NonFord1fan827')

                    elif NonFordHarnesses_values.get('-DualFan-') and NonFordHarnesses_values.get('-275065-'):
                        nxd.Down('NonFord2fan065')

                    elif NonFordHarnesses_values.get('-DualFan-') and NonFordHarnesses_values.get('-279827-'):
                        nxd.Down('NonFord2fan827')

                    sg.PopupOKCancel(NonFordpop, title = 'NonFord Program')
            

        elif values['-VACTOR-'] is True and event not in ('Exit', None):   #Checks if window is canceled or closed
            VactorHarnesses_event, VactorHarnesses_values = CheckBoxWindowVactor() #Returns the Vactor Harness Tag
        
            if VactorHarnesses_event not in ('Cancel', None):  
            
                Vactorpop = VactorHarnessHash(VactorHarnesses_values)

                downloadQuestion = DLorNo(Vactorpop) #Checks to see if the user wants to download the main program
                
                if downloadQuestion is True:
            
                    nxd.Down('Vactor')

                    sg.PopupOKCancel(Vactorpop, title = 'Vactor Program')

        elif values['-VTEC2-'] is True and event not in ('Exit', None):   #Checks if window is canceled or closed
            VTEC2Harnesses_event, VTEC2Harnesses_values = CheckBoxWindowVTEC2() #Returns the Non-Ford Harness Tag
        
            if VTEC2Harnesses_event not in ('Cancel', None):  
            
                VTEC2pop = VTEC2HarnessHash(VTEC2Harnesses_values)

                downloadQuestion = DLorNo(VTEC2pop) #Checks to see if the user wants to download the main program
                
                if downloadQuestion is True:

                    nxd.Down('VTEC2')

                    sg.PopupOKCancel(VTEC2pop, title = 'VTEC2 Program')

        elif values['-VTEC2REV2-'] is True and event not in ('Exit', None):   #Checks if window is canceled or closed
            VTEC2REV2Harnesses_event, VTEC2REV2Harnesses_values = CheckBoxWindowVTEC2REV2() #Returns the Non-Ford Harness Tag
        
            if VTEC2REV2Harnesses_event not in ('Cancel', None):  
            
                VTEC2REV2pop = VTEC2REV2HarnessHash(VTEC2REV2Harnesses_values)

                downloadQuestion = DLorNo(VTEC2REV2pop) #Checks to see if the user wants to download the main program
                
                if downloadQuestion is True:

                    nxd.Down('VTEC2REV2')

                    sg.PopupOKCancel(VTEC2REV2pop, title = 'VTEC2REV2 Program')


        elif event in ('Exit', None):
            keepGoing = False
            

        window.Close()

   





def main():

    #Splash()

    b = threading.Thread(name = 'HarTest', target = harness)   

    b.start()


if __name__ == '__main__':
    main()