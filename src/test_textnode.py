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

if __name__ == "__main__":
    unittest.main()
