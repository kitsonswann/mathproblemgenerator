import json
from worksheetgenerator.mathgenerator.addition import generate_addition_problem
from pathlib import Path
from dash import html
import numpy
import glob
from PIL import Image
import dash_bootstrap_components as dbc


ROOT = Path(__file__).parent.absolute().parent.absolute().as_posix()

N_QUESTIONS_PER_PAGE = 3

def add_margin(img, target_square=90):
    width, height = img.size

    left = (target_square - width) // 2
    right = (target_square - width) % 2

    top = (target_square - height) // 2
    bottom = (target_square - height) % 2

    result = Image.new(img.mode, (90, 90), color=(255, 255, 255))
    result.paste(img, (left, top))
    return result

def resize_image(img, target_sqaure=90):

    width, height = img.size

    if width > height:
        adjustment_percentage = 1 + ((target_sqaure - width)/width)
    else:
        adjustment_percentage = 1 + ((target_sqaure - height)/height)

    new_width = int(adjustment_percentage*width)
    new_height = int(adjustment_percentage*height)
    img = img.resize(size=(new_width, new_height))
    img = add_margin(img)

    return img

def load_images():
    image_paths = glob.glob(ROOT + '/assets/*.png')
    images = []
    for path in image_paths:
        img = Image.open(path)
        img = resize_image(img)
        images.append(img)
    return images


def generate_image_arrangement(n, cols=3, images=load_images()):
    image = images[numpy.random.randint(0, len(images))]
    empty = Image.new('RGB', (90, 90), color=(255,255,255))

    laid_out = 0
    rows = []
    while laid_out < 9:
        row = []
        for col in range(cols):
            if laid_out < n:
                row.append(dbc.Col(html.Img(src=image), md=4))
            else:
                row.append(dbc.Col(html.Img(src=empty), md=4))
            laid_out += 1
        rows.append(dbc.Row(row))
    
    return html.Div(rows)


def generate_table_rows(images):

    table_rows = []
    for row in range(N_QUESTIONS_PER_PAGE):
        left, right, answer = generate_addition_problem()
        row = dbc.Row(
            [
                dbc.Col(generate_image_arrangement(left, images=images)), 
                dbc.Col(html.H1('+')),
                dbc.Col(generate_image_arrangement(right, images=images)),
                dbc.Col(html.H1('=')),
                dbc.Col(html.H1(answer), className='answer-td')
            ],
            align='center'
        )
        table_rows.append(row)

    return table_rows

