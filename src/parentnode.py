from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required")
        
        if self.children is None:
            raise ValueError("Children are required")
        
        opening_tag = f"<{self.tag}{super().props_to_html()}>"
        closing_tag = f"</{self.tag}>"
        content = ""

        if len(self.children) == 0:
            return opening_tag + closing_tag

        for child in self.children:
            if isinstance(child, LeafNode):
                content += child.to_html()
            else:
                if content:
                    content += child.to_html()
                else:
                    content = child.to_html()
        
        return opening_tag + content + closing_tag
    
    def __repr__(self):
        return f"ParentNode({self.children}, {self.tag}, {self.props})"
