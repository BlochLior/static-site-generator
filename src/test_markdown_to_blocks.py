import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdowntoBlocks(unittest.TestCase):
    def test_example_input(self):
        text = """# This is a heading


        This is a paragraph of text. It has some **bold** and *italic* words inside of it.


        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        trans = markdown_to_blocks(text)
        expected = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block\n* This is a list item\n* This is another list item"""
        ]
        self.assertEqual(trans, expected)

    def test_two_block(self):
        text = """First line
        Second line
        
        Third line
        Fourth line"""
        trans = markdown_to_blocks(text)
        expected = ["First line\nSecond line","Third line\nFourth line"]
        self.assertEqual(trans, expected)

    def test_empty_between_blocks(self):
        text = """First
        
        Second
        
        Third"""
        trans = markdown_to_blocks(text)
        expected = [
            "First", "Second", "Third"
        ]
        self.assertEqual(trans, expected)

    def test_empty_str(self):
        text = ""
        trans = markdown_to_blocks(text)
        expected = []
        self.assertEqual(trans, expected)

    def test_whitespace(self):
        text = "   \n   \n   "
        trans = markdown_to_blocks(text)
        expected = []
        self.assertEqual(trans, expected)

if __name__ == "__main__":
    unittest.main()