from textnode import TextNode
from copystatic import copy_directory_contents

def main():

  copy_directory_contents(src="static", dst="public")

main()
