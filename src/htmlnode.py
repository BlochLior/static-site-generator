class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # tag is a string representing the html tag name
        self.tag = tag
        # value is a string representing the value of the 
        # html tag (e.g. the text inside a paragraph)
        self.value = value
        # children is a list of HTMLNode objects representing
        # the children of this node
        self.children = children
        # props is a dictionary of key-value pairs 
        # representing the attributes of the HTML tag
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return self.props
        else:
            props_copy = self.props.copy()
            props_as_tup_lst = props_copy.items()
            props_lst = []
            for (key, value) in props_as_tup_lst:
                item = f'{key}="{value}"'
                props_lst.append(item)
            return " ".join(props_lst)
    
    def get_attr(self, attr_name):
        value = getattr(self, attr_name, None)
        return f"{attr_name}={value if value is not None else 'None'}"

    def __repr__(self):
        attrs = ", ".join(self.get_attr(attr) for attr in ["tag", "value", "children", "props"])
        return f"HTMLNode({attrs})"    

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        
        for attr in ["tag", "value", "children", "props"]:
            if getattr(self, attr) != getattr(other, attr):
                return False           
        return True
    
