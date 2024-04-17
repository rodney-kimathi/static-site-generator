import re
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
    
    @classmethod
    def parse_text_nodes(cls, old_nodes, delimiter, text_type):
        new_nodes = []

        for old_node in old_nodes:
            if type(old_node) != TextNode or old_node.text_type not in TextType.values():
                new_nodes.append(old_node)
                continue

            if old_node.text.count(delimiter) % 2 != 0:
                raise ValueError("Invalid Markdown syntax")
            
            splits = old_node.text.split(delimiter)

            for i in range(len(splits)):
                if i % 2 == 0:
                    splits[i] = TextNode(splits[i], TextType.TEXT.value)
                else:
                    splits[i] = TextNode(splits[i], text_type)

            new_nodes.extend(splits)

        return new_nodes
    
    @classmethod
    def extract_markdown_images(cls, text):
        return re.findall(r"!\[(.+?)\]\((.+?)\)", text)
    
    @classmethod
    def extract_markdown_links(cls, text):
        return re.findall(r"\[(.+?)\]\((.+?)\)", text)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
