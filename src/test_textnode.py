import unittest

from textnode import TextNode


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



if __name__ == "__main__":
    unittest.main()
