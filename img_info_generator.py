import random
from PIL import Image, ImageDraw, ImageFont
import numpy as np

LH = "http://localhost:8080/static/"
categories = (
    "apple",
    "banana",
    "city",
    "drill",
    "ear",
    "forest",
    "gim",
    "hill",
    "ink",
    "juice",
    "koala",
    "lion",
    "mouse",
    "notebook",
    "octopus",
    "panda",
    "queen",
    "rabbit",
    "sun",
    "tea",
)


def list_of_categories(num):
    """function create list of categories

    Args:
        num (int): number of needed files

    Returns:
        words (list): list of random categories from 0 to 10
    """
    words = []
    for num in range(num):
        temp_str = ""
        list_categories = list(categories)
        rnd_val = random.randint(1, 10)
        # loop to generate random value of categories from 0 to 10
        for i in range(rnd_val):
            if i == 0:
                rnd_category = list_categories[
                    random.randint(0, len(list_categories) - 1)
                ]
                temp_str += rnd_category
                list_categories.remove(rnd_category)
            else:
                temp_str += ";"
                rnd_category = list_categories[
                    random.randint(0, len(list_categories) - 1)
                ]
                temp_str += rnd_category
                list_categories.remove(rnd_category)
        words.append(temp_str)
    return words


def create_image(num, words):
    """Generator from text categories to img file

    Args:
        num (int): number of needed files
        words (list): list of random categories from 0 to 10
    """
    words = "\n".join(words)
    # create an image
    out = Image.new(
        "RGB",
        (500, 500),
        (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
    )

    # get a font
    fnt = ImageFont.truetype("arial.ttf", 40)

    # get a drawing context
    drw = ImageDraw.Draw(out)

    # get style on it
    drw.text(
        (250, 75), f"{words}", font=fnt, anchor="ms", fill=(0, 0, 0), align="center"
    )
    # saving file
    out.save(f"static/image{num+1}.jpg", dpi=(500, 500))


def create_images(num):
    """Uses 'create_image' function to create multiple images and get info.csv file

    Args:
        n (int): number of needed files
    """
    words = list_of_categories(num)
    csv = []
    for i, words in enumerate(words):
        csv.append(
            str(LH + f"image{i+1}.jpg" + ";" + f"{random.randint(1, 51)}" + ";" + words)
        )
        split_words = words.split(";")
        create_image(i, split_words)
        text_info = np.array(csv)[:, None]
        np.savetxt("info.csv", text_info, fmt="%s")
        print(f"Now processing image{i+1}.jpg", end="\r")


create_images(999)
