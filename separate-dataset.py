import os
import random
import shutil

dataset_folder = 'dataset'
labels_file = os.path.join(dataset_folder, 'labels.txt')

with open(labels_file, 'r') as f:
    labels = f.readlines()

def copy_files_and_create_labels(files, folder):
    with open(os.path.join(folder, 'labels.txt'), 'w') as label_file:
        for file in files:
            shutil.copy(os.path.join(dataset_folder, file), folder)
            for label in labels:
                filename = label.split(',')[0]
                if filename == file:
                    print(filename, file)
                    label_file.write(label)
                    break

def separate_files():
    files = os.listdir(dataset_folder)
    files = [file for file in files if file.endswith('.jpg')]

    random.shuffle(files)
    
    train_files = files[:4499]
    val_files = files[5600:]
    
    train_files.sort()
    val_files.sort()

    os.makedirs('train_data', exist_ok=True)
    os.makedirs('val_data', exist_ok=True)

    copy_files_and_create_labels(train_files, 'train_data')
    copy_files_and_create_labels(val_files, 'val_data')

separate_files()