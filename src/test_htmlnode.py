import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertIsInstance(repr(node1), str)
        self.assertIsInstance(repr(node2), str)
        print(node1, node2)
        self.assertEqual(node1, node2)

    def test_2(self):
        node2 = HTMLNode("p", "this is a paragraph")
        node3 = HTMLNode("p", "this is a paragraph")
        node1 = HTMLNode("code", "this is code", [node3, node2])
        node4 = HTMLNode("img", None, None, {
            "src": "url.jpg", 
            "alt": "description of image" 
            } )
        self.assertIsInstance(repr(node1), str)
        self.assertIsInstance(repr(node2), str)
        self.assertIsInstance(repr(node3), str)
        self.assertIsInstance(repr(node4), str)
        print(node1, node2, node3, node4)
        node4.props_to_html()
        self.assertEqual(node2, node3)
        self.assertNotEqual(node1, node4)
    
    def test_3(self):
        node1 = HTMLNode("a", "link", None, {
            "href": "https.com"
        })
        node2 = HTMLNode("a", "link", None, {
            "href": "google.com"
        })
        node3 = HTMLNode("img", None, None, {
            "src": "google.com",
            "alt": "https is best http"
        })
        self.assertIsInstance(repr(node1), str)
        self.assertIsInstance(repr(node2), str)
        self.assertIsInstance(repr(node3), str)
        print(node1, node2, node3)
        print(node1.props_to_html(), node2.props_to_html(), node3.props_to_html())
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node2, node3)

if __name__ == "__main__":
    unittest.main()