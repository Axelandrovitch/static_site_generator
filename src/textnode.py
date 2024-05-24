text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


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
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


# text_node_1 = TextNode(text="Hello World", text_type="text")
# text_node_2 = TextNode(text="**this is why** *I never go* to this place !", text_type="text")
# text_node_3 = TextNode(text="it is such an idiotic thing *to do*", text_type="text")
# text_node_4 = TextNode(text="Whatever", text_type="text")
# text_node_5 = TextNode(text="I am going **home** to write some `code text`", text_type="text")

# test = split_nodes_delimiter([text_node_1, text_node_2, text_node_3, text_node_4, text_node_5], "*", "italic")
# for node in test:
#     print(node)