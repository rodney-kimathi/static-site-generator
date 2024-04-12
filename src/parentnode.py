from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no tag")
        
        if not self.children:
            raise ValueError("Invalid HTML: no children")
        
        contents = ""

        for child in self.children:
            contents += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{contents}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
