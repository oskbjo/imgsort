#!/bin/bash

# Default values
verbose_mode=false
dir_name=""
home_folder="/home/$USER/"
local_photos_path="Pictures/Photographs"
raw_dir_ext="RAW"

usage() {
  echo "Usage $0 [OPTIONS]"
  echo "Options:"
  echo " -h     Display this message"
  echo " -v     Run program in secondary-sort mode"
  echo " -d     Name of directory"
}

while getopts "hvd:" flag; do
  case $flag in
    h) # Handle the h flag
      usage
      exit 0
    ;;
    v) # Handle the v flag
      verbose_mode=true
    ;;
    d) # Handle the d flag
      dir_name=$OPTARG
    ;;
    \?) # Handle invalide value
      echo "Invalid format"
      exit 1
    ;;
  esac
done

# Normal mode. Move files from media to internal storage
if [ $verbose_mode == false ]; then
  drive=$(ls /media/$USER)
  img_files_dir="/media/$USER/$drive/DCIM/100OLYMP"

  for f in $img_files_dir/*.ORF; do
    [ -f "${f%.ORF}.JPG" ] || [ -f "${f%.ORF}.jpg" ] || rm "$f"
  done

  python3 imgsort.py --img_files_dir "$img_files_dir" --local_photos_path\
   $local_photos_path --raw_dir_ext $raw_dir_ext --dir_description $dir_name
  echo "All files moved successfully"

# Verbose mode. Filter RAW files
else
  photos_dir_path=$home_folder$local_photos_path/$dir_name
  raw_dir_path="$home_folder${local_photos_path} $raw_dir_ext"/$dir_name
  
  for f in "$raw_dir_path"/*.ORF; do
    filename=$(basename "$f")
    filename="${filename%.*}"
    file_path="$photos_dir_path/$filename"

    if [ ! -f "$file_path.JPG" ] && [ ! -f "$file_path.jpg" ]; then
      rm "$f"
    fi
  done
  echo "Filtering of files complete"
fi