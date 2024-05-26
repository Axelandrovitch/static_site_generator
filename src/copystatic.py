import os
import shutil

def copy_directory_contents(src, dst):

    os.makedirs(dst, exist_ok=True)
    
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)
        
        if os.path.isdir(src_item):
            copy_directory_contents(src_item, dst_item)
        else:
            shutil.copy2(src_item, dst_item)