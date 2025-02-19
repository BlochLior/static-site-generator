from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "link"
    IMAGES = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        
        for attr in ["text", "text_type", "url"]:
            if getattr(self, attr) != getattr(other, attr):
                return False           
        return True
    
    def get_attr(self, attr_name):
        value = getattr(self, attr_name, None)
        return f"{attr_name}={value if value is not None else 'None'}"   

    def __repr__(self):
        attrs = ", ".join(self.get_attr(attr) for attr in ["text", "text_type", "url"])
        return f"TextNode({attrs})"
          