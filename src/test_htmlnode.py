import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

  def setUp(self):
    self.default_html_node = HTMLNode()
    self.complete_html_node = HTMLNode("a", "Hello World", ["children1", "children2"], {"href": "https://www.boot.dev", "target": "bootdev website"})
    self.node1 = HTMLNode(tag='div', value='Hello', children=[HTMLNode(tag='a', value='Hello World')], props={'class': 'greeting'})
    self.node2 = HTMLNode(tag='p', value='This is a paragraph.')
    self.node3 = HTMLNode(tag='input', props={'type': 'text', 'value': 'Enter text here'})
    self.node4 = HTMLNode(tag='a', value='Click me', props={'href': 'http://example.com'})


  def test_to_html(self):
    self.expected_complete_html_node = f'href="https://www.boot.dev" target="bootdev website"'
    self.assertEqual(self.complete_html_node.props_to_html(), self.expected_complete_html_node)

  def test_repr(self):
    self.expected_repr = "tag = div, value = Hello, props = class=\"greeting\", children = ['tag = a, value = Hello World, children = no children']"
    self.assertEqual(self.node1.__repr__(), self.expected_repr)



if __name__ == "__main__":
    unittest.main()