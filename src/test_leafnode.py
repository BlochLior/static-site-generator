import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode_constructor(self):
        node = LeafNode(tag="span", value="Hello World")
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Hello World")
        self.assertEqual(node.props, {})

    def test_leafnode_with_props(self):
        # Test that props are correctly passed and stored in a LeafNode
        node = LeafNode(tag="span", value="Hello", props={"class": "highlight"})
        self.assertEqual(node.tag, "span")  # Verify tag
        self.assertEqual(node.value, "Hello")  # Verify value
        self.assertEqual(node.props, {"class": "highlight"})  # Verify props

    def test_leafnode_to_html_with_tag(self):
        node = LeafNode(tag="b", value="Bold text", props={"style": "font-weight:bold"})
        expected = '<b style="font-weight:bold">Bold text</b>'
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_to_html_without_tag_text_only_output(self):
        node = LeafNode(tag=None, value="Plain text")
        expected = "Plain text"
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_missing_value_raises_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="b", value=None)
            node.to_html()

    def test_leafnode_empty_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="b", value="")
            node.to_html()
            

    def test_leafnode_invalid_props(self):
        with self.assertRaises(ValueError): #insert here the actual error it should raise
            LeafNode(tag="a", value="link", props="not-a-dict")
    
    def test_leafnode_multiple_props(self):
        node = LeafNode(tag="img", value="pasted", props={"src": "image.png", "alt": "an image"})
        expected = '<img src="image.png" alt="an image">pasted</img>'
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_no_tag_and_no_value_raises_error(self):
        with self.assertRaises(ValueError): 
            node = LeafNode(None, None)
            node.to_html()

    def test_leafnode_whitespace_value(self):
        node = LeafNode(tag="p", value="  ")
        expected = '<p>  </p>'
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()