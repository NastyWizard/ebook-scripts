import re
import os.path
import os
import subprocess
import shutil
from termcolor import colored


kindle_path = "H:\documents"
output_dir = "./backup"

def get_all_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

files = get_all_files(kindle_path)
files = list(filter(lambda f : (re.search(".*(mobi)$", f)), files))

for f in files:
    try:
        f_basename = os.path.basename(f)
        f_basename = f_basename.rsplit( ".", 1 )[ 0 ]
        output_file = f"{output_dir}/{f_basename}.mobi"
        if os.path.exists(output_file) == False:
            print(colored(f"copying: {f} -> {output_file}", 'green'))
            shutil.copyfile(f, output_file)
        else:
            print(colored(f"{f_basename} already copied, skipping..", 'red'))
    except:
        print(f"Failed to convert {f}")
