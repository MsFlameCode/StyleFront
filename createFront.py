from PIL import Image, ImageDraw, ImageFont
import const


def transparent():
    w = len(const.INPUT_TEXT)*200+200
    h = 800
    if len(const.INPUT_TEXT) < const.STR_LEN:
        h = 300
        w = len(const.INPUT_TEXT)*100
    size_text = len(const.INPUT_TEXT)*20
    if len(const.INPUT_TEXT) > const.STR_LEN:
        size_text = 400
    img = Image.new('RGB', (w, h), color='white')
    img = img.convert("RGBA")
    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            pixdata[x, y] = (0, 0, 0, 0)
    font = ImageFont.truetype(const.CONST_FRONT_NAME, size_text)
    drawer = ImageDraw.Draw(img)
    drawer.text((0, 0), const.INPUT_TEXT, font=font, fill=const.CONST_COLOR_NAME)
    const.CUR_NAME = 'front_{:d}.png'.format(const.CONST_COUNT)
    img.save(const.CUR_NAME)
    const.CONST_COUNT += 1
    return img

