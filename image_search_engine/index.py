# وارد کردن کتابخانه های مدنظر
from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import os

# تجزیه کننده آرگومان را بسازید و آرگومان ها را تجزیه کنید
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,#برای دریافت مسیر تصاویر ما 
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,#مشخص کردن مسیر ذخیره سازی تصاویر آنالیز شده
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())
# مقداردهی توصیف رنگ
cd = ColorDescriptor((8, 12, 3))

# باز کردن فایل مدنظر ما برای ذخیره کردن
output = open(args["index"], "w")

def test(imagePath):
	# گرفتن مسیر تصاویر و حلقه بر روی آنها
	for imagePath in glob.glob(imagePath + "/*", recursive=True):
		if os.path.isfile(imagePath):
			# استخراج آدرس یکتا برای هر عکس
			imageID = imagePath[imagePath.find("/") + 1:]
			print(imageID)
		    # مسیر و لود کردن خود تصویر
			image = cv2.imread(imagePath)
			# توضیحات مربوط به رنگ هر تصویر
			features = cd.describe(image)
			# ذخیره ویژگی های هر تصویر
			features = [str(f) for f in features]
			output.write("%s,%s\n" % (imageID, ",".join(features)))

		elif os.path.isdir(imagePath):
			test(imagePath)

test(args["dataset"])

# بستن فایل 
output.close()


'''
دستور کار کردن با اسکریپت در خط فرمان

$ python index.py --dataset dataset --index index.csv

'''