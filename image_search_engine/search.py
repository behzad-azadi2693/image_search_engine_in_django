# وارد کردن کتابخانه های مدنظر
from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2

# مشخص کردن آرگومان های فایل ایندکس تصاویر و تصویر مدنظر کاربر و محل خروجی
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result_path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# مقداری دهی هیستوگرام مططابق سایر کدها
cd = ColorDescriptor((8, 12, 3))

# بارگیری عکس و مقداردهی اولیه آن
query = cv2.imread(args["query"])
features = cd.describe(query)

# انجام جستجو براساس هیستوگرام و بازگشت نتایج
searcher = Searcher(args["index"])
results = searcher.search(features)


print(results)
'''
# نمایش جستجو به کاربر
cv2.imshow("Query", query)

# حلقه بر روی نتایج 
for (score, resultID) in results:
	# لود کردن نتایج و نمایش دادن آن
	result = cv2.imread(args["result_path"] + "/" + resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)

$ python search.py --index index.csv --query queries/108100.png --result_path dataset
'''