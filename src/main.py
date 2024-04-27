from textnode import TextNode

def main():
    test_node = TextNode('This is some text node test', 'italic', 'https://boot.dev')

    print(test_node.__repr__())
main()
