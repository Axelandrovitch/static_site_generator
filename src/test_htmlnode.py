import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):

  def setUp(self):
    self.default_html_node = HTMLNode()
    self.complete_html_node = HTMLNode("a", "Hello World", ["children1", "children2"], {"href": "https://www.boot.dev", "target": "bootdev website"})
    self.node1 = HTMLNode(tag='div', value='Hello', children=[HTMLNode(tag='a', value='Hello World')], props={'class': 'greeting'})
    self.node2 = HTMLNode(tag='p', value='This is a paragraph.')
    self.node3 = HTMLNode(tag='input', props={'type': 'text', 'value': 'Enter text here'})
    self.node4 = HTMLNode(tag='a', value='Click me', props={'href': 'http://example.com'})

    self.leaf_node = LeafNode("p", "This is a paragraph of text.")
    self.leaf_node_with_props = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})


  def test_to_html(self):
    self.expected_complete_html_node = f'href="https://www.boot.dev" target="bootdev website"'
    self.assertEqual(self.complete_html_node.props_to_html(), self.expected_complete_html_node)

  def test_repr(self):
    self.expected_repr = "tag = div, value = Hello, props = class=\"greeting\", children = ['tag = a, value = Hello World, children = no children']"
    self.assertEqual(self.node1.__repr__(), self.expected_repr)

  def test_leaf_to_html(self):
    expected_result1 = "<p>This is a paragraph of text.</p>"
    expected_result2 = '<a href="https://www.google.com">Click me!</a>'
    self.assertEqual(self.leaf_node.to_html(), expected_result1)
    self.assertEqual(self.leaf_node_with_props.to_html(), expected_result2)

  def test_leaf_to_html_no_value(self):
    with self.assertRaises(ValueError) as context:
        leaf = LeafNode(tag="div", value="")
        leaf.to_html()
    self.assertEqual(str(context.exception), "This node must have a value")

if __name__ == "__main__":
    unittest.main()