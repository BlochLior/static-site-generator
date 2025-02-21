from enum import Enum
from htmlnode import HTMLNode
from leafnode import LeafNode

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

    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.NORMAL:
            normal_leafnode = LeafNode(tag=None, value=text_node.text)
            return normal_leafnode
        elif text_node.text_type == TextType.BOLD:
            bold_leafnode = LeafNode(tag="b", value=text_node.text)
            return bold_leafnode
        elif text_node.text_type == TextType.ITALIC:
            italicized_leafnode = LeafNode(tag="i", value=text_node.text)
            return italicized_leafnode
        elif text_node.text_type == TextType.CODE:
            code_leafnode = LeafNode(tag="code", value=text_node.text)
            return code_leafnode
        elif text_node.text_type == TextType.LINKS:
            link_leafnode = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
            return link_leafnode
        elif text_node.text_type == TextType.IMAGES:
            image_leafnode = LeafNode(tag="img", value="", props={
                "src": text_node.url,
                "alt": text_node.text
            })
            return image_leafnode
        else:
            raise Exception("TextNode does not correspond to an available TextType value")

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
          