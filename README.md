# README.md

### Table of Contents
- [imgsort](#imgsort)
- [Quick Install](#quick-install)
- [Usage](#usage)

# imgsort
Sort JPG and RAW images to directories
Assumes that images are stored on media device (USB stick), and that no other media is attached
JPGs stored in `/home/$USER/Pictures/Photographs`
RAWs stored in `/home/$USER/Pictures/Photographs RAW`
Runs using bash, and Python 3.12

# Quick Install
```sh
# Clone repo with
git clone git@github.com:oskbjo/imgsort.git

# Allow access to shell script
cd imgsort
# chmod u+x imgsort.sh # For execution, no write
chmod u+w imgsort.sh # For execution, and write
```

# Usage
```
# NORMAL MODE
cd ~/imgsort
./imgsort.sh "DIRECTORY_DESCRIPTION"

# FILTER MODE
./imgsort.sh -v -d "DIRECTORY_NAME"
```

I might update this if I feel the need. Please use as you see fit
