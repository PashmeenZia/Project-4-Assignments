import os  

def bulk_rename(folder_path, new_name):  
    """Renames all files in the given folder to a new format."""  
    try:  
        files = os.listdir(folder_path)  # Get all files in the folder  
        
        for index, file in enumerate(files, start=1):  
            file_ext = os.path.splitext(file)[1]  # Get file extension  
            new_filename = f"{new_name}_{index}{file_ext}"  # Rename format  
            old_path = os.path.join(folder_path, file)  
            new_path = os.path.join(folder_path, new_filename)  
            
            os.rename(old_path, new_path)  # Rename the file  
        
        print("✅ Files renamed successfully!")  

    except Exception as e:  
        print(f"⚠️ Error: {e}")  

#  User Input  
folder = input("Enter folder path: ")  
name_format = input("Enter new name format: ")  
bulk_rename(folder, name_format)  