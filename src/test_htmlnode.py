import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_repr(self):
        node1 = HTMLNode("div")
        expected = 'HTMLNode(tag=div, value=None)'
        self.assertEqual(repr(node1), expected)
        
    def test_htmlnode_empty_node(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_htmlnode_repr_with_multiple_props(self):
        node = HTMLNode(tag="div", props={"class": "header", "id": "main"})
        expected = "HTMLNode(tag=div, value=None, props={class='header', id='main'})"
        self.assertEqual(repr(node), expected)

    def test_htmlnode_repr_with_empty_value(self):
        node = HTMLNode(value="")
        expected = "HTMLNode(tag=None, value=)"
        self.assertEqual(repr(node), expected)

    def test_htmlnode_repr_with_empty_tag(self):
        node = HTMLNode(tag="")
        expected = "HTMLNode(tag=, value=None)"
        self.assertEqual(repr(node), expected)

    def test_htmlnode_repr_with_empty_children(self):
        node = HTMLNode(children="")
        expected = "HTMLNode(tag=None, value=None)"
        self.assertEqual(repr(node), expected)

    def test_htmlnode_to_html(self):
        html_node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            html_node.to_html()

    def test_htmlnode_props_to_html(self):
        node = HTMLNode(None, None, None, {
            "src": "url.png",
            "alt": "description of png"
        })
        expected = 'src="url.png" alt="description of png"'
        self.assertEqual(node.props_to_html(), expected)

    def test_htmlnode_no_props_to_html(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_htmlnode_props_to_html_large_props(self):
        props = {f"key{i}": f"value{i}" for i in range(1000)}
        node = HTMLNode(props=props)
        expected = " ".join([f'key{i}="value{i}"' for i in range(1000)])
        self.assertEqual(node.props_to_html(), expected)

    def test_htmlnode_invalid_props(self):
        node = HTMLNode(props={"src": None, "class": "main"})
        expected = 'class="main"'
        self.assertEqual(node.props_to_html(), expected)

    def test_htmlnode_partial_arguments_mixed_scenario(self):
        #following is mixed scenario, so as not to prove redundant
        node = HTMLNode("div", props={"id": "test_id"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, None)
        self.assertEqual(node.props, {"id": "test_id"})
        self.assertEqual(node.children, [])

    def test_htmlnode_equal(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_htmlnode_notequal(self):
        node1 = HTMLNode("a")
        node2 = HTMLNode("b")
        self.assertNotEqual(node1, node2)
    
    def test_htmlnode_notequal_with_diff_prop_values(self):
        node1 = HTMLNode(props={"src": "image1.jpg"})
        node2 = HTMLNode(props={"src": "image2.jpg"})
        self.assertNotEqual(node1, node2)


    def test_htmlnode_notequal_with_diff_values_else_same(self):
        node1 = HTMLNode(value="placeholder")
        node2 = HTMLNode(value="Placeholder")
        self.assertNotEqual(node1, node2)
        

    def test_htmlnode_children_with_non_htmlnode_objects_raise_valueerror(self):
        with self.assertRaises(ValueError):
            # Attempting to create an HTMLNode with an invalid child (non-HTMLNode object)
            HTMLNode(children=[HTMLNode(), 5])

    def test_htmlnode_equality_with_valid_children(self):
        child1 = HTMLNode()
        node1 = HTMLNode(children=[child1])
        node2 = HTMLNode(children=[HTMLNode(tag=child1.tag, props=child1.props)])
        self.assertEqual(node1, node2)

    def test_htmlnode_equality_with_nested_children(self):
        child1 = HTMLNode(tag="span", props={"style": "color:red"})
        nested_child1 = HTMLNode(tag="div", children=[child1])
        nested_child2 = HTMLNode(tag="div", children=[HTMLNode(tag="span", props={"style": "color:red"})])  # Recreated child
        node1 = HTMLNode(children=[nested_child1])
        node2 = HTMLNode(children=[nested_child2])  # Identical structure with nested children
        self.assertEqual(node1, node2)  # Should pass
    
    def test_htmlnode_inequality_with_different_children(self):
        child1 = HTMLNode(tag="div", props={"class": "child"})
        child2 = HTMLNode(tag="span", props={"class": "different-child"})  # Different tag and props
        node1 = HTMLNode(children=[child1])
        node2 = HTMLNode(children=[child2])  # Different child structure
        self.assertNotEqual(node1, node2)  # Should pass; they are not equal
    
    def test_htmlnode_equality_with_empty_children(self):
        node1 = HTMLNode(children=[])
        node2 = HTMLNode(children=[])  # Both have no children
        self.assertEqual(node1, node2)  # Should pass

    def test_htmlnode_inequality_with_different_children_order(self):
        child1 = HTMLNode(tag="b", value="Bold text")
        child2 = HTMLNode(tag="i", value="Italic text")
        node1 = HTMLNode(children=[child1, child2])  # b, then i
        node2 = HTMLNode(children=[child2, child1])  # i, then b (different order)
        self.assertNotEqual(node1, node2)  # Should pass; not equal because order matters

if __name__ == "__main__":
    unittest.main()