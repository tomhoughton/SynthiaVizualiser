from turtle import circle
from PIL import Image, ImageDraw
from circle import Circle
from gradient import Gradient

def main():

    img = Image.new('RGB', (300, 300), (0, 0, 0))

    # width, height = img.size()
    height = 300
    width = 300
    size = 300

    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    c = Circle(60)
    circle_points = c.get_circle(50, 50)

    circles = c.get_circles()

    g = Gradient(startColor=(255, 0, 26), endColor=(205, 0, 255), isVerticle=True, distance=(60))
    g.cacl_increase()
    g.obtainM()
    
    for r in range(1, 40):
        color = g.calculate_color(x_coord=r, y_coord=0)
        print(color)

    for r, circle in enumerate(circles):
        color = g.calculate_color(x_coord=r, y_coord=0)

        for p in circle:
            draw.point((size/2+p[0],size/2+p[1]),color)
        
        
    img.show()
    
    

main()