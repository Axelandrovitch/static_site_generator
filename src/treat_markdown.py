import re
from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, split_nodes_delimiter, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_image, text_type_link, text_node_to_html_node

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
   
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = [block.strip() for block in blocks]
    filtered_blocks = list(filter(lambda x: x != "", stripped_blocks))
    return filtered_blocks

def find_first_char(string):
   first_char = 0
   while string[first_char] == "\n":
      first_char +=1
   return string[first_char]
   

def count_consecutive(text, order = "normal"):
   if order == "normal":
      count = 0
      while text[count] == text[count+1]:
        count +=1
      return count+1
   if order == "reversed":
      count = -1
      while text[count] == text[count-1]:
         count -=1
      return abs(count)

def check_line_start(text, char, space_needed=False):
   split_text = text.split("\n")
   filtered = list(filter(lambda x: x!="", split_text))

   for subtext in filtered:
      second_char = subtext[1] if len(subtext) > 1 else None
      if space_needed is True:
         if subtext[0] != char or second_char != " ":
            return False
      elif subtext[0] != char and space_needed is False:
         return False
   return True

def check_ol(text):
   split_text = text.split("\n")
   filtered = list(filter(lambda x: x!="", split_text))
   starting_lines = []
   for subtext in filtered:
      first_char = subtext[0]
      second_char = subtext[1] if len(subtext) >= 2 else None
      third_char = subtext[2] if len(subtext) >= 3 else None
      starting_lines.append([first_char, second_char, third_char])
   for i, line in enumerate(starting_lines):
      if line[0] == str(i+1) and line[1] == "." and line[2] == " ":
         continue
      else:
         return False
   return True




def block_to_block_type(block):
   block_type_heading = "heading"
   block_type_paragraph = "paragraph"
   block_type_code = "code"
   block_type_quote = "quote"
   block_type_ul = "unordered_list"
   block_type_ol = "ordered_list"
   first_char = find_first_char(block)
   if first_char == "#" and count_consecutive(text=block) < 7 and block[count_consecutive(text=block)] == " ":
      return block_type_heading
   elif first_char == "`" and count_consecutive(text=block) == 3 and count_consecutive(text=block, order="reversed") == 3 and block[-1] == "`":
      return block_type_code
   elif first_char == ">" and check_line_start(block, char=">"):
      return block_type_quote
   elif (first_char == "*" or first_char == "-") and check_line_start(text=block, char = first_char, space_needed=True):
      return block_type_ul
   elif first_char == "1" and check_ol(block):
      return block_type_ol
   else:
      return block_type_paragraph


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    content = block.strip()

    if block_type.startswith("heading"):
        return heading_to_html(content)
    elif block_type == "paragraph":
        paragraph_node = HTMLNode("p")
        text_nodes = text_to_text_nodes(content)
        html_children = [text_node_to_html_node(node) for node in text_nodes]
        paragraph_node.children = html_children
        return paragraph_node
    elif block_type == "unordered_list":
        list_items = content.split("\n")
        list_node = HTMLNode("ul")
        list_node.children = [HTMLNode("li", value=item[2:].strip()) for item in list_items]
        return list_node
    elif block_type == "ordered_list":
        list_items = content.split("\n")
        list_node = HTMLNode("ol")
        list_node.children = [HTMLNode("li", value=item.split('.', 1)[1].strip()) for item in list_items]
        return list_node
    elif block_type == "code":
        code_content = "\n".join(block.split("\n")[1:-1])
        return HTMLNode("pre", children=[HTMLNode("code", value=code_content)])
    elif block_type == "quote":
        quote_content = "\n".join(line[1:].strip() for line in content.split("\n"))
        return HTMLNode("blockquote", value=quote_content)


def heading_to_html(heading):
   n = 1
   while heading[n-1] == "#":
      n +=1
    
   final_heading = heading[n:].strip()
   return HTMLNode(f"h{n-1}", value=final_heading)


def markdown_to_html_node(markdown):
    # Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    
    # Convert each block into an HTMLNode
    html_nodes = [block_to_html_node(block) for block in blocks]
    
    # Create the top-level <div> node
    div_node = HTMLNode("div", children=html_nodes)
    
    return div_node


def extract_title(markdown):
   blocks = markdown_to_blocks(markdown=markdown)
   h1_count = 0
   h1_to_rtrn = None
   for block in blocks:
      html_node = block_to_html_node(block=block)
      if html_node.tag == "h1":
         h1_to_rtrn = html_node
         h1_count +=1
   if h1_count == 1:
      return h1_to_rtrn.text
   else:
      raise Exception("Must have one and only one h1")
      