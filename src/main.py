from textnode import TextNode
import os
import shutil
from copystatic import copy_directory_contents
from generatepage import generate_page




dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    copy_directory_contents(src=dir_path_static, dst=dir_path_public)
    
    generate_page(
        from_path=os.path.join(dir_path_content, "index.md"),
        template_path=template_path,
        dest_path=os.path.join(dir_path_public, "index.html")
    )
    
    print(f"Copied static contents from {dir_path_static} to {dir_path_public}")
    print(f"Generated page from {os.path.join(dir_path_content, 'index.md')} using template {template_path} to {os.path.join(dir_path_public, 'index.html')}")


main()
