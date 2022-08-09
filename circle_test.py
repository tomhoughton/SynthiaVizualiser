from turtle import circle
from PIL import Image, ImageDraw
from circle import Circle

def main():

    img = Image.new('RGB', (300, 300), (0, 0, 0))

    # width, height = img.size()
    height = 300
    width = 300
    size = 300

    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    c = Circle(40)
    circle_points = c.get_circle(50, 50)

    for p in circle_points:
        draw.point((size/2+p[0],size/2+p[1]),(255,255,255))

    img.show()
    

main()