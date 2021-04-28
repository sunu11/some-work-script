from PIL import Image

im = Image.open("mistery_picture.bmp")
pix = im.load()
width, height = im.size

extracted_bits = []
for y in range(height):
    for x in range(width):
        r, g, b = pix[(x,y)]
#        print(r&1)
        extracted_bits.append(b & 1)
        extracted_bits.append(g & 1)
        extracted_bits.append(r & 1)

open('1.txt','w').write(''.join(map(str,extracted_bits)))
with open('1.txt','r') as f:
# with open('1.txt','r') as f:
    r = f.read()
    r=r.strip()
    rst = ""
    for j in range(0,10,1):
        for i in range(j,len(r),8):
            a = r[i:i+8]
            a = a[::-1]
            x = int(a,2)
            rst = rst + chr(x)
        if "Iron" in rst:
            print(j)
            print(rst)

