# وارد کردن کتابخانه های مورد نیاز
import numpy as np
import cv2
import imutils

class ColorDescriptor:
	def __init__(self, bins):
		# ذخیره تعدادی اضافه از هیستوگرام
		self.bins = bins
	#گرفتن تصویر مورد جستجو از کاربر
	def describe(self, image):
		# تبدیل فضای رنگی تصویر و مقداردهی اولیه
		# ویژگی های مورد استفاده کمیت تصویر
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		# گرفتن ابعاد تصویر و یافتن مرکز آن
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))

        
		#تقسیم تصویر به پنج قسمت مرکزی و گوشه ها
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),(0, cX, cY, h)] 


		
		#تعیین مرکز تصویر با شعاع ۷۵ درصد از عکس
		(axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75) // 2) 
		ellipMask = np.zeros(image.shape[:2], dtype = "uint8")# ساخت یک تصویر با همان ابعاد مدنظر با پس زمینه سیاه
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)#قرار دادن دایره مرکزی بر روی آن

		# حلقه روی بخش ها
		for (startX, endX, startY, endY) in segments:
			# برای هر گوشه از تصویر یک ماسک بسازید و از آن کم کنید
			# مرکز بیضوی از آن را مشخص کنید
			cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
			cornerMask = cv2.subtract(cornerMask, ellipMask)


			# برای هر قسمت جدول هیستوگرام را صدا واستخراج میکنیم
			hist = self.histogram(image, cornerMask)#آپدیت بردار وکتور
			features.extend(hist)


		# استخراج یک هیستوگرام رنگی از قسمت مرکزی
		hist = self.histogram(image, ellipMask)
		features.extend(hist)#آپدیت بردار وکتور

		# بازگشت دادن ویزگی ها
		return features

	# متد هیستوگرام دو مقدار میگیرد اولی ایمیج مدنظر ما
	# دومی ماسکی از ناحیه تصویر که میخواهیم توصیف کنیم
	def histogram(self, image, mask):
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,# محاسبه هیستوگرام ناحیه پوشانده شده تصویر
			[0, 180, 0, 256, 0, 256])

		# نرمال کردن هیستوگرام با کتابخانه مدنظر
		if imutils.is_cv2():
			hist = cv2.normalize(hist).flatten()

		# کنترل نرمالایز کردن هیستوگرام

		else:
			hist = cv2.normalize(hist, hist).flatten()
		# بازگشت هیستوگرام
		return hist