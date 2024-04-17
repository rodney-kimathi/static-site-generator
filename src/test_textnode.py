import unittest

from text_type import TextType
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.default_node = TextNode("Text node", TextType.TEXT.value)
        self.standard_node = TextNode("Text node", TextType.BOLD.value, "https://www.google.com")
    
    def test_similar_properties(self):
        another_default_node = TextNode("Text node", TextType.TEXT.value)
        self.assertEqual(self.default_node, another_default_node)

    def test_different_properties(self):
        another_default_node = TextNode("Another text node", TextType.ITALIC.value)
        self.assertNotEqual(self.default_node, another_default_node)

    def test_similar_url(self):
        another_standard_node = TextNode("Text node", TextType.BOLD.value, "https://www.google.com")
        self.assertEqual(self.standard_node, another_standard_node)

    def test_default_url(self):
        self.assertIsNone(self.default_node.url)

    def test_representation(self):
        self.assertEqual(repr(self.standard_node), "TextNode(Text node, bold, https://www.google.com)")

    def test_parse_valid_text_nodes(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT.value)
        split_text_nodes = TextNode.parse_text_nodes([node], "`", TextType.CODE.value)

        self.assertIsInstance(split_text_nodes, list)
        self.assertEqual(len(split_text_nodes), 3)
        self.assertEqual(split_text_nodes[1].text_type, TextType.CODE.value)

    def test_parse_invalid_text_nodes(self):
        node = TextNode("This is text with a `code block", TextType.TEXT.value)

        with self.assertRaises(ValueError) as cm:
            TextNode.parse_text_nodes([node], "`", TextType.CODE.value)

        self.assertEqual(cm.exception.args[0], "Invalid Markdown syntax")

    def test_parse_unrecognized_text_nodes(self):
        node_1 = TextNode("This is text with a `code block`", "unrecognized_text_type")
        node_2 = "This is an unrecognized text node"
        split_text_nodes = TextNode.parse_text_nodes([node_1, node_2], "`", TextType.CODE.value)

        self.assertIsInstance(split_text_nodes, list)
        self.assertListEqual(split_text_nodes, [node_1, node_2])

    def test_extract_valid_markdown_images(self):
        text = """
        This is text with an ![image](https://storage.googleapis.com/image.png) and 
        ![another-image](https://storage.googleapis.com/another-image.png)
        """
        images = TextNode.extract_markdown_images(text)

        self.assertListEqual(
            images,
            [
                ("image", "https://storage.googleapis.com/image.png"), 
                ("another-image", "https://storage.googleapis.com/another-image.png")
            ]
        )

    def test_extract_invalid_markdown_images(self):
        text_1 = """
        This is text with an !(https://storage.googleapis.com/image.png) and 
        !(https://storage.googleapis.com/another-image.png)
        """
        text_2 = "This is text with an ![]() and ![]()"
        images_1 = TextNode.extract_markdown_images(text_1)
        images_2 = TextNode.extract_markdown_images(text_2)

        self.assertListEqual(images_1, [])
        self.assertListEqual(images_2, [])

    def test_extract_valid_markdown_links(self):
        text = """
        This is text with a [link](https://example.com) and 
        [another-link](https://another-example.com)
        """
        links = TextNode.extract_markdown_links(text)

        self.assertListEqual(
            links,
            [("link", "https://example.com"), ("another-link", "https://another-example.com")]
        )

    def test_extract_invalid_markdown_links(self):
        text_1 = "This is text with a (https://example.com) and (https://another-example.com)"
        text_2 = "This is text with an []() and []()"
        links_1 = TextNode.extract_markdown_images(text_1)
        links_2 = TextNode.extract_markdown_images(text_2)

        self.assertListEqual(links_1, [])
        self.assertListEqual(links_2, [])

if __name__ == "__main__":
    unittest.main()
