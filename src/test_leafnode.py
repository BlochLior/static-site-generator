import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode_constructor(self):
        node = LeafNode("span", "Hello World")
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.props, {})

    def test_leafnode_with_props(self):
        # Test that props are correctly passed and stored in a LeafNode
        node = LeafNode("span", "Hello", {"class": "highlight"})
        self.assertEqual(node.tag, "span")  # Verify tag
        self.assertEqual(node.value, "Hello")  # Verify value
        self.assertEqual(node.props, {"class": "highlight"})  # Verify props

    def test_leafnode_to_html_with_tag(self):
        node = LeafNode("b", "Bold text", {"style": "font-weight:bold"})
        expected = '<b style="font-weight:bold">Bold text</b>'
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_to_html_without_tag_text_only_output(self):
        node = LeafNode(None, "Plain text")
        expected = "Plain text"
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_missing_value_raises_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("b", None)
            node.to_html()

    def test_leafnode_empty_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("b", "")
            node.to_html()
            

    def test_leafnode_invalid_props(self):
        with self.assertRaises(ValueError): #insert here the actual error it should raise
            LeafNode("a", "link", "not-a-dict")
    
    def test_leafnode_multiple_props(self):
        node = LeafNode("img", "pasted", {"src": "image.png", "alt": "an image"})
        expected = '<img src="image.png" alt="an image">pasted</img>'
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_no_tag_and_no_value_raises_error(self):
        with self.assertRaises(ValueError): 
            node = LeafNode(None, None)
            node.to_html()

    def test_leafnode_whitespace_value(self):
        node = LeafNode("p", "  ")
        expected = '<p>  </p>'
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()