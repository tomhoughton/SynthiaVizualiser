from PIL import Image
from gradient import Gradient

def red_change(row):
    m = 1.275
    return row * m

def blue_change(row): 
    m = -1.275
    c = 255
    return (row * m) + 255

def main():

    img = Image.new('RGB', (300, 200), (0, 0, 0))

    # width, height = img.size()
    height = 200
    width = 300

    g = Gradient(startColor=(255, 0, 217), endColor=(205, 255, 199), isVerticle=True, distance=200)
    g.cacl_increase()
    g.obtainM()

    for y in range(0, height):
        # Need to get blue and red values for the row:
        for x in range(0, width):
            color = g.calculate_color(x_coord=y, y_coord=0)
            img.putpixel((x, y), color)

    img.show()

main()
