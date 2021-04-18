w = input('請輸入體重(kg):')
w = float(w)
h = input('請輸入身高(cm):')
h = float(h)
h = h/100

BMI = w / (h ** 2)
print('您的身體質量指數是:',BMI)

if BMI < 18.5:
	print('過輕')
elif BMI >= 18.5 and BMI < 24:
	print('正常')
elif BMI >= 24 and BMI <27:
	print('過重')
elif BMI >= 27 and BMI <30:
	print('輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('中度肥胖')
elif BMI >= 35:
	print('重度肥胖')