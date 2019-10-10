
import PySimpleGUI as sg

def CheckBoxWindowFord():

	layout = [
		[sg.Checkbox('1'),
		sg.Checkbox('2'),
		sg.Checkbox('3'),
		sg.Checkbox('4'),
		sg.Checkbox('5'),
		sg.Checkbox('6'),
		sg.Checkbox('7'),
		sg.Checkbox('8')]
		[sg.OK, sg.Cancel]
		]
	
	window = sg.window('Ford Harnesses', layout)

	event, values = window.Read()
	window.Close()
		


