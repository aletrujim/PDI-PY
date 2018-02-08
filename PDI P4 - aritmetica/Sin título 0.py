import cv2 

img1 = cv2.imread('fig1.png')           
height1, width1, channels1 = img1.shape

img2 = cv2.imread('fig2.png')           
height2, width2, channels2 = img2.shape

#yiq_img1 = rgb_yiq(img1, width1, height1)
yiq_img1 = img2
for w in range(width1):
    for h in range(height1):
        r, g, b = tuple(img1[h][w]) 
        y = 0.299*r + 0.587*g + 0.114*b
        i = 0.595716*r - 0.274453*g - 0.321263*b
        q = 0.211456*r - 0.522591*g + 0.311135*b                                                   
        yiq_img1[h, w] = [y, i, q]

#yiq_img2 = rgb_yiq(img2, width2, height2)yiq_img = img1
yiq_img2 = img2
for w in range(width2):
    for h in range(height2):
        r, g, b = tuple(img2[h][w]) 
        y = 0.299*r + 0.587*g + 0.114*b
        i = 0.595716*r - 0.274453*g - 0.321263*b
        q = 0.211456*r - 0.522591*g + 0.311135*b                                                   
        yiq_img2[h, w] = [y, i, q]

#opera
yiq_img3 = yiq_img1
for w in range(width1):
    for h in range(height1):
        y1, i1, q1 = tuple(yiq_img1[h][w])
        y2, i2, q2 = tuple(yiq_img2[h][w])
        if y1 > y2:
            y = y1
            i = i1
            q = q1
        elif y2 > y1:
            y = y2
            i = i2
            q = q2
        yiq_img3[h, w] = [y, i, q]
         
#img3 = yiq_rgb(yiq_img3, width1, height1)
rgb_img3 =  yiq_img3
for w in range(width1):
    for h in range(height1):
        y, i, q = tuple(yiq_img3[h][w]) 
        r = y + 0.948262*i + 0.624013*q
        g = y - 0.276066*i - 0.639810*q
        b = y - 1.105450*i + 1.729860*q                                               
        rgb_img3[h, w] = [r, g, b]

print rgb_img3
