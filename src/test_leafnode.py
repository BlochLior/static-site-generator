import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_1(self):
        node1 = LeafNode("p", "this is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.com"})
        node3 = LeafNode("img", None, {
            "src": "url/of/image.jpg",
            "alt": "this is an image"
        })
        self.assertIsInstance(repr(node1), str)
        self.assertIsInstance(repr(node2), str)
        self.assertIsInstance(repr(node3), str)
        print(node1, node2, node3)
        node1.to_html()
        node2.to_html()
        with self.assertRaises(ValueError): node3.to_html()
        print(node1.props_to_html(), node2.props_to_html(), node3.props_to_html())
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node2, node3)
    
    def test_2(self):
        node1 = LeafNode("p", "parararrarargraph")
        node2 = LeafNode("p", "parararrarargraph")
        self.assertEqual(node1, node2)

    def test_3(self):
        node = LeafNode("any", "any")
        self.assertIsInstance(node, LeafNode)



if __name__ == "__main__":
    unittest.main()