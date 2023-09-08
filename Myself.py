from PIL import Image
# 需要用到的字符
char_set = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''

# 修改图片大小，改为黑白照片
im = Image.open("Photo.jpeg")
im = im.resize((80,50),Image.ANTIALIAS)
im = im.convert("L")
im.save("tt.jpeg")

# 根据色彩选择字符
def get_char(grey):
    if grey >= 240:
        return ' '
    else:
        return char_set[int(grey/(256+1)/len(char_set))]

# 准备将图片转换为文档
text = ''


for i in range(im.height):
    for j in range(im.width):
        gray = im.getpixel((j, i))      # 返回值可能是一个int, 也可能是一个三元组
        if isinstance(gray, tuple):
            gray = int(0.2126 * gray[0] + 0.7152 * gray[1] + 0.0722 * gray[2])

        text += get_char(gray)
    text += "\n"

with  open('Me.txt',"w") as  f:
    f.write(text)





