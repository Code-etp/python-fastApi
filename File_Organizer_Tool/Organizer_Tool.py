import os
import shutil
from pathlib import Path

def get_folder_path():
    while True:
        folder_path = input("Enter the path of the folder to organize: ").strip()
        if os.path.isdir(folder_path):
            return folder_path
        print("Invalid folder path. Please try again.")

def create_category_folders(root_path, categories):
    for category in categories:
        category_path = os.path.join(root_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

def organize_files(folder_path):

    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    }
    

    create_category_folders(folder_path, categories.keys())
    

    moved_files = []
    

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        if os.path.isdir(item_path) or item.startswith('.'):
            continue
        
        file_ext = Path(item).suffix.lower()
        
        moved = False
        for category, extensions in categories.items():
            if file_ext in extensions:
                dest_folder = os.path.join(folder_path, category)
                try:
                    shutil.move(item_path, dest_folder)
                    moved_files.append((item, category))
                    moved = True
                    break
                except Exception as e:
                    print(f"Error moving {item}: {str(e)}")
        
        if not moved:
            dest_folder = os.path.join(folder_path, 'Other')
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            try:
                shutil.move(item_path, dest_folder)
                moved_files.append((item, 'Other'))
            except Exception as e:
                print(f"Error moving {item}: {str(e)}")
    
    return moved_files

def display_results(moved_files):
    if not moved_files:
        print("\nNo files were moved - everything is already organized!")
        return
    
    print("\nOrganization complete! Here's what changed:")
    print("-" * 60)
    print(f"{'File':<40} | {'Moved To':<15}")
    print("-" * 60)
    for file, category in moved_files:
        print(f"{file:<40} | {category:<15}")
    print("-" * 60)
    print(f"Total files moved: {len(moved_files)}")

def main():
    print("File Organizer Tool")
    print("This tool will organize files into folders by their type.\n")
    
    try:
        folder_path = get_folder_path()
        moved_files = organize_files(folder_path)
        display_results(moved_files)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    finally:
        print("\nThank you for using the File Organizer Tool!")
main()