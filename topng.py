#!/usr/bin/env python
# coding: utf-8
# if you don't have pillow_avif, you might need to "pip install pillow-avif-plugin"

from PIL import Image
from tqdm import tqdm
import pillow_avif
import os

print("""
   ______                           __     __           ____  _   ________
  / ____/___  ____ _   _____  _____/ /_   / /_____     / __ \/ | / / ____/
 / /   / __ \/ __ \ | / / _ \/ ___/ __/  / __/ __ \   / /_/ /  |/ / / __  
/ /___/ /_/ / / / / |/ /  __/ /  / /_   / /_/ /_/ /  / ____/ /|  / /_/ /  
\____/\____/_/ /_/|___/\___/_/   \__/   \__/\____/  /_/   /_/ |_/\____/   
""")

folder = input("Enter the folder you want to work on:\n\t>>")
todo = [x for x in os.listdir(folder) if x.endswith(".webp")]
print(f"\n>> Found {len(todo):,} files to work on\n\n")

for imagefile in tqdm(todo):
    basename = imagefile[:-5]
    extension = imagefile[-5:]

    im = Image.open(os.path.join(folder, imagefile)).convert("RGB")
    im.save(fr"{folder}\{basename}.png")


print("Done")
input(">> Press any button to close...")

