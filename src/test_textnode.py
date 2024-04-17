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

    def test_split_standard_text_nodes(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT.value)
        split_text_nodes = TextNode.parse_text_nodes([node], "`", TextType.CODE.value)

        self.assertIsInstance(split_text_nodes, list)
        self.assertEqual(len(split_text_nodes), 3)
        self.assertEqual(split_text_nodes[1].text_type, TextType.CODE.value)

    def test_split_invalid_text_nodes(self):
        node = TextNode("This is text with a `code block", TextType.TEXT.value)

        with self.assertRaises(ValueError) as cm:
            TextNode.parse_text_nodes([node], "`", TextType.CODE.value)

        self.assertEqual(cm.exception.args[0], "Invalid Markdown syntax")

    def test_split_unrecognized_text_nodes(self):
        node_1 = TextNode("This is text with a `code block`", "unrecognized_text_type")
        node_2 = "This is an unrecognized text node"
        split_text_nodes = TextNode.parse_text_nodes([node_1, node_2], "`", TextType.CODE.value)

        self.assertIsInstance(split_text_nodes, list)
        self.assertListEqual(split_text_nodes, [node_1, node_2])

if __name__ == "__main__":
    unittest.main()
