# وارد کردن کتابخانه های مدنظر
from .colordescriptor import ColorDescriptor
import cv2
import os
from imagesearch.models import Image
from django.conf import settings


# مقداردهی توصیف رنگ
cd = ColorDescriptor((8, 12, 3))

# باز کردن فایل مدنظر ما برای ذخیره کردن
output = open(os.path.join(settings.BASE_DIR, 'image_search_engine', 'image_index.csv'), "w")

images = Image.objects.all()
list_path_image = [ img.image.path for img in images ]

# گرفتن مسیر تصاویر و حلقه بر روی آنها
for imagePath in list_path_image:
	# استخراج آدرس یکتا برای هر عکس
	imageID = imagePath[imagePath.find("/") + 1:]
	# مسیر و لود کردن خود تصویر
	image = cv2.imread(imagePath)
	# توضیحات مربوط به رنگ هر تصویر
	features = cd.describe(image)
	# ذخیره ویژگی های هر تصویر
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))
# بستن فایل 
output.close()


'''
دستور کار کردن با اسکریپت در خط فرمان

$ python index.py --dataset dataset --index index.csv

'''
