from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        if not self.children:
            raise ValueError("parent must have children!")

    def to_html(self):
        if not self.tag:
            raise ValueError("parent must have a tag!")
        final = []
        for child in self.children:
            final.append(child.to_html())
        if not self.props:
            return f'<{self.tag}>{"".join(final)}</{self.tag}>'
        return f'<{self.tag} {self.props_to_html()}>{"".join(final)}</{self.tag}>'
 