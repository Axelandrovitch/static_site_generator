import unittest
from textnode import TextNode, split_nodes_delimeter



class TestTextNode(unittest.TestCase):
    
    def setUp(self):
        # Full node arbitrary sample
        self.full_node = TextNode("This is a text node", "bold", "https://boot.dev")

        self.full_node_different_url = TextNode("This is a text node", "bold", "https://not-the-same.dev")
        self.text_and_type_text_node = TextNode("This is a text node", "bold")
        self.text_and_type_text_node_duplicate = TextNode("This is a text node", "bold")

        self.same_text_and_different_type_text_node =  TextNode("This is a text node", "italic")

        self.only_text_node = TextNode("This is a text node")
        self.only_text_different_node = TextNode("This is another text node")

        # Note that the default node differs from the full test node
        self.same_text_default_node= TextNode("This is a text node", "text", None)

        


    def test_eq(self):
        full_node_duplicate = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(self.full_node, full_node_duplicate)
    def test_not_same_instance(self):
        class OtherClass:
            def __init__(self, other):
                self.other = other
        
        other_class_instance = OtherClass("other")
        self.assertFalse(self.full_node == other_class_instance) 
    def test_text_type_default(self):
        self.assertEqual(self.only_text_node, self.same_text_default_node)
    
    def test_inequality_due_to_different_text(self):
        self.assertNotEqual(self.only_text_node, self.only_text_different_node)
    
    def test_inequality_due_to_different_text_type(self):
        self.assertNotEqual(self.text_and_type_text_node, self.same_text_and_different_type_text_node)
    def test_inequality_due_to_different_url(self):
        node_empty_url = TextNode("This is a text node", "bold", "")
        self.assertNotEqual(self.full_node, self.full_node_different_url)
        self.assertNotEqual(self.full_node, node_empty_url)


class ConversionFunctions(unittest.TestCase):

  def test_split_nodes_delimeter(self):
    text_node_text = TextNode(text="Hello World")
    text_node_bold= TextNode(text="**bold text** not bold")
    text_node_italic = TextNode(text="not italic*italic text*")
    text_node_code = TextNode(text="some other stuff `code text` not code")


    text_node_1 = TextNode(text="Hello World", text_type="text")
    text_node_2 = TextNode(text="**bold text** not bold", text_type="text")
    text_node_3 = TextNode(text="not italic", text_type="text")
    text_node_4 = TextNode(text="italic text", text_type="italic")
    text_node_5 = TextNode(text="some other stuff `code text` not code", text_type="text")
    expected_italic = [text_node_1, text_node_2, text_node_3, text_node_4, text_node_5]

    test1 = split_nodes_delimeter([text_node_text, text_node_bold, text_node_italic, text_node_code], "*", "italic")
    self.assertEqual(test1, expected_italic)