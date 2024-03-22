import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_equal_similar(self):
        a_node = TextNode("This is a text node", "bold")
        another_node = TextNode("This is a text node", "bold")

        self.assertEqual(a_node, another_node)

    def test_not_equal_different(self):
        a_node = TextNode("This is a text node", "bold")
        another_node = TextNode("This is another text node", "italic")

        self.assertNotEqual(a_node, another_node)

    def test_equal_similar_url(self):
        a_node = TextNode("This is a text node", "bold", "https://www.google.com")
        another_node = TextNode("This is a text node", "bold", "https://www.google.com")

        self.assertEqual(a_node, another_node)

    def test_equal_default_url(self):
        a_node = TextNode("This is a text node", "bold")

        self.assertEqual(a_node.url, None)

    def test_equal_representation(self):
        a_node = TextNode("This is a text node", "bold", "https://www.google.com")

        self.assertEqual(repr(a_node), "TextNode(This is a text node, bold, https://www.google.com)")

if __name__ == "__main__":
    unittest.main()
