from textnode import TextNode
import os
import shutil
from copystatic import copy_directory_contents, copy_files_recursive
from generatepage import generate_page, generate_pages_recursive




dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    copy_files_recursive(source_dir_path=dir_path_static, dest_dir_path=dir_path_public)
    
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    
    print(f"Copied static contents from {dir_path_static} to {dir_path_public}")
    print(f"Generated page from {os.path.join(dir_path_content, 'index.md')} using template {template_path} to {os.path.join(dir_path_public, 'index.html')}")


main()
