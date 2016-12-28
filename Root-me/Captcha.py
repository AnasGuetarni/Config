from PIL import Image
import ImageEnhance, base64, requests, time
import pytesser as pytesser
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def save_captcha(s, link, filename):
	r = s.get(link)
	source = r.text.encode('utf-8')
	source = source.split('base64,')[1]
	source = source.split('" /><br>')[0]
	with open(filename, 'wb') as f:
		f.write(base64.b64decode(source))

pytesser.tesseract_exe_name = 'C:/Python27/Lib/site-packages/tesseract.exe'
filename = 'temp.png'

s = requests.Session()
save_captcha(s, 'http://challenge01.root-me.org/programmation/ch8/', filename)

imgx = Image.open(filename)
imgx = imgx.convert("RGBA")
pix = imgx.load()
for y in xrange(imgx.size[1]):
	for x in xrange(imgx.size[0]):
		if pix[x, y] == (0, 0, 0, 255):
			pix[x, y] = (255, 255, 255, 255)
imgx.save("bw.gif", "GIF")
original = Image.open('bw.gif')
captcha = ''.join(pytesser.image_to_string(original).strip().split())
print captcha
r = s.post('http://challenge01.root-me.org/programmation/ch8/', data = {'cametu':captcha})
source = r.text.encode('utf-8')
print strip_tags(source)
