import unittest

from textnode import TextNode, TextType

"""
this test creates two TextNode objects with the same properties
and asserts that they are equal. if the test passes when running
in in the command ./test.sh, we did good. 
"""
class TestTextNode(unittest.TestCase):
    def test_1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertIsInstance(repr(node), str)
        self.assertIsInstance(repr(node2), str)
        print(node, node2)
        self.assertEqual(node, node2)
        
    def test_2(self):
        node = TextNode("it's a trap", TextType.BOLD)
        node2 = TextNode("its a trap", TextType.BOLD)
        self.assertIsInstance(repr(node), str)
        self.assertIsInstance(repr(node2), str)
        print(node, node2)
        self.assertNotEqual(node, node2)
    
    def test_3(self):
        node = TextNode("i am fine", TextType.ITALIC, "www.com")
        node2 = TextNode("this is pretty", TextType.IMAGES, ".png")
        self.assertIsInstance(repr(node), str)
        self.assertIsInstance(repr(node2), str)
        print(node, node2)
        self.assertNotEqual(node, node2)

    def test_4(self):
        node = TextNode("identical", TextType.NORMAL, ".com")
        node2 = TextNode("identical", TextType.NORMAL, ".com")
        node3 = TextNode("i_dentical", TextType.NORMAL, ".com")
        self.assertIsInstance(repr(node), str)
        self.assertIsInstance(repr(node2), str)
        self.assertIsInstance(repr(node3), str)
        print(node, node2, node3)
        self.assertNotEqual(node, node3)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()