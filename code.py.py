from os.path import exists, join
from lackey import *
import time
import subprocess
import os
from pyautogui import scroll

# Ensure the path to images is set correctly
# Set the current working directory as the root directory
cwd = os.getcwd()
image_folder = "images"
Settings.ImagesPath = join(cwd, image_folder)

# Create the 'images' directory if it doesn't exist
if not os.path.exists(Settings.ImagesPath):
    os.makedirs(Settings.ImagesPath)

# Ensure the path to Edge executable is set correctly
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


# Main automation flow
def main():
    try:
        # Step 1: Launch Microsoft Edge and open the website
        print("Launching Microsoft Edge...")
        subprocess.Popen([edge_path, "https://www.banquepopulaire.fr/"])
        time.sleep(5)

        # Handle other interactions with images
        accept_all_path = join(Settings.ImagesPath, "close.png")
        if exists(accept_all_path, 10):
            click(accept_all_path)
            time.sleep(1)

        # Handle other interactions with images
        accept_all_path = join(Settings.ImagesPath, "Tout accepter.png")
        if exists(accept_all_path, 10):
            click(accept_all_path)
            time.sleep(1)

        print("Scrolling down the page...")
        for _ in range(12):
            scroll(-650)  # Scroll down by 300 units
            time.sleep(2)


        find_agency_path = join(Settings.ImagesPath, "Trouver une agence.png")
        if exists(find_agency_path, 10):  # Check for image with a timeout of 10 seconds
            # print("Image found, clicking...")
            click(find_agency_path)
            time.sleep(2)  # Add a brief pause after clicking

        search_box_path = join(Settings.ImagesPath, "search_box.png")
        postal_code_box_path = join(Settings.ImagesPath, "postal_code_box.png")

        # Check if both search box and postal code box are found within 10 seconds
        if exists(search_box_path, 10) and exists(postal_code_box_path, 10):
            # Handle search box
            click(search_box_path)
            type("Lyon")
            time.sleep(3)

            # Handle postal code box
            click(postal_code_box_path)
            type("69000")
            time.sleep(3)

        print("Scrolling down the page...")
        for _ in range(1):
            scroll(-400)  # Scroll down by 300 units
            time.sleep(1)

        # Clicking the search button
        search_button_path = join(Settings.ImagesPath, "research.png")
        if exists(search_button_path, 5):
            click(search_button_path)
            time.sleep(2)

        # Select Lyon Perrache location
        lyon_perrache_path = join(Settings.ImagesPath, "lyon_perrache.png")
        if exists(lyon_perrache_path, 10):
            click(lyon_perrache_path)
            time.sleep(3)

        print("Scrolling down the page...")
        for _ in range(1):
            scroll(-400)  # Scroll down by 300 units
            time.sleep(1)

        # Click on location 4 on the map
        location_4_path = join(Settings.ImagesPath, "Capture.png")
        if exists(location_4_path, 10):
            click(location_4_path)
            time.sleep(2)
    finally:
        print("Closing Microsoft Edge...")
        os.system("taskkill /im msedge.exe /f")

# Run the script
if __name__ == "__main__":
    main()
