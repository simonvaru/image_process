# import png

# # Method 1:
# # f = open('ramp.png', 'wb')      # binary mode is important
# # w = png.Writer(256, 1, greyscale=True)
# # w.write(f, [range(256)])

# # Method 2:
# with open('ramp4.png', 'wb') as f:
#     # w = png.Writer(256, 100, greyscale=True)
#     w = png.Writer(256, 100, size=None, greyscale=True, alpha=False, bitdepth=8, palette=None, transparent=None, background=None, gamma=None, compression=None, interlace=False, planes=None, colormap=None, maxval=None, chunk_limit=1048576, x_pixels_per_unit=None, y_pixels_per_unit=None, unit_is_meter=False)
#     w.write(f, [list(range(256))] * 100 )

# f.close()






# import png
# s = ['111100001100001100001111',
#      '111100001100001100001111',
#      '110011001111001100110000',
#      '110011001111001100110000',
#      '111100001100111100110011',
#      '111100001100111100110011',
#      '110000001100001100001111',
#      '110000001100001100001111']
# s = [[int(c) for c in row] for row in s]
# palette=[(0x55,0x55,0x55), (0xff,0x99,0x99)]
# w = png.Writer(len(s[0]), len(s), palette=palette, bitdepth=1)
# f = open('png.png', 'wb')
# w.write(f, s)
# f.close()



# import requests
# from urllib import response
# import png
# import urllib


# url = "https://example.com/image.jpg"
# response = requests.get(url)
# with open("image.jpg", "wb") as f:
#     f.write(response.content)
   
import png
help(png)
