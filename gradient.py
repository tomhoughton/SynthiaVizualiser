from PIL import Image

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
    for y in range(0, height):
        # Need to get blue and red values for the row:
        blue = blue_change(row=y)
        red = red_change(row=y)
        for x in range(0, width):
            img.putpixel((x, y), (int(red), int(blue), int(blue)))

    img.show()

main()
