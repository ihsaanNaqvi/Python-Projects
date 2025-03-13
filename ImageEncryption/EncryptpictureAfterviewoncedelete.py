import os
import time

def check_file_processed(flag_file):
    """Check if the image has already been processed."""
    return os.path.exists(flag_file)

def create_flag_file(flag_file):
    """Create a flag file to mark the image as processed."""
    with open(flag_file, 'w') as f:
        f.write("Processed")

def delete_image(image_path):
    """Delete the image file after processing."""
    if os.path.exists(image_path):
        os.remove(image_path)
        print("Image has been deleted.")

def open_image(image_path):
    """Open the image with the default image viewer."""
    if os.path.exists(image_path):
        os.startfile(image_path)  # Open image using default viewer on Windows
    else:
        print("Image file does not exist.")

def main():
    image_path = r'C:\Users\Ibn e Ali\Desktop\1711187113132.jpg'  # Path to image
    flag_file = "image_processed.flag"  # Flag file to track processing
    view_duration = 5  # Time (in seconds) before deleting the image


    # Check if the image has already been viewed and deleted
    if check_file_processed(flag_file):
        print("This image has already been viewed and deleted. You cannot open it again.")
        return  # Exit if the file has already been processed

    # Open the image
    open_image(image_path)

    print(f"Image will be deleted after {view_duration} seconds...")
    time.sleep(view_duration)  # Wait for specified time before deletion

    # Mark as processed
    create_flag_file(flag_file)

    # Delete the image
    delete_image(image_path)

if __name__ == "__main__":
    main()

 
 #Command to create exe file 
#pyinstaller --onefile --noconsole EncryptpictureAfterviewoncedelete.py 
#PS D:\MS Big Data and Data Science\Second Semester\Python programming By
#  Sir Mikhail Ovsiannikov\Python-Projects\ImageEncryption> 
# pyinstaller --onefile --noconsole EncryptpictureAfterviewoncedelete.py