# وارد کردن کتابخانه های مدنظر
from colordescriptor import ColorDescriptor
import cv2
import os

# مقداردهی توصیف رنگ
cd = ColorDescriptor((8, 12, 3))

# باز کردن فایل مدنظر ما برای ذخیره کردن
output = open('image_index.csv', "w")

#خواندن مسیرها از درون فایل و ایجاد لیست
with open('write_path.txt', 'r') as file_in:
	list_path_image = []
	for line in file_in:
        	check_path = line.replace('\n', '')
        	if os.path.isfile(check_path):
    	    		list_path_image.append(check_path)
        	else:
            		pass


# گرفتن مسیر تصاویر و حلقه بر روی آنها
for imagePath in list_path_image:
	# استخراج آدرس یکتا برای هر عکس
	imageID = imagePath[imagePath.find("/") + 1:]
	print(imagePath)
	# مسیر و لود کردن خود تصویر
	image = cv2.imread(imagePath)
	# توضیحات مربوط به رنگ هر تصویر
	features = cd.describe(image)
	# ذخیره ویژگی های هر تصویر
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))
	
# بستن فایل 
output.close()

