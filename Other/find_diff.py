"""
name: find_diff
create_time: 2023/8/13 0:24
author: Ethan

Description: 
"""
from copy import copy

from PIL import Image, ImageDraw
import random



def generate_random_color():
    """
    生成随机颜色
    :return:
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def generate_image_with_squares(rows, cols, square_size, border_size):
    """
    绘制一个由小正方形组成的图片
    :param rows: 行数
    :param cols: 列数
    :param square_size: 每个小正方形的边长
    :param border_size: 边框的宽度
    :return:
    """
    image_width = cols * square_size + 2 * border_size
    image_height = rows * square_size + 2 * border_size

    image = Image.new('RGB', (image_width, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # 绘制白色边框
    draw.rectangle((0, 0, image_width - 1, image_height - 1), outline=(255, 255, 255))

    for row in range(rows):
        for col in range(cols):
            x0 = col * square_size + border_size
            y0 = row * square_size + border_size
            x1 = x0 + square_size
            y1 = y0 + square_size

            color = generate_random_color()
            draw.rectangle((x0, y0, x1, y1), fill=color)

    # 随机改变一个小方块的颜色
    random_row = random.randint(0, rows - 1)
    random_col = random.randint(0, cols - 1)
    random_x0 = random_col * square_size + border_size
    random_y0 = random_row * square_size + border_size
    random_x1 = random_x0 + square_size
    random_y1 = random_y0 + square_size
    print(random_row, random_col)
    image1 = copy(image)
    draw1 = ImageDraw.Draw(image1)

    draw1.rectangle((random_x0, random_y0, random_x1, random_y1), fill=generate_random_color())

    return image, image1


def concatenate_images_horizontally(image1, image2):
    """
    拼接两张图片
    :param image1:
    :param image2:
    :return:
    """
    width1, height1 = image1.size
    width2, height2 = image2.size

    new_width = width1 + width2
    new_height = max(height1, height2)

    new_image = Image.new('RGB', (new_width, new_height))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (width1, 0))

    return new_image


n = 10  # 小正方形的行列数
square_size = 50  # 小正方形的边长

image1, image2 = generate_image_with_squares(n, n, square_size, 4)




# 拼接图片
concatenated_image = concatenate_images_horizontally(image1, image2)
concatenated_image.show()  # 显示拼接后的图片