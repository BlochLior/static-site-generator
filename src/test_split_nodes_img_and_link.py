import unittest
import re

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from extract_links_images import extract_markdown_links, extract_markdown_images
from split_nodes_img_and_link import split_nodes_image, split_nodes_link

class Testsplitnodesimgandlinks(unittest.TestCase):

    def test_split_nodes_link_wrong_text_type(self):
        node = TextNode("link", TextType.LINKS, "https://www.google.com")
        trans = split_nodes_link([node])
        expected = [node]
        self.assertEqual(trans, expected)

    def test_split_nodes_link_one(self):
        node = TextNode("A link to [Boot.dev](https://boot.dev).", TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = [
            TextNode("A link to", TextType.NORMAL),
            TextNode("Boot.dev", TextType.LINKS, "https://boot.dev"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)
    
    def test_split_nodes_img_one(self):
        text = "Here is an image ![img](link)."
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = [
            TextNode("Here is an image", TextType.NORMAL),
            TextNode("img", TextType.IMAGES, "link"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)
        

    def test_split_nodes_link_multiple_nodes(self):
        old_nodes = [
            TextNode("Explore the great ", TextType.NORMAL),
            TextNode("[Boot.dev](https://boot.dev) for deep learning and fun!", TextType.NORMAL),
            TextNode("Alongside it, you will find knowledge aplenty.", TextType.NORMAL),
            TextNode("Check out this resource: [Another Link](https://example.com)", TextType.NORMAL),
            TextNode("This is just some plain text to finish.", TextType.NORMAL)
            ]
        trans = split_nodes_link(old_nodes)
        expected = [
            TextNode("Explore the great", TextType.NORMAL),
            TextNode("Boot.dev", TextType.LINKS, "https://boot.dev"),
            TextNode("for deep learning and fun!", TextType.NORMAL),
            TextNode("Alongside it, you will find knowledge aplenty.", TextType.NORMAL),
            TextNode("Check out this resource:", TextType.NORMAL),
            TextNode("Another Link", TextType.LINKS, "https://example.com"),
            TextNode("This is just some plain text to finish.", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)

    def test_split_nodes_images_multiple(self):
        text = "Here are images ![img1](link1) and ![img2](link2)."
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = [
            TextNode("Here are images", TextType.NORMAL),
            TextNode("img1", TextType.IMAGES, "link1"),
            TextNode("and", TextType.NORMAL),
            TextNode("img2", TextType.IMAGES, "link2"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)

    def test_split_nodes_links_multiple(self):
        text = "Here are links [Home](https://boot.dev) and [Docs](https://docs.boot.dev)."
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = [
            TextNode("Here are links", TextType.NORMAL),
            TextNode("Home", TextType.LINKS, "https://boot.dev"),
            TextNode("and", TextType.NORMAL),
            TextNode("Docs", TextType.LINKS, "https://docs.boot.dev"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)

    def test_split_nodes_links_images_both_order_1(self):
        text = "Text with an image ![img](link) and a link [here](https://boot.dev)."
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image(split_nodes_link([node]))
        expected = [
            TextNode("Text with an image", TextType.NORMAL),
            TextNode("img", TextType.IMAGES, "link"),
            TextNode("and a link", TextType.NORMAL),
            TextNode("here", TextType.LINKS, "https://boot.dev"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)

    def test_split_nodes_links_images_both_order_2(self):
        text = "Text with an image ![img](link) and a link [here](https://boot.dev)."
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link(split_nodes_image([node]))
        expected = [
            TextNode("Text with an image", TextType.NORMAL),
            TextNode("img", TextType.IMAGES, "link"),
            TextNode("and a link", TextType.NORMAL),
            TextNode("here", TextType.LINKS, "https://boot.dev"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)

    def test_split_nodes_no_match_images(self):
        text = "This is a text node with no images or links."
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = [node]
        self.assertEqual(trans, expected)
    
    def test_split_nodes_no_match_links(self):
        text = "This is a text node with no images or links."
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = [node]
        self.assertEqual(trans, expected)

    def test_split_nodes_img_empty(self):
        text = ""
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = []
        self.assertEqual(trans, expected)

    def test_split_nodes_link_space(self):
        text = " "
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = []
        self.assertEqual(trans, expected)

    def test_split_nodes_incomplete_image(self):
        text = "Here is an incomplete image ![alt text](link"
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = [node]
        self.assertEqual(trans, expected)

    def test_split_nodes_incomplete_link(self):
        text = "Check out this [link here](https://example.com"
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = [node]
        self.assertEqual(trans, expected)

    def test_split_nodes_img_link_incomplete_both_1(self):
        text = "![img alt]( and [link](https://example.com"
        node = TextNode(text, TextType.NORMAL)
        trans1 = split_nodes_image(split_nodes_link([node]))
        trans2 = split_nodes_link(split_nodes_image([node]))
        expected = [node]
        self.assertEqual(trans1, expected)
        self.assertEqual(trans2, expected)


    def test_split_nodes_img_link_incomplete_both_2(self):
        text = "![alt](url[incorrect(nested))"
        node = TextNode(text, TextType.NORMAL)
        trans1 = split_nodes_image(split_nodes_link([node]))
        trans2 = split_nodes_link(split_nodes_image([node]))
        expected = [node]
        self.assertEqual(trans1, expected)
        self.assertEqual(trans2, expected)

    def test_split_nodes_image_only(self):
        text = "![alt text](url)"
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = [TextNode("alt text", TextType.IMAGES, "url")]
        self.assertEqual(trans, expected)

    def test_split_nodes_link_only(self):
        text = "[link text](url)"
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = [TextNode("link text", TextType.LINKS, "url")]
        self.assertEqual(trans, expected)

    def test_split_nodes_image_at_end(self):
        text = "Some text before the last image ![img](link)"
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = [
            TextNode("Some text before the last image", TextType.NORMAL),
            TextNode("img", TextType.IMAGES, "link")
            ]
        self.assertEqual(trans, expected)

    def test_split_nodes_link_at_start(self):
        text = "[link](url) this starts with a link, will your test handle?"
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = [
            TextNode("link", TextType.LINKS, "url"),
            TextNode("this starts with a link, will your test handle?", TextType.NORMAL)
            ]
        self.assertEqual(trans, expected)

    def test_split_nodes_image_extremely_long_string(self):
        text = " ".join(f"![img{i}](url{i})" for i in range(100))
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = []
        for i in range(100):
            expected.append(TextNode(f"img{i}", TextType.IMAGES, f"url{i}"))
        self.assertEqual(trans, expected)
        
    def test_split_nodes_link_extremely_long_string(self):
        text = " ".join(f"[link{i}](https://example.com/{i})" for i in range(100))
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = []
        for i in range(100):
            expected.append(TextNode(f"link{i}", TextType.LINKS, f"https://example.com/{i}"))
        self.assertEqual(trans, expected)
        
    def test_split_nodes_image_intersperesed_long(self):
        text = "Some text " + " ".join(f"![img{i}](url{i}) and more text" for i in range(50))
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = [TextNode("Some text", TextType.NORMAL)]
        for i in range(50):
            expected.append(TextNode(f"img{i}", TextType.IMAGES, f"url{i}"))
            expected.append(TextNode("and more text", TextType.NORMAL))
        self.assertEqual(trans, expected)

    def test_split_nodes_link_intersperesed_long(self):
        text = "Click here " + " ".join(f"[link{i}](https://example.com/{i}) for details" for i in range(50))
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = [TextNode("Click here", TextType.NORMAL)]
        for i in range(50):
            expected.append(TextNode(f"link{i}", TextType.LINKS, f"https://example.com/{i}")),
            expected.append(TextNode("for details", TextType.NORMAL))
        self.assertEqual(trans, expected)

    def test_split_nodes_link_image_random_input(self):
        text = "Random text ![img](url) [link](url) ![img2](url2) text without markdown {random text}"
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image(split_nodes_link([node]))
        expected = [
            TextNode("Random text", TextType.NORMAL),
            TextNode("img", TextType.IMAGES, "url"),
            TextNode("link", TextType.LINKS, "url"),
            TextNode("img2", TextType.IMAGES, "url2"),
            TextNode("text without markdown {random text}", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)

    def test_split_nodes_image_stability(self):
        text = "Some![img1](url1)text![img2](url2)more![img3](url3)."
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = [
            TextNode("Some", TextType.NORMAL),
            TextNode("img1", TextType.IMAGES, "url1"),
            TextNode("text", TextType.NORMAL),
            TextNode("img2", TextType.IMAGES, "url2"),
            TextNode("more", TextType.NORMAL),
            TextNode("img3", TextType.IMAGES, "url3"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)

    def test_split_nodes_link_stability(self):
        text = "Find[link1](https://url1)[link2](https://url2)here[link3](https://url3)."
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_link([node])
        expected = [
            TextNode("Find", TextType.NORMAL),
            TextNode("link1", TextType.LINKS, "https://url1"),
            TextNode("link2", TextType.LINKS, "https://url2"),
            TextNode("here", TextType.NORMAL),
            TextNode("link3", TextType.LINKS, "https://url3"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(trans, expected)

    def test_split_nodes_image_link_unexpected_int(self):
        with self.assertRaises(TypeError):
            text = 1234
            split_nodes_image(text)

    def test_split_nodes_image_link_unexpected_list(self):
        with self.assertRaises(TypeError):
            text = ["string inside list"]
            split_nodes_link(text)
        
    def test_split_nodes_image_link_unexpected_None(self):
        with self.assertRaises(TypeError):
            text = None
            split_nodes_link(text)
        
    def test_split_nodes_image_link_random(self):
        text = "!!! *** ??? [[[]]]>>><<<"
        node = TextNode(text, TextType.NORMAL)
        trans = split_nodes_image([node])
        expected = [node]
        self.assertEqual(trans, expected)



if __name__ == "__main__":
    unittest.main()