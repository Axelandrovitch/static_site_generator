import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

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

#Test HTMLNode
  def test_to_html(self):
    self.expected_complete_html_node = f'href="https://www.boot.dev" target="bootdev website"'
    self.assertEqual(self.complete_html_node.props_to_html(), self.expected_complete_html_node)

  def test_repr(self):
    self.expected_repr = "tag = div, value = Hello, props = class=\"greeting\", children = ['tag = a, value = Hello World, children = no children']"
    self.assertEqual(self.node1.__repr__(), self.expected_repr)


# Test LeafNode
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

#Test ParentNode
  def test_parent_to_html(self):
     node = ParentNode(tag="p",children=[LeafNode(tag="b", value="Bold text"), LeafNode(tag=None, value="Normal text"), LeafNode(tag="i", value="italic text"), LeafNode(tag=None, value="Normal text")])
     expected_result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
     self.assertEqual(node.to_html(), expected_result)
  
  def test_parent_to_html_no_children(self):
    with self.assertRaises(ValueError) as context:
      node = ParentNode(tag="p",children=[])
      node.to_html()
    self.assertEqual(str(context.exception), "A parent node must have at least one child")
  
  def test_parent_to_html_no_tag(self):
    with self.assertRaises(ValueError) as context:
      node = ParentNode(tag="", children=[LeafNode(tag="b", value="Bold text"), LeafNode(tag=None, value="Normal text"), LeafNode(tag="i", value="italic text"), LeafNode(tag=None, value="Normal text")])
      node.to_html()
    self.assertEqual(str(context.exception), "A tag must be provided for a parent node")
  
  def test_parent_to_html_incorrect_children(self):
    with self.assertRaises(TypeError) as context:
     node = ParentNode(tag="p",children=[LeafNode(tag="b", value="Bold text"), 3])
     node.to_html()
    self.assertEqual(str(context.exception), "The children must be of type LeafNode or ParentNode")

# Test conversion from TextNode to HTMLNode
  def test_node_to_html_node(self):
    text_node_text = TextNode(text="Hello World")
    text_node_bold= TextNode(text="bold text", text_type="bold")
    text_node_italic = TextNode(text="italic text", text_type="italic")
    text_node_code = TextNode(text="code text", text_type="code")
    text_node_link = TextNode(text="anchor text", text_type="link", url="https://www.boot.dev")
    text_node_image = TextNode(text="some image", text_type="image", url="img_src")
    empty_html_node = HTMLNode()
    expected_result_text = LeafNode(tag=None, value="Hello World")
    expected_result_bold = LeafNode(tag="b", value="bold text")
    expected_result_italic = LeafNode(tag="i", value="italic text")
    expected_result_code = LeafNode(tag="code", value="code text")
    expected_result_link = LeafNode(tag="a", value="anchor text", props={"href": "https://www.boot.dev"})
    expected_result_image = LeafNode(tag="img", value="", props={"src": "img_src", "alt": "some image"})
    
    self.assertEqual(empty_html_node.text_node_to_html_node(text_node_text), expected_result_text)
    self.assertEqual(empty_html_node.text_node_to_html_node(text_node_bold), expected_result_bold)
    self.assertEqual(empty_html_node.text_node_to_html_node(text_node_italic), expected_result_italic)
    self.assertEqual(empty_html_node.text_node_to_html_node(text_node_code), expected_result_code)
    self.assertEqual(empty_html_node.text_node_to_html_node(text_node_link), expected_result_link)
    self.assertEqual(empty_html_node.text_node_to_html_node(text_node_image), expected_result_image)


if __name__ == "__main__":
    unittest.main()