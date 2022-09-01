# وارد کردن کتابخانه های مدنظر
import numpy as np
import csv

class Searcher:
	def __init__(self, indexPath):
		# مسیر فایل ذخیره شده محتوی تمام تصاویر ما
		self.indexPath = indexPath

	def search(self, queryFeatures, limit = 20):
		# مقدار دهی دیکشنری از نتایج
		results = {}

		# باز کردن فایل محتوی تمامی تصاویر ما
		with open(self.indexPath) as f:
			# مقدار دهی اولیه خواندن سی اس وی
			reader = csv.reader(f)

			# شروع به حلقه زدن روی هر خط فایل
			for row in reader:
				# برای هر ردیف از فایل
				# هیستوگرام آنرا استخراج کنید
				# و ویژگی آنرا با عکس ارسالی کاربر مقایسه کنید
				features = [float(x) for x in row[1:]]
				d = self.chi2_distance(features, queryFeatures)

				# اکنون ما نتایجی مشابه از هر دو را داریم
				# از طریق بردارهایمان و دیکشنری نتایج را آپدیت میکنیم
				# شامل نام و شناسه یکتای هر تصویر
				# مقدار فاصله مورد محاسبه ما
				# مقدار شباهت به تصویر مورد نظر ما
				results[row[0]] = d

			# بستن فایل
			f.close()

		# مرتب کردن خروجی بر اساس شباهت
		# تصویر مرتبط در جلوی لیست قرار میگیرد
		results = sorted([(v, k) for (k, v) in results.items()])

		# بازگشت نتایج به ما
		return results[:limit]

	def chi2_distance(self, histA, histB, eps = 1e-10):
		# محاسبه فاصله مجذور دو 
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		# بازگشت نتایج
		return d