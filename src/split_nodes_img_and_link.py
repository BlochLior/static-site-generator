import re

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from extract_links_images import extract_markdown_links, extract_markdown_images


def split_nodes_image(old_nodes):
    new_nodes_list = []
    if not isinstance(old_nodes, list):
        if HTMLNode.SPLITIMGLINK_DEBUG:
            print(f"Expected a list of TextNode objects, got {type(old_nodes).__name__} instead.")
        raise TypeError(f"{type(old_nodes).__name__} is not a valid input, you should enter a list of TextNode objects.")
    for node in old_nodes:
        if not isinstance(node, TextNode):
            if HTMLNode.SPLITIMGLINK_DEBUG:
                print(f"{type(node).__name__} is an invalid input for this function.")
            raise TypeError("list of input contains a non-TextNode object.")
        text = node.text
        if HTMLNode.SPLITIMGLINK_DEBUG:
            print(f"Processing node: {node.text}, Type: {node.text_type}\n")
        if node.text_type != TextType.NORMAL:
            if text.strip():
                if HTMLNode.SPLITIMGLINK_DEBUG:
                    print(f"Skipping split: Node {repr(node.text)} is not NORMAL, and not empty. Appending as-is...\n")
                node.text = text.strip()
                new_nodes_list.append(node)
                if HTMLNode.SPLITIMGLINK_DEBUG:
                    print(f"Appended node. Updated new_nodes_list: {[n.text for n in new_nodes_list]}\n")
                continue
            if HTMLNode.SPLITIMGLINK_DEBUG:
                print(f"Skipped appending empty node. proceeding...\n")
            continue
        curr_pos = 0
        list_of_tuples = extract_markdown_images(text) 
        if list_of_tuples == []:
            if text.strip():
                node.text = text.strip()
                new_nodes_list.append(node)
            continue
        
        for (node_text, node_url) in list_of_tuples:
            text_to_split = text[curr_pos:]
            sections = text_to_split.split(f"![{node_text}]({node_url})", 1)
            if len(sections) < 2:
                if sections[0].strip():
                    if HTMLNode.SPLITIMGLINK_DEBUG:
                        print(f"Split did not find any more parts, adding {sections[0]} as normal TextNode.\n")
                    new_nodes_list.append(TextNode(sections[0].strip(), TextType.NORMAL))
                continue
            node_before = TextNode(sections[0].strip(), TextType.NORMAL)
            image_node = TextNode(node_text, TextType.IMAGES, node_url)
            if sections[0].strip():
                if HTMLNode.SPLITIMGLINK_DEBUG:
                    print(f"Found textnode before the new image. Created {repr(node_before)}\n")
                new_nodes_list.append(node_before)
            if HTMLNode.SPLITIMGLINK_DEBUG:
                print(f"Found match, created {repr(image_node)}\n")
            new_nodes_list.append(image_node)
            to_add = len(sections[0]) + len(f"![{node_text}]({node_url})")
            curr_pos += to_add
        if curr_pos < len(text):
            if text[curr_pos:].strip():
                if HTMLNode.SPLITIMGLINK_DEBUG:
                    print(f"No further matches found in the text. Appending '{text[curr_pos:].strip()}' as a normal text textnode.\n")
                new_nodes_list.append(TextNode(text[curr_pos:].strip(), TextType.NORMAL))
    if HTMLNode.SPLITIMGLINK_DEBUG:
        print(f"Finished splitting nodes. The old nodes {old_nodes} were converted to \n {new_nodes_list}")
    return new_nodes_list

def split_nodes_link(old_nodes):
    new_nodes_list = []
    if not isinstance(old_nodes, list):
        if HTMLNode.SPLITIMGLINK_DEBUG:
            print(f"Expected a list of TextNode objects, got {type(old_nodes).__name__} instead.")
        raise TypeError(f"{type(old_nodes).__name__} is not a valid input, you should enter a list of TextNode objects.")
    for node in old_nodes:
        if not isinstance(node, TextNode):
            if HTMLNode.SPLITIMGLINK_DEBUG:
                print(f"{type(node).__name__} is an invalid input for this function.")
            raise TypeError("list of input contains a non-TextNode object.")
        text = node.text
        if HTMLNode.SPLITIMGLINK_DEBUG:
            print(f"Processing node: {node.text}, Type: {node.text_type}\n")
        if node.text_type != TextType.NORMAL:
            if text.strip():
                if HTMLNode.SPLITIMGLINK_DEBUG:
                    print(f"Skipping split: Node {repr(node.text)} is not NORMAL. Appending as-is...\n")
                node.text = text.strip()
                new_nodes_list.append(node)
                if HTMLNode.SPLITIMGLINK_DEBUG:
                    print(f"Appended node. Updated new_nodes_list: {[n.text for n in new_nodes_list]}\n")
                continue
            if HTMLNode.SPLITIMGLINK_DEBUG:
                print(f"Skipped appending empty node. proceeding...\n")
            continue
        curr_pos = 0
        list_of_tuples = extract_markdown_links(text) 
        if list_of_tuples == []:
            if text.strip():
                node.text = text.strip()
                new_nodes_list.append(node)
            continue
        
        for (node_text, node_url) in list_of_tuples:
            text_to_split = text[curr_pos:]
            sections = text_to_split.split(f"[{node_text}]({node_url})", 1)
            if len(sections) < 2:
                new_text = sections[0].strip()
                if new_text:
                    if HTMLNode.SPLITIMGLINK_DEBUG:
                        print(f"Split did not find any more parts, adding {new_text} as normal TextNode.\n")
                    
                    new_nodes_list.append(TextNode(new_text, TextType.NORMAL))
                continue
            new_text = sections[0].strip()
            node_before = TextNode(new_text, TextType.NORMAL)
            link_node = TextNode(node_text, TextType.LINKS, node_url)
            if new_text:
                if HTMLNode.SPLITIMGLINK_DEBUG:
                    print(f"Found textnode before the new link. Created {repr(node_before)}\n")
                new_nodes_list.append(node_before)
            if HTMLNode.SPLITIMGLINK_DEBUG:
                print(f"Found match, created {repr(link_node)}\n")
            new_nodes_list.append(link_node)
            to_add = len(sections[0]) + len(f"[{node_text}]({node_url})")
            curr_pos += to_add
        if curr_pos < len(text):
            last_text = text[curr_pos:].strip()
            if last_text:
                if HTMLNode.SPLITIMGLINK_DEBUG:
                    print(f"No further matches found in the text. Appending '{last_text}' as a normal text textnode.\n")
                new_nodes_list.append(TextNode(last_text, TextType.NORMAL))
    if HTMLNode.SPLITIMGLINK_DEBUG:
        print(f"Finished splitting nodes. The old nodes {old_nodes} were converted to \n {new_nodes_list}")
    return new_nodes_list