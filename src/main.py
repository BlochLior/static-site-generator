from enum import Enum
from textnode import TextType
from textnode import TextNode

def main():
    new_textnode = TextNode("hello world", "bold", "www.com")
    print(new_textnode)

main()