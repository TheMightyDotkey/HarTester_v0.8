import PySimpleGUI as sg
import HarnessSelector as hs

def FordHarnessHash(n):

    hash = 'Unsupported combination.  Please retry or contact Engineering.'

    if not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and not n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-SingleFan-'):
        hash = 'Program: Ford_1fan, ID: Ford Standard'
    
    elif not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-SingleFan-'):
        hash = 'Program: Ford_1fan, ID: Ford w/Generator'

    elif n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and not n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-SingleFan-'):
        hash = 'Program: Ford_1fan, ID: Ford w/DualPress'
    
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
    
    elif not n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and n.get('-277896-') and not n.get('-277898-') and n.get('-DualFan-'): 
        hash = 'Program: Ford_2fan, ID: Ford w/GenAuxHdySw'
    
    elif n.get('-269022-') and n.get('-269024-') and n.get('-269025-') and n.get('-269026-') and n.get('-269028-') and n.get('-PTO-') and n.get('-269991-') and n.get('-275469-') and n.get('-278610-') and n.get('-277896-') and n.get('-277898-') and n.get('-DualFan-'):
        hash = 'Program: Ford_2fan, ID: Ford w/GenDPAuxHydSw'

    Fordpop = sg.PopupOKCancel(hash, title = 'Ford Program') 
        
    if Fordpop is 'OK':

        hs.harness()




def NonFordHarnessHash(n):

    #269022 is DP - Dual Pressure
    #269028 is GEN - Generator
    #277319 is REM - Remote Engage
    #277896 & 277898 are HYD - Hyrdaulic
    #278610 is PWM PTO - Pulse Width Modulation PTO

    hash = 'Unsupported combination.  Please retry or contact Engineering.'

    if n.get('-269022-') and n.get('269024') and n.get('269025') and n.get('269026') and n.get('269028') \
    and n.get('PTO') and n.get('AUX') and n.get('275469') and n.get('276206') and n.get('277136') and n.get('277319') and n.get('277896') and n.get('277898') and n.get('278610'): 

        layoutnep = [
            [sg.Image(r'C:\Users\nwilczewski\source\repos\HarTester_v0.8\PythonApplication1\tumblr_nkfr27M3lv1uofb9ho1_500.png')]
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
        
        #Checks if the harness is "PWM PTO". Standard + PWM module		
        elif not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):  
            
            if n.get('-269840-'):
                hash = 'Program: NonFord_1fan, ID: PWM PTO UH269840'
            elif n.get('-273620-'):
                hash = 'Program: NonFord_1fan, ID: PWM PTO UH273620'

        #Checks if the harness is "GEN". Standard + GEN.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):   		

            if n.get('-273434-'):
                hash = 'Program: NonFord_1fan, ID: GEN UH273434'
            elif n.get('-274339-'):
                hash = 'Program: NonFord_1fan, ID: GEN UH274339'
        
        #Checks if the harness is "GEN PWM PTO". Standard + GEN + PWM PTO.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):   

            if n.get('-274340-'):
                hash = 'Program: NonFord_1fan, ID: GEN UH273434'

        #Checks if the harness is "GEN AUX HYD". Standard + GEN + HYDRO + AUX.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and n.get('-AUX-') \
        and not n.get('-277319-') and n.get('-277896-') and n.get('-277898-') and not n.get('-278610-'):
            
            if n.get('-274339-'):
                hash = 'Program: NonFord_1fan, ID: GEN AUX HYD UH274339'

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
            
            elif n.get('-273620-'):
                hash = 'Program: NonFord_2fan, ID: Standard UH273620'
        
        #Checks if the harness is "PWM PTO". Standard + PWM module		
        elif not n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):  
            
            if n.get('-269840-'):
                hash = 'Program: NonFord_2fan, ID: PWM PTO UH269840'
            elif n.get('-273620-'):
                hash = 'Program: NonFord_2fan, ID: PWM PTO UH273620'

        #Checks if the harness is "GEN". Standard + GEN.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):   		

            if n.get('-273434-'):
                hash = 'Program: NonFord_2fan, ID: GEN UH273434'
            elif n.get('-274339-'):
                hash = 'Program: NonFord_2fan, ID: GEN UH274339'
        
        #Checks if the harness is "GEN PWM PTO". Standard + GEN + PWM PTO.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and n.get('-278610-'):   

            if n.get('-274340-'):
                hash = 'Program: NonFord_2fan, ID: GEN UH273434'

        #Checks if the harness is "GEN AUX HYD". Standard + GEN + HYDRO + AUX.
        elif not n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and n.get('-AUX-') \
        and not n.get('-277319-') and n.get('-277896-') and n.get('-277898-') and not n.get('-278610-'):
            
            if n.get('-274339-'):
                hash = 'Program: NonFord_2fan, ID: GEN AUX HYD UH274339'

        #Checks if the harness is "DP". Standard + DP.
        elif n.get('-269022-') and not n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-273434-'):
                hash = 'Program: NonFord_2fan, ID: DP UH273434'
        
        #Checks if the harness is "DP GEN". Standard + DP + GEN.
        elif n.get('-269022-') and n.get('-269028-') and n.get('-PTO-') and not n.get('-AUX-') \
        and not n.get('-277319-') and not n.get('-277896-') and not n.get('-277898-') and not n.get('-278610-'):

            if n.get('-274340-'):
                hash = 'Program: NonFord_2fan, ID: DP GEN UH274340'

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


    NonFordpop = sg.PopupOKCancel(hash, title = 'NonFord Program')

    if NonFordpop is 'OK':

        hs.harness()


    return hash
