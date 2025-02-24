import re

from htmlnode import HTMLNode
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter
from extract_links_images import extract_markdown_images, extract_markdown_links
from split_nodes_img_and_link import split_nodes_image, split_nodes_link

# order should be - bold **, italic *, and code `

def text_to_textnodes(text):
    if not isinstance(text, str):
        if HTMLNode.TEXTTOTEXTNODES_DEBUG:
            print(f"Expected a string, got {type(text).__name__} instead.")
        raise TypeError(f"Input isn't a string, can't be processed")
    if HTMLNode.TEXTTOTEXTNODES_DEBUG:
        print(f"Processing {text}...")
    before = TextNode(text, TextType.NORMAL)
    split_bold = split_nodes_delimiter([before], "**", TextType.BOLD)
    split_italic_bold = split_nodes_delimiter(split_bold, "*", TextType.ITALIC)
    split_delim_done = split_nodes_delimiter(split_italic_bold, "`", TextType.CODE)
    if HTMLNode.TEXTTOTEXTNODES_DEBUG:
        print(f"Progress report: after splitting bold, italics and code, current node list is: {repr(split_delim_done)}\n")
    split_images = split_nodes_image(split_delim_done)
    new_nodes_list = split_nodes_link(split_images)
    if HTMLNode.TEXTTOTEXTNODES_DEBUG:
        print(f"Finished. {text} was transformed to\n {repr(new_nodes_list)}")

    return new_nodes_list