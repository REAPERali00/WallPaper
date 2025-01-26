import os
import random
import subprocess
import sys


def list_images(dir):
    return [
        os.path.join(dir, file)
        for file in os.listdir(dir)
        if file.endswith((".jpg", ".jpeg", ".png"))
    ]


def set_wallpaper(image_path):
    command = f"swaybg -i {image_path} -m fill &"
    subprocess.run(command, shell=True, check=True)
    
    ags_wall = "/home/alireza/.config/ags/scripts/color_generation/switchwall.sh"
    command = f"{ags_wall} {image_path} &> /dev/null &"
    subprocess.run(command, shell=True, check=True)



def select_rand_wallpaper(dir):
    images = list_images(dir)
    if images:  # Check if there are any images in the directory
        selected_image = random.choice(images)
        set_wallpaper(selected_image)
        print(f'Set wallpaper to "{selected_image}".')
    else:
        print("No images found in the directory.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: [light|dark]")
        sys.exit(1)
    mode = sys.argv[1].lower()
    if mode not in ["light", "dark"]:
        print("Invalid argument. args: [light|dark]")
        sys.exit(1)

    home_dir = os.path.expanduser("~")
    dir_light = os.path.join(home_dir, "Downloads/WallPaper/wallpapers/light")
    dir_dark = os.path.join(home_dir, "Downloads/WallPaper/wallpapers/dark")
    dir = dir_light if mode == "light" else dir_dark
    select_rand_wallpaper(dir)
