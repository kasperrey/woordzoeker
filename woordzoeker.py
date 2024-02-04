import cv2
import numpy as np
from PIL import Image


class Berekenen:
    def __init__(self, veld, zoeken, origineel):
        self.veld = veld
        self.img = np.array(Image.new(mode = "RGB", size = (500, 500), color = (255, 255, 255)))
        y0, dy = 50, 40
        for i, zin in enumerate(origineel.split("\n")):
            y = y0 + i * dy
            cv2.putText(self.img, zin, (50, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        for woord in zoeken:
            if self.zoek(len(woord), woord):
                woord_totaal, pos = self.zoek(len(woord), woord)
                if woord_totaal == woord:
                    self.teken(pos)
            else:
                print("mislukt")
        cv2.imshow("woordzoeker", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def zoek(self, aantal, woord):
        for y in range(len(self.veld)):
            for x in range(len(self.veld[y])):
                if self.veld[y][x] == woord[0]:
                    if len(self.veld)>y+1:
                        pos = [(x, y)]
                        woord_kijk = self.veld[y][x]
                        if self.veld[y+1][x] == woord[1]:
                            woord_kijk += self.veld[y+1][x]
                            woord_uit, pos_2 = self.verder(0, 1, woord_kijk, aantal, x, y)
                            if woord_uit == woord:
                                if pos_2 == ():
                                    pos_2 = (x, y + 1)
                                pos.append(pos_2)
                                return woord_uit, pos
                    if len(self.veld[y])>x+1:
                        pos = [(x, y)]
                        woord_kijk = self.veld[y][x]
                        if self.veld[y][x+1] == woord[1]:
                            woord_kijk += self.veld[y][x+1]
                            woord_uit, pos_2 = self.verder(1, 0, woord_kijk, aantal, x, y)
                            if woord_uit == woord:
                                if pos_2 == ():
                                    pos_2 = (x+1, y)
                                pos.append(pos_2)
                                return woord_uit, pos
                    if 0<=x-1:
                        pos = [(x, y)]
                        woord_kijk = self.veld[y][x]
                        if self.veld[y][x-1] == woord[1]:
                            woord_kijk += self.veld[y][x-1]
                            woord_uit, pos_2 = self.verder(-1, 0, woord_kijk, aantal, x, y)
                            if woord_uit == woord:
                                if pos_2 == ():
                                    pos_2 = (x-1, y)
                                pos.append(pos_2)
                                return woord_uit, pos
                    if 0<=y-1:
                        pos = [(x, y)]
                        woord_kijk = self.veld[y][x]
                        if self.veld[y-1][x] == woord[1]:
                            woord_kijk += self.veld[y-1][x]
                            woord_uit, pos_2 = self.verder(0, -1, woord_kijk, aantal, x, y)
                            if woord_uit == woord:
                                if pos_2 == ():
                                    pos_2 = (x, y-1)
                                pos.append(pos_2)
                                return woord_uit, pos
                    if len(self.veld)>y+1 and len(self.veld[y])>x+1:
                        pos = [(x, y)]
                        woord_kijk = self.veld[y][x]
                        if self.veld[y+1][x+1] == woord[1]:
                            woord_kijk += self.veld[y+1][x+1]
                            woord_uit, pos_2 = self.verder(1, 1, woord_kijk, aantal, x, y)
                            if woord_uit == woord:
                                if pos_2 == ():
                                    pos_2 = (x+1, y+1)
                                pos.append(pos_2)
                                return woord_uit, pos
                    if len(self.veld)>y+1 and 0<=x-1:
                        pos = [(x, y)]
                        woord_kijk = self.veld[y][x]
                        if self.veld[y+1][x-1] == woord[1]:
                            woord_kijk += self.veld[y+1][x-1]
                            woord_uit, pos_2 = self.verder(-1, 1, woord_kijk, aantal, x, y)
                            if woord_uit == woord:
                                if pos_2 == ():
                                    pos_2 = (x-1, y+1)
                                pos.append(pos_2)
                                return woord_uit, pos
                    if 0<=y-1 and len(self.veld[y])>x+1:
                        pos = [(x, y)]
                        woord_kijk = self.veld[y][x]
                        if self.veld[y-1][x+1] == woord[1]:
                            woord_kijk += self.veld[y-1][x+1]
                            woord_uit, pos_2 = self.verder(1, -1, woord_kijk, aantal, x, y)
                            if woord_uit == woord:
                                if pos_2 == ():
                                    pos_2 = (x+1, y-1)
                                pos.append(pos_2)
                                return woord_uit, pos
                    if 0<=y-1 and 0<=x-1:
                        pos = [(x, y)]
                        woord_kijk = self.veld[y][x]
                        if self.veld[y-1][x-1] == woord[1]:
                            woord_kijk += self.veld[y-1][x-1]
                            woord_uit, pos_2 = self.verder(-1, -1, woord_kijk, aantal, x, y)
                            if woord_uit == woord:
                                if pos_2 == ():
                                    pos_2 = (x-1, y-1)
                                pos.append(pos_2)
                                return woord_uit, pos

    def verder(self, plus_x, plus_y, woord_kijk, aantal, x, y):
        woord = woord_kijk
        pos = ()
        for a in range(2, aantal):
            if plus_y > 0 and plus_x == 0:
                if len(self.veld)>y+a:
                    pos = (x, y+a)
                    woord += self.veld[y+a][x]
            elif plus_y < 0 and plus_x == 0:
                if 0 <= y-a:
                    pos = (x, y-a)
                    woord += self.veld[y-a][x]
            elif plus_x > 0 and plus_y == 0:
                if len(self.veld[y]) > x + a:
                    pos = (x+a, y)
                    woord += self.veld[y][x+a]
            elif plus_x < 0 and plus_y == 0:
                if 0 <= x - a:
                    pos = (x-a, y)
                    woord += self.veld[y][x-a]
            elif plus_x > 0 < plus_y:
                if len(self.veld)>y+a and len(self.veld[y]) > x + a:
                    pos = (x+a, y+a)
                    woord += self.veld[y+a][x+a]
            elif plus_x < 0 < plus_y:
                if len(self.veld)>y+a and 0 <= x - a:
                    pos = (x-a, y+a)
                    woord += self.veld[y+a][x-a]
            elif plus_x > 0 > plus_y:
                if 0 <= y-a and len(self.veld[y]) > x + a:
                    pos = (x+a, y-a)
                    woord += self.veld[y-a][x+a]
            elif plus_x < 0 > plus_y:
                if 0 <= y-a and 0 <= x - a:
                    pos = (x-a, y-a)
                    woord += self.veld[y-a][x-a]
        return woord, pos

    def teken(self, pos):
        cv2.line(self.img, (pos[0][0]*35+50, pos[0][1]*40+45), (pos[1][0]*35+50, pos[1][1]*40+45), (0, 0, 0), 2)


# veld_string = """a s p e r g e
# n i i q d e x
# s d v t h n x
# e d v j l t k
# n i a q d e x"""
#
# zoeken = []
#
def maak_lijst(veld):
    lijst = []
    y = veld.split("\n")
    for x in y:
        lijst.append(x.split(" "))
    return lijst

# Berekenen(maak_lijst(veld_string), zoeken, veld_string)
