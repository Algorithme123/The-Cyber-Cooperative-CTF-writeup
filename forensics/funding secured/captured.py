
from PIL import Image

img = Image.open('captured.png')

w = img.width
h = img.height

contents = ''

for r in range(11):
    for c in range(w):
        contents += ''.join([hex(a % 2)[2:] for a in img.getpixel((c, r))])

final_contents = b''
for i in range(0, len(contents), 8):
    final_contents += bytes([int(contents[i:i+8], 2)])
with open('out.bin', 'wb') as f:
    f.write(final_contents[3:])
