import random
import string


class TextNode:
    def __init__(self, text, text_type="text", url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"{self.text}, {self.text_type}, {self.url}"


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    all_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError(f"Node: {node} is not a TextNode")
        split_node = manage_delimiter(delimiter, node.text)
        converted_node = []
        for i in range(0, len(split_node)):
            raw_text = split_node[i]
            if i % 2 != 0:
                converted_node.append(TextNode(text=raw_text, text_type=text_type))
            elif raw_text != "":
                converted_node.append(TextNode(text=raw_text, text_type="text"))
        all_nodes.extend(converted_node)
    return all_nodes


def manage_delimiter(delimiter, text):
    if text.count(delimiter) % 2 != 0:
        raise ValueError("Opened delimiters must be closed")
    elif delimiter == "*" and "**" in text:
        nodes = []
        italic = False
        current_text = ""
        asterisk_occurrence = 0
        for i in range(len(text)):
            next_i = text[i + 1] if i < len(text) - 1 else None

            if text[i] == "*":
                asterisk_occurrence += 1

                if asterisk_occurrence == 1 and next_i != "*":
                    italic = not italic
                    if italic and current_text:
                        nodes.append(TextNode(text=current_text, text_type="text"))
                        current_text = ""
                    elif not italic and current_text:
                        nodes.append(TextNode(text=current_text, text_type="italic"))
                        current_text = ""

                if asterisk_occurrence == 2:
                    current_text += "**"
                    asterisk_occurrence = 0

            else:
                current_text += text[i]
                asterisk_occurrence = 0

            if i == len(text) - 1 and current_text:
                if italic:
                    nodes.append(TextNode(text=current_text, text_type="italic"))
                else:
                    nodes.append(TextNode(text=current_text, text_type="text"))

        return nodes
    else:
        return text.split(delimiter)


def generate_random_tag():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))


text_node_text = TextNode(text="*Hello**World**this is a test*")
text_node_bold = TextNode(text="bold t*ext not* bold")
text_node_italic = TextNode(text="not *italic* italic* text*")
text_node_code = TextNode(text="some other stuff `code text not code")

text_node_1 = TextNode(text="Hello World", text_type="text")
text_node_2 = TextNode(text="bold text not bold", text_type="text")
text_node_3 = TextNode(text="not italic", text_type="text")
text_node_4 = TextNode(text="italic text", text_type="italic")
text_node_5 = TextNode(text="some other stuff `code text` not code", text_type="text")
expected_italic = [text_node_1, text_node_2, text_node_3, text_node_4, text_node_5]

test1 = split_nodes_delimiter([text_node_text, text_node_bold, text_node_italic, text_node_code], "*", "italic")
print(test1)
