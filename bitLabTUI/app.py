from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Placeholder
from textual.containers import HorizontalScroll, VerticalScroll
from .screens.num_convertor import NumConvertor
from .components.topbar import TopBar
from .components.items import Box


class BitLabApp(App):
    """A Bitlab App"""

    DEFAULT_CSS = """
    VerticalScroll{
        padding:1 4;
    }
     
    
    
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.screens = [
            {
                "name": "Number Convertor",
                "description": "convert number to another number , hex,decimal,binary",
                "screen": NumConvertor,
            }
        ]

    def compose(self) -> ComposeResult:
        yield TopBar("home")

        with VerticalScroll():
            for screen in self.screens:
                yield Box(screen["name"], screen["description"], screen["screen"])
        yield Footer()
        
    def on_box_opened(self,event:Box.Opened):
        self.push_screen(event.box.itemNav())

app = BitLabApp()
