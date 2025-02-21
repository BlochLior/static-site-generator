import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_text_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsInstance(repr(node), str)

    def test_textnode_repr_value_w_url(self):
        node = TextNode("this is code", TextType.CODE, "www.code.com")
        expected = 'TextNode(text=this is code, text_type=TextType.CODE, url=www.code.com)'
        self.assertEqual(repr(node), expected)

    def test_textnode_repr_value_no_url(self):
        node = TextNode("this is normal", TextType.NORMAL)
        expected = 'TextNode(text=this is normal, text_type=TextType.NORMAL, url=None)'
        self.assertEqual(repr(node), expected)

    def test_textnode_notequal(self):
        node = TextNode("it's a trap", TextType.BOLD)
        node2 = TextNode("its a trap", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_textnode_equal(self):
        node = TextNode("identical", TextType.NORMAL, ".com")
        node2 = TextNode("identical", TextType.NORMAL, ".com")
        self.assertIsInstance(repr(node), str)
        self.assertIsInstance(repr(node2), str)
        self.assertEqual(node, node2)

    def test_textnode_to_htmlnode_normal_text(self):
        textnode = TextNode("normal placeholder text", TextType.NORMAL)
        trans = textnode.text_node_to_html_node()
        expected = LeafNode(value="normal placeholder text")
        self.assertEqual(trans, expected)
        
    def test_textnode_to_htmlnode_bold(self):
        textnode = TextNode(text="this will be bold", text_type=TextType.BOLD)
        trans = textnode.text_node_to_html_node()
        expected = LeafNode(value="this will be bold", tag="b")
        self.assertEqual(trans, expected)


    def test_textnode_to_htmlnode_italics(self):
        textnode = TextNode("will be italicized", TextType.ITALIC)
        trans = textnode.text_node_to_html_node()
        expected = LeafNode("will be italicized", "i")
        self.assertEqual(trans, expected)

    def test_textnode_to_htmlnode_code(self):
        textnode = TextNode("this is encrypted", TextType.CODE)
        trans = textnode.text_node_to_html_node()
        expected = LeafNode("this is encrypted", "code")
        self.assertEqual(trans, expected)

    def test_textnode_to_htmlnode_link(self):
        textnode = TextNode("click here!", TextType.LINKS, "https://youtube.com")
        trans = textnode.text_node_to_html_node()
        expected = LeafNode("click here!", "a", {"href": "https://youtube.com"})
        self.assertEqual(trans, expected)

    def test_textnode_to_htmlnode_image(self):
        textnode = TextNode("a cat", TextType.IMAGES, "~/catphotoes/cat1.jpeg")
        trans = textnode.text_node_to_html_node()
        expected = LeafNode("", "img", {
            "src": "~/catphotoes/cat1.jpeg",
            "alt": "a cat"
        })
        self.assertEqual(trans, expected)

if __name__ == "__main__":
    unittest.main()