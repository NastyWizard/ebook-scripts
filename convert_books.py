import re
import os.path
import os
import subprocess
from termcolor import colored
import json

with open('settings.json', 'r') as f:
    variables = json.load(f)

convert = f"\"{variables['CALIBRE_DIR']}/ebook-convert.exe\""
output_dir = variables['CONVERT_OUTDIR']

def get_all_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

files = get_all_files(".")
files = list(filter(lambda f : (re.search(".*(epub)$", f)), files))

for f in files:
    try:
        f_basename = os.path.basename(f)
        f_basename = f_basename.rsplit( ".", 1 )[ 0 ]
        output_file = f"{output_dir}/{f_basename}.mobi"
        if os.path.exists(output_file) == False:
            print(colored(f"{convert} {f} {output_file}", 'green'))
            print(f"{convert} {f} {output_file}")
            subprocess.Popen(f"{convert} \"{f}\" \"{output_file}\"", shell=True)
        else:
            print(colored(f"{f_basename} already converted, skipping..", 'red'))
    except:
        print(f"Failed to convert {f}")
