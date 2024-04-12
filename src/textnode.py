from leafnode import LeafNode
from text_type import TextType

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            type(other) == TextNode
            and self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def to_html_node(self):
        if self.text_type not in TextType.values():
            raise ValueError(f"Invalid text type: {self.text_type}")
        
        leaf_node = LeafNode(None, self.text)
        
        if self.text_type == TextType.IMAGE.value:
            leaf_node.value = ""
            leaf_node.tag = "img"
            leaf_node.props = {"src": self.url, "alt": self.text}

        if self.text_type == TextType.LINK.value:
            leaf_node.tag = "a"
            leaf_node.props = {"href": self.url}
        
        if self.text_type == TextType.CODE.value: leaf_node.tag = "code"
        if self.text_type == TextType.ITALIC.value: leaf_node.tag = "i"
        if self.text_type == TextType.BOLD.value: leaf_node.tag = "b"

        return leaf_node
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
