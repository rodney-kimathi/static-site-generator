import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def setUp(self):
        self.props = {"class": "a-class"}
        self.normal_text = LeafNode("span", "Normal")
        self.bold_text = LeafNode("b", "Bold")
        self.italic_text = LeafNode("i", "Italic")
        self.anchor_leaf_node = LeafNode("a", "Anchor")
        self.paragraph_parent_node = ParentNode("p", [])
        self.default_parent_node = ParentNode("span", [])
        self.standard_parent_node = ParentNode("div", [])

    def test_default_properties(self):
        self.assertEqual(self.default_parent_node.tag, "span")
        self.assertListEqual(self.default_parent_node.children, []) # type: ignore
        self.assertIsNone(self.default_parent_node.props)

    def test_standard_properties(self):
        self.standard_parent_node.children.append(self.paragraph_parent_node) # type: ignore
        self.standard_parent_node.props = self.props

        self.assertEqual(self.standard_parent_node.tag, "div")
        self.assertListEqual(self.standard_parent_node.children, [self.paragraph_parent_node]) # type: ignore
        self.assertIn("class", self.standard_parent_node.props)

    def test_nested_parent_nodes(self):
        self.anchor_leaf_node.props = self.props
        self.paragraph_parent_node.props = self.props
        self.standard_parent_node.props = self.props
        self.paragraph_parent_node.children.append(self.anchor_leaf_node) # type: ignore
        self.standard_parent_node.children.append(self.paragraph_parent_node) # type: ignore

        self.assertEqual(
            self.standard_parent_node.to_html(),
            "<div class=\"a-class\"><p class=\"a-class\"><a class=\"a-class\">Anchor</a></p></div>"
        )

    def test_nested_leaf_nodes(self):
        self.normal_text.props = self.props
        self.bold_text.props = self.props
        self.italic_text.props = self.props
        self.paragraph_parent_node.props = self.props
        self.paragraph_parent_node.children.extend([self.normal_text, self.bold_text, self.italic_text]) # type: ignore

        self.assertEqual(
            self.paragraph_parent_node.to_html(),
            "<p class=\"a-class\"><span class=\"a-class\">Normal</span><b class=\"a-class\">Bold</b><i class=\"a-class\">Italic</i></p>"
        )

    def test_nested_parent_and_nested_leaf_nodes(self):
        paragraph_1 = ParentNode("p", [])
        paragraph_2 = ParentNode("p", [])

        paragraph_1.children.extend([self.bold_text, self.italic_text]) # type: ignore
        paragraph_2.children.append(self.anchor_leaf_node) # type: ignore

        self.standard_parent_node.children.extend([paragraph_1, paragraph_2]) # type: ignore

        self.assertEqual(
            self.standard_parent_node.to_html(),
            "<div><p><b>Bold</b><i>Italic</i></p><p><a>Anchor</a></p></div>"
        )

    def test_representation(self):
        self.assertEqual(repr(self.standard_parent_node), "ParentNode(div, [], None)")

if __name__ == "__main__":
    unittest.main()
