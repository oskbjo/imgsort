import os
import argparse
import re
import shutil
from datetime import datetime


def CreateDirs(local_path, mod_date, raw_ext="", desc=""):
    local_img_dir = ""
    local_raw_img_dir = ""
    if raw_ext != "":
        temp = ["", " " + raw_ext]

    for i in temp:
        path = "~/" + local_path + i + "/" + mod_date + " " + desc
        full_path = os.path.expanduser(path)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"Directory {full_path} successfully created")
        else:
            print(f"Directory {full_path} already exists")
        if i == "":
            local_img_dir = full_path
        else:
            local_raw_img_dir = full_path
    return local_img_dir, local_raw_img_dir

def ExtractDate(file_path):
    mod_time = os.path.getmtime(file_path)
    mod_dt = datetime.fromtimestamp(mod_time)
    mod_date = mod_dt.strftime("%Y") + "-" + mod_dt.strftime("%m") +\
        "-" + mod_dt.strftime("%d")
    return mod_date

def MoveFiles(img_files_dir, local_img_dir, local_raw_img_dir, img_files):
    jpg_files = [f for f in img_files if re.search(r'\.jpg$', f, re.IGNORECASE)]
    raw_files = [f for f in img_files if re.search(r'\.orf$', f, re.IGNORECASE)]
    for i in range(len(jpg_files)):
        shutil.move(img_files_dir + jpg_files[i], local_img_dir)
        shutil.move(img_files_dir + raw_files[i], local_raw_img_dir)

def main():
    parser = argparse.ArgumentParser(
        description=""
    )
    parser.add_argument(
        "--img_files_dir",
        type=str,
        help="Directory of jpg files, and raw files",
    )
    parser.add_argument(
        "--local_photos_path",
        type=str,
        default="Pictures/Photographs",
        help="Path to local photos dir from home dir"
    )
    parser.add_argument(
        "--raw_dir_ext",
        type=str,
        default="",
        help="Optional extension for separate raw photos dir"
    )
    parser.add_argument(
        "--dir_description",
        type=str,
        default="",
        help="Description of photos dir to be part of dir name"
    )
    args = parser.parse_args()
    
    img_files_dir = args.img_files_dir + "/"
    img_files = os.listdir(img_files_dir)

    mod_dates = set()
    mod_dict = {}
    for img_file in img_files:
        mod_date = ExtractDate(img_files_dir + img_file)[2:]
        mod_dates.add(mod_date)
        if mod_date not in mod_dict.keys():
            mod_dict.update({mod_date: []})
        mod_dict.get(mod_date).append(img_file)

    for mod_date in mod_dates:
        local_img_dir, local_raw_img_dir = CreateDirs(
            args.local_photos_path,
            mod_date,
            args.raw_dir_ext,
            args.dir_description)
        MoveFiles(
            img_files_dir,
            local_img_dir,
            local_raw_img_dir,
            mod_dict.get(mod_date))

if __name__=="__main__":
    main()