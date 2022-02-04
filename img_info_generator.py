from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np

lh = "http://localhost:8080/static/"
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


def list_of_categories(n):
    """function create list of categories

    Args:
        n (int): number of needed files

    Returns:
        words (list): list of random categories from 0 to 10
    """
    words = []
    for k in range(n):
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


def create_image(n, words):
    """Generator from text categories to img file

    Args:
        n (int): number of needed files
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
    d = ImageDraw.Draw(out)

    # get style on it
    d.text((250, 75), f"{words}", font=fnt, anchor="ms", fill=(0, 0, 0), align="center")
    # saving file
    out.save(f"static/image{n+1}.jpg", dpi=(500, 500))


def create_images(n):
    """Uses 'create_image' function to create multiple images and get info.csv file

    Args:
        n (int): number of needed files
    """
    words = list_of_categories(n)
    CSV = []
    for i in range(len(words)):
        CSV.append(
            str(
                lh
                + f"image{i+1}.jpg"
                + ";"
                + f"{random.randint(1, 51)}"
                + ";"
                + words[i]
            )
        )
        split_words = words[i].split(";")
        create_image(i, split_words)
        text_info = np.array(CSV)[:, None]
        np.savetxt("info.csv", text_info, fmt="%s")
        print(f"Now processing image{i}.jpg", end="\r")


create_images(999)
