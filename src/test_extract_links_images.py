from extract_links_images import extract_markdown_images, extract_markdown_links
import unittest
import re

class Testextract(unittest.TestCase):
    
    def test_extract_markdown_images_basic_case(self):
        text = "Here's an ![image](https://example.com/pic.jpg)"
        trans = extract_markdown_images(text)
        expected = [
            ("image", "https://example.com/pic.jpg")
        ]
        self.assertEqual(trans, expected)

    def test_extract_markdown_links_basic_case(self):
        text = "Here's a [link](https://example.com)"
        trans = extract_markdown_links(text)
        expected = [("link", "https://example.com")]
        self.assertEqual(expected, trans)

    def test_extract_markdown_images_multiple_items(self):
        text = "Multiple ![image1](url1) and ![image2](url2)"
        trans = extract_markdown_images(text)
        expected = [
            ("image1", "url1"), ("image2", "url2")
        ]
        self.assertEqual(trans, expected)

    def test_extract_markdown_links_multiple_items(self):
        text = "Multiple [link1](url1) and [link2](url2)"
        trans = extract_markdown_links(text)
        expected = [
            ("link1", "url1"), ("link2", "url2")
        ]
        self.assertEqual(trans, expected)


    def test_extract_markdown_links_no_match(self):
        text = "Empty text"
        trans = extract_markdown_links(text)
        expected = []
        self.assertEqual(trans, expected)

    def test_extract_markdown_images_no_match(self):
        text = "Empty text"
        trans = extract_markdown_images(text)
        expected = []
        self.assertEqual(trans, expected)

    def test_extract_markdown_links_wrong_syntax(self):
        text = "Wrong syntax [link(url)]"
        trans = extract_markdown_links(text)
        expected = []
        self.assertEqual(trans, expected)

    def test_extract_markdown_images_wrong_syntax(self):
        text = "Wrong syntax ![image(url)"
        trans = extract_markdown_images(text)
        expected = []
        self.assertEqual(trans, expected)

    def test_extract_markdown_images_incomplete_features(self):
        text = "Incomplete ![image]()"
        trans = extract_markdown_images(text)
        expected = [("image", "")]
        self.assertEqual(trans, expected)

    def test_extract_markdown_links_incomplete_features(self):
        text = "Incomplete [link]()"
        trans = extract_markdown_links(text)
        expected = [("link", "")]
        self.assertEqual(trans, expected)

    def test_extract_markdown_items_mixed_case(self):
        text = "Mixed ![image](img_url) and [link](link_url)"
        trans1 = extract_markdown_images(text)
        trans2 = extract_markdown_links(text)
        trans = trans1 + trans2
        expected = [("image", "img_url"), ("link", "link_url")]
        self.assertEqual(trans, expected)

    def test_extract_markdown_images_long_string(self):
        long_string = "".join([f"this is ![image{i}](img_url{i})" for i in range(1000)])
        trans = extract_markdown_images(long_string)
        expected = [(f"image{i}", f"img_url{i}") for i in range(1000)]
        self.assertEqual(trans, expected)

    def test_extract_markdown_links_long_string(self):
        long_string = "".join([f"this is [link{i}](link_url{i})" for i in range(1000)])
        trans = extract_markdown_links(long_string)
        expected = [(f"link{i}", f"link_url{i}") for i in range(1000)]
        self.assertEqual(trans, expected)

if __name__ == "__main__":
    unittest.main()