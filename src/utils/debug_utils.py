def debug_node_diff(expected, actual, indent=0):
    """
    Compare two tree-like nodes and print differences in a readable format
    Returns True if nodes are equal, False otherwise
    """
    prefix = " " * indent
    
    # Compare node types
    if expected.__class__ != actual.__class__:
        print(f"{prefix}Type mismatch: {expected.__class__.__name__} != {actual.__class__.__name__}")
        return False
    
    # Compare basic properties
    equal = True
    for attr in ["tag", "value", "props"]:
        if hasattr(expected, attr) and hasattr(actual, attr):
            exp_val = getattr(expected, attr)
            act_val = getattr(actual, attr)
            if exp_val != act_val:
                print(f"{prefix}Attribute '{attr}' mismatch:")
                print(f"{prefix}  Expected: '{exp_val}'")
                print(f"{prefix}  Actual:   '{act_val}'")
                equal = False
    
    # Compare children
    if hasattr(expected, "children") and hasattr(actual, "children"):
        exp_children = getattr(expected, "children", [])
        act_children = getattr(actual, "children", [])
        
        if len(exp_children) != len(act_children):
            print(f"{prefix}Child count mismatch: {len(exp_children)} != {len(act_children)}")
            equal = False
        
        # Compare individual children
        for i in range(min(len(exp_children), len(act_children))):
            print(f"{prefix}Comparing child {i}:")
            child_equal = debug_node_diff(exp_children[i], act_children[i], indent + 2)
            if not child_equal:
                equal = False
    
    if equal:
        print(f"{prefix}Nodes match!")
    
    return equal