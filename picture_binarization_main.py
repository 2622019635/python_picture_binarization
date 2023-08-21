import argparse

parse = argparse.ArgumentParser(description='picture binarization')
parse.add_argument('-p', '--path', type=str, metavar='\b', help='Picture path.')
parse.add_argument('-t', '--threshold', type=int, default=200,metavar='\b', choices=tuple(range(256)), help='Boundary values for black and white. [0-255]')

args = parse.parse_args()
# # 图片二值化
# from PIL import Image
# img = Image.open('test.jpg')
 
# # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
# Img = img.convert('L')
# Img.save("test1.jpg")
 
# # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
# threshold = 200
 
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
 
# # 图片二值化
# photo = Img.point(table, '1')
# photo.save("test2.jpg")