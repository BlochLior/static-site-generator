import unittest
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter

class Testsplitdelimiter(unittest.TestCase):
    def test_splitdelimiter_multiple_delimiter_pairs(self):
        s1 = "**bold****text**"  # Multiple with space between
        s2 = "**bold** **text**" # Multiple with no space between
        node1 = TextNode(s1, TextType.NORMAL)
        node2 = TextNode(s2, TextType.NORMAL)
        old_nodes_list = [node1, node2]
        delimiter = "**"
        text_type = TextType.BOLD
        trans = split_nodes_delimiter(old_nodes_list, delimiter, text_type)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode("text", TextType.BOLD),
            TextNode("bold", TextType.BOLD),
            TextNode("text", TextType.BOLD)
        ]
        self.assertEqual(trans, expected)
    
    def test_splitdelimiter_partial_delimiter(self):
        with self.assertRaises(Exception):
            s1 = "`is this code?"
            s2 = "is this code?`"
            s3 = "is this code?"
            s4 = "*`is this code?`**"
            node1 = TextNode(s1, TextType.NORMAL)
            node2 = TextNode(s2, TextType.NORMAL)
            node3 = TextNode(s3, TextType.NORMAL)
            node4 = TextNode(s4, TextType.NORMAL)
            old_list = [node1, node2, node3, node4]
            delimiter = "`"
            text_type = TextType.CODE
            split_nodes_delimiter(old_list, delimiter, text_type)

    def test_splitdelimiter_no_delimiter(self):
        node1 = TextNode("`this isn't italics`", TextType.NORMAL)
        old_nodes = [node1]
        delimiter = "*"
        text_type = TextType.ITALIC
        trans = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected = old_nodes
        self.assertEqual(trans, expected)

if __name__ == "__main__":
    unittest.main()