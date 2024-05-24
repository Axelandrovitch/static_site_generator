import re
import textnode
from textnode import TextNode, split_nodes_delimiter, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_image, text_type_link

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

# text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
# print(extract_markdown_images(text))

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

# text2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
# print(extract_markdown_links(text2))


def split_node_image(old_nodes):
    nodes = []
    for node in old_nodes:
        original_text = node.text
        extracted_images = extract_markdown_images(original_text)
        if not extracted_images:  # If no images found, add the original node back
          nodes.append(node)
          continue
        for image in extracted_images:
          image_label = image[0]
          image_url = image[1]
          split_text = original_text.split(f"![{image_label}]({image_url})", 1)
          if split_text[0]:
            nodes.append(TextNode(text_type=text_type_text, text=split_text[0]))
          nodes.append(TextNode(text_type=text_type_image, text=image_label, url=image_url))
          if len(split_text)>1:
             original_text = split_text[1]
          else: original_text = ""
    if original_text:
        nodes.append(TextNode(text=original_text, text_type=text_type_text))
    return nodes

def split_node_link(old_nodes):
    nodes = []
    for node in old_nodes:
        original_text = node.text
        extracted_links = extract_markdown_links(original_text)
        if not extracted_links:  
          nodes.append(node)
          continue
        for link in extracted_links:
          link_label = link[0]
          link_url = link[1]
          split_text = original_text.split(f"[{link_label}]({link_url})", 1)
          if split_text[0]:
            nodes.append(TextNode(text_type=text_type_text, text=split_text[0]))
          nodes.append(TextNode(text_type=text_type_link, text=link_label, url=link_url))
          if len(split_text)>1:
             original_text = split_text[1]
          else: original_text = ""
          
    if original_text:
       nodes.append(TextNode(text=original_text, text_type="text"))
    return nodes

def text_to_text_nodes(text):
   node = TextNode(text=text, text_type=text_type_text)
   processed_nodes = split_nodes_delimiter([node], delimiter="**", text_type=text_type_bold)
   processed_nodes = split_nodes_delimiter(processed_nodes, delimiter="*", text_type=text_type_italic)
   processed_nodes = split_nodes_delimiter(processed_nodes, delimiter="`", text_type=text_type_code)
   processed_nodes = split_node_image(processed_nodes)
   processed_nodes = split_node_link(processed_nodes)
   return processed_nodes
   
   

# node = TextNode(
#     "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     "text",
# )

# new_nodes = split_node_image([node])

# print(new_nodes)


# node2 = TextNode(
#     "This is text with an ![image1](https://example.com/image1.png) and another ![image2](https://example.com/image2.png) here.",
#     text_type="text"
# )
# new_nodes2 = split_node_image([node2])
# # print(new_nodes2)

# node_links = TextNode(
#     "Here is a [link1](https://example.com/link1) and here is another [link2](https://example.com/link2) and some more text.",
#     text_type="text"
# )
# new_nodes_link = split_node_link([node])

# print(new_nodes_link)


test_text_to_nodes = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

final = text_to_text_nodes(test_text_to_nodes)

for node in final:
   print(node)