class Button(object):
    html = ""

    def get_html(self):
        return self.html

    def __init__(self):
        print("Button constructor")


class Image(Button):
    html = "<img></img>"

    def __init__(self):
        print("Image constructor")


class Input(Button):
    html = "<input></input>"

    def __init__(self):
        print("Input constructor")


class Flash(Button):
    html = "<obj></obj>"

    def __init__(self):
        print("Flash constructor")


class ButtonFactory:
    def create_button(self, typ):
        targetClass = typ.capitalize()
        return globals()[targetClass]()


buttonObj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
    buttonFact = buttonObj.create_button(b)
    #print(buttonFact.get_html())
    #print(buttonObj.create_button(b).get_html())
