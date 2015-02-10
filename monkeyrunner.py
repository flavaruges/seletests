from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

def main():
    # Connects to the current device, returning a MonkeyDevice object
    device = MonkeyRunner.waitForConnection()
    print "waiting for connection...\n"

    package = 'coms6998.cs.columbia.edu'

    activity = 'coms6998.cs.columbia.edu.VoiceRegonitionDemoActivity'

    # sets the name of the component to start
    runComponent = package + '/' + activity

    # Runs the component
    device.startActivity(component=runComponent)

    # Presses the speaker button
    device.press("DPAD_DOWN", MonkeyDevice.DOWN_AND_UP)
    device.press("DPAD_CENTER", MonkeyDevice.DOWN_AND_UP)
    device.touch()
    
    
    # Takes a screenshot
    screenshot = device.takeSnapshot()
    reference = MonkeyRunner.loadImageFromFile('./device.png')

    MonkeyRunner.sleep(4)
    
    screenshot2 = device.takeSnapshot()
    screenshot.writeToFile('./device2.png','png')

    # Writes the screenshot to a file
    screenshot.writeToFile('./device1.png','png')
    if not screenshot.sameAs(reference, 0.9):
        print "comparison failed!\n"

if __name__ == '__main__':
     main()