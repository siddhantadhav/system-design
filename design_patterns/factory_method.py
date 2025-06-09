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
        return "This is a windows button"

class MacButton(Button):
    def render(self):
        return "This is a mac button"

class WinCheckbox(Checkbox):
    def check(self):
        return "This is a windows checkbox"

class MacCheckbox(Checkbox):
    def check(self):
        return "This is a mac checkox"

class ButtonFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

class CheckboxFactory(ABC):
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

class WinButtonFactory(ButtonFactory):
    def create_button(self):
        return WinButton()

class WinCheckboxFactory(CheckboxFactory):
    def create_checkbox(self):
        return WinCheckbox()
    
class MacButtonFactory(ButtonFactory):
    def create_button(self):
        return MacButton()

class MacCheckboxFactory(CheckboxFactory):
    def create_checkbox(self):
        return MacCheckbox()

if __name__ == "__main__":
    windows_button = WinButtonFactory()
    button = windows_button.create_button()
    button.render()