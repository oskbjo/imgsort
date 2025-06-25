#!/bin/bash

drive=$(ls /media/$USER)
img_files_dir="/media/$USER/$drive/DCIM/100OLYMP"
local_photos_path="Pictures/Photographs"
raw_dir_ext="RAW"

for f in $img_files_dir/*.ORF; do
  [ -f "${f%.ORF}.JPG" ] || [ -f "${f%.ORF}.jpg" ] || rm "$f"
done

python3 imgsort.py --img_files_dir "$img_files_dir" --local_photos_path $local_photos_path --raw_dir_ext $raw_dir_ext --dir_description $1