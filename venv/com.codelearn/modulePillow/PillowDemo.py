from PIL import Image, ImageDraw, ImageFont;
# pip install image:

img = Image.new('RGB', (650,625), color="white");
font = ImageFont.load_default();

d = ImageDraw.Draw(img);
d.text((10, 10), "Hello World", font = font, fill="black");
img.show();