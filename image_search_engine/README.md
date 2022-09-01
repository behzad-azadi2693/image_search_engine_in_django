https://pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/

Place this folder next to the images folder

pip install -r requirements.txt

python index.py --dataset <path directory images> --index image_index.csv

python search.py --index image_index.csv --query <path image for search> --result-path dataset
