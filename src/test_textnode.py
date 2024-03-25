import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.default_node = TextNode("This is a text node", "bold")
        self.standard_node = TextNode("This is a text node", "bold", "https://www.google.com")
    
    def test_similar_properties(self):
        another_default_node = TextNode("This is a text node", "bold")
        self.assertEqual(self.default_node, another_default_node)

    def test_different_properties(self):
        another_default_node = TextNode("This is another text node", "italic")
        self.assertNotEqual(self.default_node, another_default_node)

    def test_similar_url(self):
        another_standard_node = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(self.standard_node, another_standard_node)

    def test_default_url(self):
        self.assertIsNone(self.default_node.url)

    def test_representation(self):
        self.assertEqual(repr(self.standard_node), "TextNode(This is a text node, bold, https://www.google.com)")

if __name__ == "__main__":
    unittest.main()
