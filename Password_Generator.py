import random

def get_upper():
    '''
    生成大写字母
    :return:产生一到两位大写字母
    '''
    count = random.randint(1, 3)
    return random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=count)


def get_special_char():
    '''
    生成特殊符号
    :return:一到两位特殊字符
    '''
    count = random.randint(1, 3)
    return random.choices('!@$%^&*()_+~', k=count)


def get_lower(count):
    '''
    生成小写字母和数字
    :param count:需要小写字母和数字的数量
    :return:
    '''
    string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return random.choices(string, k=count)

# 在D:/Password文件夹下存储密码
f = open('D://Password','a',encoding="UTF-8")

Website = input("请输入你需要的XX网站：")
length =int(input("请输入你所需要的密码长度："))


# password += random.choices(get_num(),get_low(),get_upper(),get_special_char(),k=5)
if length < 6:
    length = 6
lst = []
upper_lst = get_upper()     # 大写
special_char = get_special_char()      # 特殊字符
lst.extend(upper_lst)
lst.extend(special_char)

surplus_count = length - len(lst)
lower_lst = get_lower(surplus_count)
lst.extend(lower_lst)
# 将顺序打乱
random.shuffle(lst)

print(lst)
print(''.join(lst))

f.write(f"网站：{Website}  密码：{''.join(lst)}\n")
f.close()

