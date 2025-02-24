class HTMLNode:
    DEBUG = False # >>>>>>>>>>>>>>>raise this banner True only when intensive debugging are afoot
    SPLITDELIMITER_DEBUG = False #>directed at split_nodes_delimiter func
    EXTRACT_DEBUG = False #>>>>>>>>directed at extract_links and extract_images from markdown functions
    SPLITIMGLINK_DEBUG = True #>>>>directed at split_nodes_image and split_nodes_link functions

    def __init__(self, tag=None, value=None, children=None, props=None):
        if HTMLNode.DEBUG:
            print(f"DEBUG: tag={tag}, value={value}, children={children}, props={props}\n")
        
        if props is not None and not isinstance(props, dict):
            raise ValueError("Props must be a dictionary")
        
        self.tag = tag
        self.value = value
        self.children = children or []  # Default to an empty list if None
        self.props = props if props else {} 
        for child in self.children:
            if child is not None and not isinstance(child, HTMLNode):
                raise ValueError("All children must be instances of HTMLNode or None!")

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        # Exclude None values
        props_lst = [f'{key}="{value}"' for key, value in self.props.items() if value is not None]
        return " ".join(props_lst)
    
    def get_attr(self, attr_name):
        value = getattr(self, attr_name, None)
        if attr_name == "children":
            # Show nothing if no children exist
            return None if not value else f"{attr_name}={len(value)} children"
        elif attr_name == "props":
            # Properly format props if it contains multiple key-value pairs
            return f"{attr_name}={{{', '.join(f'{k}={repr(v)}' for k, v in value.items())}}}" if value else None
        return f"{attr_name}={value if value is not None else 'None'}"

    def __repr__(self):
        attrs = ", ".join(attr for attr in (self.get_attr(attr) for attr in ["tag", "value", "children", "props"]) if attr)
        return f"{self.__class__.__name__}({attrs})" 

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        # Compare attributes directly, trusting they are valid
        for attr in ["tag", "value", "children", "props"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True
    
