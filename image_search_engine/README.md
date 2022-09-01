https://pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/

Place this folder next to the images folder

pip install -r requirements.txt

python index.py --dataset ../<مسیر دایرکتوری تصاویر ما> --index image_index.csv

python search.py --index image_index.csv --query <مسیر تصویر مدنظر برای سرچ> --result-path dataset