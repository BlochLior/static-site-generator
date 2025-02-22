import re
from htmlnode import HTMLNode

def extract_markdown_images(text):
    list_of_tuples = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if HTMLNode.EXTRACT_DEBUG:
        print(f"In {text}, we found {list_of_tuples}\n")
    if not list_of_tuples:
        if HTMLNode.EXTRACT_DEBUG:
            print(f"No images found in {text}")
        return []    
        
    return list_of_tuples

def extract_markdown_links(text):
    list_of_tuples = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    if HTMLNode.EXTRACT_DEBUG:
        print(f"In '{text}', we found {list_of_tuples}\n")
    
    if not list_of_tuples:
        if HTMLNode.EXTRACT_DEBUG:
            print(f"No images found in {text}")
        return []    
    return list_of_tuples