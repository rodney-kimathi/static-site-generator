import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def setUp(self):
        self.default_node = LeafNode(None, "Default leaf node")
        self.standard_node = LeafNode("a", "Standard leaf node", {"href": "https://www.google.com"})

    def test_default_properties(self):
        self.assertIsNone(self.default_node.tag)
        self.assertEqual(self.default_node.value, "Default leaf node")
        self.assertIsNone(self.default_node.props)

    def test_standard_properties(self):
        self.assertEqual(self.standard_node.tag, "a")
        self.assertEqual(self.standard_node.value, "Standard leaf node")
        self.assertIn("href", self.standard_node.props) # type: ignore

    def test_to_html(self):
        self.assertEqual(
            self.standard_node.to_html(),
            "<a href=\"https://www.google.com\">Standard leaf node</a>"
        )

    def test_representation(self):
        self.assertEqual(
            repr(self.standard_node),
            "LeafNode(a, Standard leaf node, {'href': 'https://www.google.com'})"
        )

if __name__ == "__main__":
    unittest.main()
