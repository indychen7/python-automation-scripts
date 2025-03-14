import requests
import os
from PIL import Image
from io import BytesIO

# ✅ Folder to save images
SAVE_FOLDER = "downloaded_images"

def download_image(image_url):
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an error if request fails

        # Get image name from URL
        image_name = os.path.join(SAVE_FOLDER, image_url.split("/")[-1])

        # Save the image
        with open(image_name, "wb") as file:
            file.write(response.content)

        # ✅ Check if it's a valid image
        img = Image.open(BytesIO(response.content))
        img.verify()

        print(f"✅ Image downloaded successfully: {image_name}")

    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    image_url = input("Enter the image URL: ").strip()
    download_image(image_url)
