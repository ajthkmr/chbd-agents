from openocr import OpenOCR

engine = OpenOCR()

img_path = 'C:\\Users\\Ajithkumar K\\Desktop\\agent base\\20250310_124035.jpg'
result, elapse = engine(img_path)

# Server mode
# engine = OpenOCR(mode='server')