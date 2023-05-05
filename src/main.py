import sys

from model.model import Model
from qtgui.view.view import View
from qtgui.controller.controller import Controller

def main():
    m = Model()
    v = View()
    c = Controller()
    
    print("Linking MVC Components")
    m.link(c)
    v.link(c)
    c.link(m, v)

    print("start data load in background threads")
    m.load()
    m.communicate(lambda : print("Model Thread listening"))

    print("start to trigger buffers and lock main thread Qt/View's event loop")
    v.start()
    
    print("Demo Ending")
    m.communicate(lambda : sys.exit())

if __name__ == "__main__":
    main()
