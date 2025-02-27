import unittest
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parentnode_none_tag_to_html(self):
        with self.assertRaises(ValueError):
            child = LeafNode("placeholder", "placeholder")
            node = ParentNode(None, children=[child])
            node.to_html()

    def test_parentnode_no_children_to_html(self):
        with self.assertRaises(ValueError):
            node = ParentNode("a", None)
            node.to_html()
    
    def test_parentnode_single_child_to_html(self):
        child = LeafNode(tag="li", value="Item 1")
        node = ParentNode("ul", [child])
        expected = "<ul><li>Item 1</li></ul>"
        self.assertEqual(node.to_html(), expected)
    
    def test_parent_with_multiple_children(self):
        children = [
            LeafNode(tag="b", value="Bold"),
            LeafNode(tag=None, value="Normal"),
            LeafNode(tag="i", value="Italic")
        ]
        node = ParentNode("p", children)
        expected = "<p><b>Bold</b>Normal<i>Italic</i></p>"
        self.assertEqual(node.to_html(), expected)

    def test_nested_parent_nodes(self):
        inner_parent = ParentNode("p", [LeafNode(tag="span", value="Hello")])
        outer_parent = ParentNode("div", [inner_parent])
        expected = "<div><p><span>Hello</span></p></div>"
        self.assertEqual(outer_parent.to_html(), expected)

    def test_complex_list_structure(self):
        list_items = [
            LeafNode(tag="li", value="Item 1"),
            LeafNode(tag="li", value="Item 2"),
            LeafNode(tag="li", value="Item 3")
        ]
        unordered_list = ParentNode("ul", list_items)
        expected = "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        self.assertEqual(unordered_list.to_html(), expected)

    def test_deeply_nested_structure(self):
        deep_structure = ParentNode("div", [
            ParentNode("p", [
                LeafNode(tag="strong", value="Important"),
                LeafNode(tag=None, value=" and "),
                LeafNode(tag="em", value="emphasized"),
                LeafNode(tag=None, value=" text")
            ])
        ])
        expected = "<div><p><strong>Important</strong> and <em>emphasized</em> text</p></div>"
        self.assertEqual(deep_structure.to_html(), expected)    

if __name__ == "__main__":
    unittest.main()