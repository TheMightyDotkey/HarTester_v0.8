#A python app to choose a wiring harness.
import HarnessHashBuilder as hhb
import CheckBoxWindow as cbw
import PySimpleGUI as sg
import main
import NXDown as nxd

def harness():

    #This function makes the first radio popup menu and guides through the rest of the menus.
    Fordpop = 0
    NonFordpop = 0
    FordHarnesses_event = 0
    NonFordHarnesses_event = 0

    layout = [
	    [sg.Radio('Ford', "MAKERADIO", key = '-FORD-', default = True, pad = (32, 10)),
	    sg.Radio('Non-Ford', "MAKERADIO", key = '-NONFORD-', pad = (32, 10))],
	    [sg.Submit(pad = (42, 10)), sg.Exit(pad = (42, 10))]
    ]

    window = sg.Window('Harness Selector', layout, size = (300, 100))

    event, values = window.Read()

    window.Close()

    print(values)

    if values['-FORD-'] is True and event not in ('Exit', None):  #Checks if window is canceled or closed
        FordHarnesses_event, FordHarnesses_values = cbw.CheckBoxWindowFord()

        if FordHarnesses_event not in ('Cancel', None):  #Returns the Ford Harness Tag
             
            if FordHarnesses_values.get('-SingleFan-'):
                nxd.Down('Ford1fan')

            elif FordHarnesses_values.get('-DualFan-'):
                nxd.Down('Ford2fan')
            
            Fordpop = hhb.FordHarnessHash(FordHarnesses_values)
            
           

    elif values['-NONFORD-'] is True and event not in ('Exit', None):   #Checks if window is canceled or closed
        NonFordHarnesses_event, NonFordHarnesses_values = cbw.CheckBoxWindowNonFord()
        
        if NonFordHarnesses_event not in ('Cancel', None):  #Returns the Non-Ford Harness Tag
            hhb.NonFordHarnessHash(NonFordHarnesses_values)

            if NonFordHarnesses_values.get('-SingleFan-'):
                nxd.Down('NonFord1fan')

            elif NonFordHarnesses_values.get('-DualFan-'):
                nxd.Down('NonFord2fan')

    window.Close()
    
   

