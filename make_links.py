import os
import re

source_root = '/home/user/'
destination_root = '/tmp/tools_links'

for item_name in os.listdir(source_root):
    match = re.match(r'([a-zA-Z0-9][a-zA-Z0-9.\-]*)$', item_name)
    if match:
        source_folder = os.path.join(source_root, item_name)
        destination_folder = os.path.join(destination_root, item_name)
        if os.path.isdir(source_folder):
            os.symlink(source_folder, destination_folder)
