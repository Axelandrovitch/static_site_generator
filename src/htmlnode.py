class HTMLNode:
  def __init__(self, tag = None, value = None, children = None, props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    if self.props is None:
      return ""
    else:
      props_to_concatenate = []
      for key, value in self.props.items():
        props_to_concatenate.append(f'{key}="{value}"')
      return " ".join(props_to_concatenate)


  def __repr__(self):
    props_str = ""
    if self.props is not None:
      props_str = self.props_to_html()
    def check_props(props):
      if len(props) > 0 and type(props) == str:
        return f" props = {props},"
      return ""
    children_reprs = [repr(child) for child in self.children] if self.children else "no children"
    return f"tag = {self.tag}, value = {self.value},{check_props(props_str)} children = {children_reprs}"



class LeafNode(HTMLNode):
  def __init__(self, tag, value, props = None):
    super().__init__(tag, value, None, props)
  
  def to_html(self):
    if self.value is None or self.value =="":
      raise ValueError("This node must have a value")
    elif self.tag is None:
      return str(self.value)
    else:
      props_str =" " + self.props_to_html() if self.props_to_html() != "" else ""
      return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"