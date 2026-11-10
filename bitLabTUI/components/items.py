from textual.app import    ComposeResult

from textual.message import Message
from textual.widget import Widget
from textual.widgets import Static, Label


class Box(Widget):
    DEFAULT_CSS = """
    Box {
        height: auto;
        border: round $primary;
        padding: 1;
        margin-bottom: 1;
    }
    Box:hover { border: round $accent; }
    Box .title { text-style: bold underline; }
    Box .desc  { color: $text-muted; }
    """

    class Opened(Message):
        def __init__(self,box:"Box"):
            self.box = box
            super().__init__()

    def __init__(self,title,description,screen, **kwargs):
        super().__init__(**kwargs)
        self.itemName = title
        self.itemDescription = description
        self.itemNav = screen

    def compose(self) -> ComposeResult:
        """
        TUI Items 
        """

        yield Static(f"{self.itemName}", id="title")
        yield Static(self.itemDescription,id="desc")

    def on_click(self) -> None:
        self.post_message(self.Opened(self))
