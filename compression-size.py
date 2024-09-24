import os
from PIL import Image

def resize_images_in_folder(source_folder, target_folder_40, target_folder_120):
    os.makedirs(target_folder_40, exist_ok=True)
    os.makedirs(target_folder_120, exist_ok=True)
    
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith('.jpeg'):
            full_file_path = os.path.join(source_folder, file_name)
            
            output_path_40 = os.path.join(target_folder_40, file_name)
            output_path_120 = os.path.join(target_folder_120, file_name)
            
            with Image.open(full_file_path) as img:
                img_resized_40 = img.resize((40, 40), Image.Resampling.LANCZOS)
                img_resized_40.save(output_path_40)
                
                img_resized_120 = img.resize((120, 120), Image.Resampling.LANCZOS)
                img_resized_120.save(output_path_120)

source_folder = './coco_imagens_jpeg'
target_folder_40 = './coco_imagens_40x40'
target_folder_120 = './coco_imagens_120x120'


resize_images_in_folder(source_folder, target_folder_40, target_folder_120)
