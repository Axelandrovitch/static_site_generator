class HTMLNode:
  def __init__(self, tag = None, value = None, children = None, props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
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