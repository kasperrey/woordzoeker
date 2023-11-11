import pytesseract
import cv2
import woordzoeker

img = cv2.imread('woordzoeker3.png')
hImg, wImg, _ = img.shape
lijst = []
lijst_op_volgorde = []
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    bo = b.split(' ')
    lijst.append(bo)
    # print(bo)
    x, y, w, h = int(bo[1]), int(bo[2]), int(bo[3]), int(bo[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
    cv2.putText(img, bo[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)


def deel_op(lijst):
    i = 0
    string_veld = """"""
    for x in lijst:
        if i == 13:
            i = 0
            string_veld += "\n"
        string_veld += x[0]
        string_veld += " "
        i += 1
    return string_veld

def volgorde(lijst):
    laag = lijst[0]
    for x in lijst:
        if (hImg-int(x[2]))+int(bo[4]) < (hImg-int(laag[2]))+int(bo[4]):
            laag = x
        elif int(x[2]) == int(laag[2]):
            if int(x[1]) < int(laag[1]):
                laag = x
    return laag

#while len(lijst)>0:
#    laag = volgorde(lijst)
#    lijst.remove(laag)
#    lijst_op_volgorde.append(laag)

woordzoeker.Berekenen(woordzoeker.maak_lijst(deel_op(lijst)), ["brussel", "aardwerk", "banaan"], deel_op(lijst))

#cv2.imshow('Detected text', img)
#cv2.waitKey(0)
