from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

class WinButton(Button):
    def render(self):
        return "Windows button clicked"

class WinCheckbox(Checkbox):
    def check(self):
        return "Windows checkbox ticked"

class MacButton(Button):
    def render(self):
        return "Mac button clicked"

class MacCheckbox(Checkbox):
    def check(self):
        return "Mac checkbox rendered"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

if __name__ == "__main__":
    factory = WinFactory()
    button = factory.create_button()
    print(button.render())
