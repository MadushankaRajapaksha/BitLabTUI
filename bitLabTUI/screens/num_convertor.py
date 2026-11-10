from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static


class NumConvertor(Screen):
    """
    number conveting screen


    """
    
    def compose(self) -> ComposeResult:
        yield Static("this is a number convertor screen")
        
