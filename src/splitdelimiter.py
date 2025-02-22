from textnode import TextNode, TextType
from htmlnode import HTMLNode

# bear - i think i already have 6.
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes_list = []
    for node in old_nodes:
        if HTMLNode.SPLITDELIMITER_DEBUG:
            print(f"Processing node: {node.text}, Type: {node.text_type}\n")

        if node.text_type != TextType.NORMAL:
            if HTMLNode.SPLITDELIMITER_DEBUG:
                print(f"Skipping split: Node {repr(node.text)} is not NORMAL. Appending as-is...")

            new_nodes_list.append(node)
            if HTMLNode.SPLITDELIMITER_DEBUG:
                print(f"Appended node. Updated new_nodes_list: {[n.text for n in new_nodes_list]}\n")
            continue
        text = node.text
        curr_pos = 0
        while curr_pos < len(text):
            opening_index = text.find(delimiter, curr_pos)
            if HTMLNode.SPLITDELIMITER_DEBUG:
                print(f"Current position: {curr_pos}, Opening index: {opening_index}, Current text segment: {text[curr_pos:]}\n")

            if opening_index == -1:
                remaining_text = text[curr_pos:]
                if remaining_text:
                    if HTMLNode.SPLITDELIMITER_DEBUG:
                        print(f"No more delimitors found in the node, therefore adding NORMAL node with the text: '{remaining_text}'\n")

                    new_nodes_list.append(TextNode(remaining_text, TextType.NORMAL))
                break
            
            closing_index = text.find(delimiter, opening_index + len(delimiter))
            if closing_index == -1:
                if HTMLNode.SPLITDELIMITER_DEBUG:
                    print(f"No closing delimiter found for: {text[opening_index:]}. Raising exception\n")

                raise Exception("invalid markdown syntax, no closing delimiter")
            
            text_between = text[opening_index + len(delimiter):closing_index]
            if text_between.strip() == "":
                curr_pos = opening_index + len(delimiter)
                if HTMLNode.SPLITDELIMITER_DEBUG:
                    print(f"Empty content between delimiters at {opening_index}, advancing cursor to {curr_pos} without appending. Remaining text: '{text[curr_pos:]}'\n")

                continue
            if text[curr_pos:opening_index].strip():
                node1 = TextNode(text[curr_pos:opening_index], TextType.NORMAL)
                if HTMLNode.SPLITDELIMITER_DEBUG:
                    print(f"Adding NORMAL node with text: '{node1.text}' before delimiter.\n")
                new_nodes_list.append(node1)
            node2 = TextNode(text_between, text_type)
            if HTMLNode.SPLITDELIMITER_DEBUG:
                print(f"Adding FORMATTED node with the text {text_between}, Type: {text_type}.\n")
            new_nodes_list.append(node2)
            curr_pos = closing_index + len(delimiter)
            if HTMLNode.SPLITDELIMITER_DEBUG:
                print(f"Cursor moved to position {curr_pos} after processing formatted text '{text_between}'. Remaining text: '{text[curr_pos:]}'\n")
        
        if HTMLNode.SPLITDELIMITER_DEBUG:
            print(f"Completed processing current node: '{node.text}' current new_nodes_list: {[{'text': n.text, 'type': n.text_type} for n in new_nodes_list]}\n")

    if HTMLNode.SPLITDELIMITER_DEBUG:
        print(f"Final new_nodes_list text to be returned: {[{'text': n.text, 'type': n.text_type} for n in new_nodes_list]}\n")

    return new_nodes_list