import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.default_node = HTMLNode()
        self.standard_node = HTMLNode(
            "a",
            "Google",
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )
    
    def test_default_properties(self):
        self.assertIsNone(self.default_node.tag)
        self.assertIsNone(self.default_node.value)
        self.assertIsNone(self.default_node.children)
        self.assertIsNone(self.default_node.props)

    def test_standard_properties(self):
        self.assertEqual(self.standard_node.tag, "a")
        self.assertEqual(self.standard_node.value, "Google")
        self.assertIsNone(self.standard_node.children)
        self.assertIn("href", self.standard_node.props) # type: ignore

    def test_to_html(self):
        self.assertRaises(NotImplementedError, self.default_node.to_html)

    def test_props_to_html(self):
        self.assertEqual(
            self.standard_node.props_to_html(),
            " href=\"https://www.google.com\" target=\"_blank\""
        )

    def test_representation(self):
        self.assertEqual(
            repr(self.standard_node),
            "HTMLNode(a, Google, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        )

if __name__ == "__main__":
    unittest.main()
