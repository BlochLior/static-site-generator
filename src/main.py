from enum import Enum
from textnode import TextType, TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    new_textnode = TextNode("hello world", "bold", "www.com")
    print(new_textnode)

main()