from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Button, Static


class TopBar(Widget):
    DEFAULT_CSS = """
        TopBar{
            dock:top;
            height: 1;
            background: $surface;
            padding: 0 1;
        }
        Horizontal { height: 100%; }
        #spacer1 ,#spacer2{
            width:1fr;
            
        } 
        TopBar Horizontal { height: 100%; }
        TopBar Static   { width: auto; }
        TopBar .spacer  { width: 1fr; }
        TopBar .back    { color: $primary; }
        TopBar .menu    { color: $primary; }
    """

    def __init__(self, screen, isback=True):
        super().__init__()
        self.enbledBack = isback
        self.screenName = screen

    def compose(self):
        with Horizontal():
            if self.enbledBack:
                yield Static("←", classes="back")   
            yield Static("", classes="spacer")
            yield Static(f"{self.screenName} - BitLabTUI", classes="title")
            yield Static("", classes="spacer")
            yield Static("☰", classes="menu")
