try:
    from .define import *
except:
    from define import *

class App():
    def __init__(self, ROOT) -> None:
        ROOT.geometry('750x400')
        ROOT.title('Main Menu')
        ROOT['background'] = COLOUR_BACKGROUND
        ROOT.resizable(False, False)

