import os
from copystatic import copy_directory_contents
from generatepage import generate_page


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():

  copy_directory_contents(src="static", dst="public")
  generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


main()
