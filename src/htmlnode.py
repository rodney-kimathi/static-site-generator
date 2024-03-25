class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("To be overridden by child classes")
    
    def props_to_html(self):
        attrs = ""

        if not self.props:
            return attrs
        
        for key, value in self.props.items():
            attrs += f" {key}=\"{value}\""

        return attrs
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
