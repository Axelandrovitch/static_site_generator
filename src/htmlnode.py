class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        # Start with the opening tag
        if self.tag:
            tag_open = f"<{self.tag}"
            for prop, value in self.props.items():
                tag_open += f' {prop}="{value}"'
            tag_open += ">"
        else:
            tag_open = ""

        # Add the content inside the tag (value and children)
        content = self.value if self.value else ""
        for child in self.children:
            content += child.to_html()

        # Closing tag
        tag_close = f"</{self.tag}>" if self.tag else ""

        return tag_open + content + tag_close


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
            if len(props) > 0 and isinstance(props, str):
                return f" props = {props},"
            return ""

        children_reprs = [repr(child) for child in self.children] if self.children else "no children"
        return f"tag = {self.tag}, value = {self.value},{check_props(props_str)} children = {children_reprs}"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return NotImplemented
        return self.tag == other.tag and self.value == other.value and self.props == other.props

    def to_html(self):
        if self.value is None:
            raise ValueError("This node must have a value")
        elif self.tag is None:
            return str(self.value)
        else:
            props_str = " " + self.props_to_html() if self.props_to_html() != "" else ""
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("A tag must be provided for a parent node")
        if self.children is None or len(self.children) == 0:
            raise ValueError("A parent node must have at least one child")
        for children in self.children:
            if not isinstance(children, ParentNode) and not isinstance(children, LeafNode):
                raise TypeError("The children must be of type LeafNode or ParentNode")
        else:
            concat_children = "".join([child.to_html() for child in self.children])
            return f"<{self.tag}>{concat_children}</{self.tag}>"
