
import PySimpleGUI as sg

def CheckBoxWindowFord():
    #This function gathers the data on which harnesses are being tested and what fan config

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
		
def CheckBoxWindowNonFord():

    #This function gathers the data on which harnesses are being tested and what fan config

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
