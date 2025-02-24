import re
import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter
from extract_links_images import extract_markdown_images, extract_markdown_links
from split_nodes_img_and_link import split_nodes_image, split_nodes_link
from text_to_textnodes import text_to_textnodes

class TestTexttoTextNodes(unittest.TestCase):
    def test_text_to_textnodes_adjacent_spec_characters(self):
        text = "**bold**`code`*italic* all together"
        trans = text_to_textnodes(text)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode("code", TextType.CODE),
            TextNode("italic", TextType.ITALIC),
            TextNode("all together", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)
    
    def test_text_to_textnodes_simp_bold(self):
        text = "simple **bold** text"
        trans = text_to_textnodes(text)
        expected = [
            TextNode("simple", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode("text", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)

    def test_text_to_textnodes_link_image(self):
        text = "A [link](https://boot.dev) and an ![image](pic.jpg)"
        trans = text_to_textnodes(text)
        expected = [
            TextNode("A", TextType.NORMAL),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
            TextNode("and an", TextType.NORMAL),
            TextNode("image", TextType.IMAGES, "pic.jpg")
        ]
        self.assertEqual(trans, expected)
    
    def test_text_to_textnodes_mixed_all(self):
        text = "Mixed **bold** and *italic* and `code` with [link](url)"
        trans = text_to_textnodes(text)
        expected = [
            TextNode("Mixed", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode("and", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode("and", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode("with", TextType.NORMAL),
            TextNode("link", TextType.LINKS, "url")            
        ]
        self.assertEqual(trans, expected)
    
    def test_long_repeating_pattern(self):
        elements = [
            "**bold text**",
            "*italic text*",
            "`code block`",
            "[link](https://example.com)",
            "![image](https://image.com/pic.jpg)",
            "plain text "
        ]
        
        test_text = ""
        for i in range(20): 
            test_text += elements[i % len(elements)]
            test_text += " "
        trans = text_to_textnodes(test_text)
        bold = TextNode("bold text", TextType.BOLD)
        italic = TextNode("italic text", TextType.ITALIC)
        code = TextNode("code block", TextType.CODE)
        link = TextNode("link", TextType.LINKS, "https://example.com")
        image = TextNode("image", TextType.IMAGES, "https://image.com/pic.jpg")
        normal = TextNode("plain text", TextType.NORMAL)
        expected = [
            bold, italic, code, link, image, normal,
            bold, italic, code, link, image, normal, 
            bold, italic, code, link, image, normal, 
            bold, italic
        ]
        self.assertEqual(trans, expected)


if __name__ == "__main__":
    unittest.main()