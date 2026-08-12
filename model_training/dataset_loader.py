
import os
import glob
from collections import Counter
import cv2
from sklearn.model_selection import train_test_split

def load_dataset(dataset_path):
    """
    Scans the dataset folder, verifies images, and extracts paths and labels.
    """
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset path {dataset_path} does not exist.")

    image_paths = []
    labels = []
    
    # A-Z capital letters
   # classes = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # ['A', 'B', ..., 'Z']
    classes = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # ['A', 'B', ..., 'Z']
    # classes = [str(i) for i in range(10)]


    # Handle inconsistent naming: 'S_cap' vs 'A_caps'
    def get_folder_name(letter):
        # folder_caps  = os.path.join(dataset_path, f"digit_{letter}")#_caps")
        folder_caps   = os.path.join(dataset_path, f"{letter}")#_cap")
        if os.path.exists(folder_caps):
            return folder_caps
     
        return None

    class_to_idx = {c: idx for idx, c in enumerate(classes)}  # A=0, B=1, ..., Z=25
    
    print(f"Scanning dataset in: {dataset_path}")
    
    corrupted_files = 0
    valid_files = 0

    for letter, idx in class_to_idx.items():
        folder_path = get_folder_name(letter)
        if folder_path is None:
            print(f"Warning: Folder for '{letter}' not found.")
            continue
        print(f"Checking folder: {folder_path}")

        extensions = ('*.jpg', '*.jpeg', '*.png')
        files = []
        for ext in extensions:
            files.extend(glob.glob(os.path.join(folder_path, ext)))
            files.extend(glob.glob(os.path.join(folder_path, ext.upper())))
            
        for file in files:
            try:
                img = cv2.imread(file)
                if img is None:
                    corrupted_files += 1
                else:
                    image_paths.append(file)
                    labels.append(idx)
                    valid_files += 1
            except Exception:
                corrupted_files += 1

    print(f"Found {valid_files} valid images.")
    print(f"Found {corrupted_files} corrupted images (skipped).")
    
    return image_paths, labels


def get_dataset_stats(labels, split_name="Dataset"):
    """Prints statistics about the dataset."""
    counts = Counter(labels)
    classes = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    print(f"\n--- {split_name} Statistics ---")
    print(f"Total images: {len(labels)}")
    print("Images per class:")
    for idx, letter in enumerate(classes):
        print(f"  {letter}: {counts.get(idx, 0)}")


def prepare_data_splits(image_paths, labels, test_size=0.2, random_state=42):
    """
    Splits the data into train (used for CV) and hold-out test set.
    """
    X_train_cv, X_test, y_train_cv, y_test = train_test_split(
        image_paths, labels, test_size=test_size, stratify=labels, random_state=random_state
    )
    
    get_dataset_stats(labels,    "Full Dataset")
    get_dataset_stats(y_train_cv,"Train/CV Split (80%)")
    get_dataset_stats(y_test,    "Hold-out Test Split (20%)")
    
    return X_train_cv, X_test, y_train_cv, y_test