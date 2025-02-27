import re
import unittest
from enum import Enum
from blocktype import *

class TestBlockType(unittest.TestCase):
    def test_blocktype_simple_heading(self):
        block = "# Heading 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_blocktype_multiple_hashtags(self):
        block = "### Heading 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_blocktype_maximum_valid_heading_level(self):
        block = "###### Heading 6"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_blocktype_invalid_heading(self):
        block = "#NoSpace_Paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_too_many_hashatags(self):
        block = "####### too many #'s"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_code(self):
        block = "```\ncode here\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_blocktype_code_with_specified_lang(self):
        block = "```python\ndef test():\n    pass\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_invalid_code_block(self):
        block = "```\nnot code here"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_simple_quote(self):
        block = "> this is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_multi_line_quote(self):
        block = "> Line 1\n> Line 2\n> Line 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_blocktype_missing_mark_on_one_quoteline(self):
        block = "> Line 1\nLine 2\n> Line 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_single_item_list(self):
        block = "- Item 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_blocktype_multi_item_ul(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_blocktype_invalid_ul(self):
        block = "-Item 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_invalid_ul_one_line_miss(self):
        block = "- Item 1\nItem 2\n- Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_wrong_marker_for_ul(self):
        block = "* Item 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_single_item_ordered(self):
        block = "1. Item 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
    def test_blocktype_multi_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_blocktype_invalid_ol_numbering(self):
        block = "1. Item 1\n3. Item 2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_invalid_ol_no_space(self):
        block = "1.Item 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_invalid_ol_non_sequentaial(self):
        block = "1. Item 1\n1. Item 2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_simple_paragraph(self):
        block = "this is a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_multi_line_par(self):
        block = "This is line 1\nThis is line 2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_rando_symbols_paragraph(self):
        block = "This has # but not at start\nAnd > in the middle"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_empty_string(self):
        block = ""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_no_matching_complete_pattern(self):
        block = "- Item 1\n1. Item 2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_very_similar(self):
        block = "This has ``` backticks but not as a code block"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_blocktype_very_similar_2(self):
        block = "> This is a quote line\nThis is not a quote line"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
        
if __name__ == "__main__":
    unittest.main()