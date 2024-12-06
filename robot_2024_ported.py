#Port of 2023 robot.py to use 2024 missions
#Currently untested
from PortMap24 import * #PortMap has all the import

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.
hub.system.set_stop_button(None)

#missionList = ["1","2","3", '4'] #add here for new mission
MIN_MISSION=1
MAX_MISSION=10
missionList=[str(i) for i in range(MIN_MISSION, MAX_MISSION+1)]

def runProgram(mission):
    if mission=='1':
        import mission1_2024_2
    if mission == "2":
        import tree_2024
    elif mission == "3":
        import Tree_part2_2024
    elif mission == "4":
        import joels_code
    elif mission=='5':
        import Test2
    elif mission=='6':
        import Squide2_2024
    #elif mission == '7':
        #import mission2_2024
    #elif mission == '8':
        #import mission3_2024
    #elif mission == '7':
        #import rightmap
    #elif mission == '8':
        #import whaleandkrill

pressed={}

runBytes = hub.system.storage(offset=0,read=1,)
n=int.from_bytes(runBytes, 'big')

try: missionList[n]
except: n=0
while True:
    hub.display.char(missionList[n])

    # Wait for any button.
    pressed = ()
    while not pressed:
        pressed = hub.buttons.pressed()
        wait(10)
    
    # Wait for the button to be released.
    while hub.buttons.pressed():
        wait(10)
    
    if Button.RIGHT in pressed:
        n = (0 if (n==len(missionList)-1) else n+1)
        buttonPressed = True;
    elif Button.LEFT in pressed:
        n = (len(missionList)-1 if (n==0) else n-1)
        buttonPressed = True
    elif Button.CENTER in pressed:
        buttonPressed = True
        break

hub.light.on(Color.GREEN)
wait(50)
hub.system.set_stop_button(Button.CENTER) # Now we want to use the Center button as the stop button again.
runBytes = n.to_bytes(1, 'big')
hub.system.storage(offset=0,write=runBytes)
runProgram(missionList[n])
