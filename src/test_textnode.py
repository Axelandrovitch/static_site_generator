import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    
    def setUp(self):
        self.full_node = TextNode("This is a text node", "bold", "https://boot.dev")
        self.full_node_duplicate = TextNode("This is a text node", "bold", "https://boot.dev")
        self.same_text_default_type_text_default_url = TextNode("This is a text node", "text", None)
        self.same_text_default_type_no_url = TextNode("This is a text node", "text")
        self.full_node_different_url = TextNode("This is a text node", "bold", "https://not-the-same.dev")
        self.text_and_type_text_node = TextNode("This is a text node", "bold")
        self.text_and_type_text_node_duplicate = TextNode("This is a text node", "bold")
        self.different_text_and_same_type_text_node =  TextNode("This is another a text node", "bold")
        self.same_text_and_different_type_text_node =  TextNode("This is a text node", "italic")
        self.only_text_node = TextNode("This is a text node")
        self.only_text_different_node = TextNode("This is another text node")


    def test_eq(self):
        self.assertEqual(self.full_node, self.full_node_duplicate)
    
    def test_text_type_default(self):
        self.assertEqual(self.only_text_node, self.same_text_default_type_no_url)
    
    def test_inequality_due_to_different_text(self):
        self.assertNotEqual(self.only_text_node, self.only_text_different_node)
    
    def test_inequality_due_to_different_text_type(self):
        self.assertNotEqual(self.text_and_type_text_node, self.same_text_and_different_type_text_node)
    def test_inequality_due_to_different_url(self):
        self.assertNotEqual(self.full_node, self.full_node_different_url)



if __name__ == "__main__":
    unittest.main()
