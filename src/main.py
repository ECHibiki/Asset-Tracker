import sys

from model.model import Model
from qtgui.view.view import WindowManager
from qtgui.controller.controller import Controller

def main():
    m = Model()
    v = WindowManager()
    c = Controller()
    
    print("Linking MVC Components")
    m.link(c)
    v.link(c)
    c.link(v , m)


    print("start to trigger")
    v.start()
    print("Demo Ending")
    sys.exit()

if __name__ == "__main__":
    main()
