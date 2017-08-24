import io

import PIL.Image
import urllib2

import aalib

screen = aalib.AsciiScreen(width=80, height=40)
fp = io.BytesIO(urllib2.urlopen('https://www.python.org/static/favicon.ico').read())
image = PIL.Image.open(fp).convert('L').resize(screen.virtual_size)
screen.put_image((0, 0), image)
print
screen.render()
