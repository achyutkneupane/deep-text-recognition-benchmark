# Easy OCR Training

This repository contains the code for training Easy OCR model on custom dataset.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Prepare the dataset

In this case, we have dataset from KEC marksheets. The training data is in `train_data` folder and the validation data is in `val_data` folder.

Each folder has a `labels.txt` file which contains the labels for the images in the folder.

#### Distribution

There are `5500 (91.92%)` images in the training dataset and `483 (8.08%)` images in the validation dataset. The ratio is `11.38:1`.


### Create LMDB dataset

To create the LMDB dataset, run the following command:

```bash
cd deep-text-recognition-benchmark
```

Before creating the dataset, update the `create_lmdb_dataset.py` to have below on line `47`:

```python
imagePath, label = datalist[i].strip('\n').split('.jpg')
imagePath += '.jpg'
imagePath = os.path.join(inputPath, imagePath)
```

#### For training dataset

```bash
python create_lmdb_dataset.py ../train_data ../train_data/labels.txt ../train_lmdb
```

#### For validation dataset

```bash
python create_lmdb_dataset.py ../val_data ../val_data/labels.txt ../val_lmdb
```