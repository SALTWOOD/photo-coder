from PIL import Image
import itertools
import time
import os

class iterer:
	def __init__(self,lst):
		self.lst = lst
		self.count = 0
	
	def next(self):
		res = self.lst[self.count]
		self.count += 1
		return res


def crypt(img):
	width,height = img.size
	im = Image.new('RGB',(height,width),0x0)
	pixels = []
	y = 0
	for y,x in itertools.product(range(height),range(width)):
		pixels.append(img.getpixel((x,y)))
	p = iterer(pixels)
	for y,x in itertools.product(range(width),range(height)):
		im.putpixel((x,y),p.next())
	return im

if __name__ == '__main__':
	img = Image.open('./all.png')
	_img = crypt(img)
	_img.save('out.png')

'''
if __name__ == '__main__':
	lst = os.listdir('./pics')
	for i in lst:
		if os.path.exists('./pics/{}_out.png'.format(i.split('.')[0])):
			print('./pics/{}_out.png'.format(i.split('.')[0]))
			continue
		start = time.time()
		img = Image.open('./pics/{}'.format(i))
		_img = crypt(img)
		_img.save('./pics/{}_out.png'.format(i.split('.')[0]))
		print('Spent: {}ms'.format((time.time() - start) * 1000))
'''
