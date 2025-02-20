import unittest

from textnode import TextNode, TextType

"""
this test creates two TextNode objects with the same properties
and asserts that they are equal. if the test passes when running
in in the command ./test.sh, we did good. 
"""
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


if __name__ == "__main__":
    unittest.main()