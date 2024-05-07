import random
import string
class TextNode:
    def __init__(self, text, text_type = "text", url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)

    def __repr__(self):
        return f"{self.text}, {self.text_type}, {self.url}"
    


def split_nodes_delimeter(old_nodes, delimeter, text_type):
    all_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError(f"Node: {node} is not a TextNode")
        splitted_node = manage_delimeter(delimeter, node.text)
        converted_node = []
        for i in range(0, len(splitted_node)):
            raw_text = splitted_node[i]
            if i % 2 != 0:
                converted_node.append(TextNode(text=raw_text, text_type=text_type))
            elif raw_text != "":
                converted_node.append(TextNode(text=raw_text, text_type="text"))
        all_nodes.extend(converted_node)
    return all_nodes
  


def manage_delimeter(delimeter, text):
  if delimeter == "*" and "**" in text:
      random_tag = "_"
      while random_tag in text:
          random_tag = generate_random_tag()
      text = text.replace("**", random_tag)
      splitted_text = text.split(delimeter)
      splitted_text = [i.replace(random_tag, "**") if random_tag in i else i for i in splitted_text]
      return splitted_text
  else:
      return text.split(delimeter) 

def generate_random_tag():
  return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))

  def append_node(splited_node, converted_node, text_type):
    for i in range(0, len(splited_node)):
        raw_text = splited_node[i]
        if i % 2 != 0:
            converted_node.append(TextNode(text=raw_text, text_type=text_type))
        elif raw_text != "":
            converted_node.append(TextNode(text=raw_text, text_type="text"))
    return converted_node

                


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
print(test1)