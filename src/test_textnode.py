import unittest

from textnode import TextNode, TextType

"""
this test creates two TextNode objects with the same properties
and asserts that they are equal. if the test passes when running
in in the command ./test.sh, we did good. 
"""
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_no_equal(self):
        node = TextNode("it's a trap", TextType.BOLD)
        node2 = TextNode("its a trap", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_2_no_equal(self):
        node = TextNode("i am fine", TextType.ITALIC, "www.com")
        node2 = TextNode("this is pretty", TextType.IMAGES, ".png")
        self.assertNotEqual(node, node2)

    def test_3_multiple(self):
        node = TextNode("identical", TextType.NORMAL, ".com")
        node2 = TextNode("identical", TextType.NORMAL, ".com")
        node3 = TextNode("i_dentical", TextType.NORMAL, ".com")
        self.assertNotEqual(node, node3)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()