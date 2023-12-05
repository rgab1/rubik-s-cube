class Face:

    def __init__(self, str_color):
        self.face = []
        for i in range(3):
            self.face.append([str_color, str_color, str_color])

    #lors de la rotation de la ligne du bas ou celle du haut de la face d'un rubik's cube, la face inférieur ou supérieur se voit pivoter
    def pivot(self, direction_pivot):
        tab = self.face
        if direction_pivot == self.voisin1:
            self.face[0] = [tab[2][0], tab[1][0], tab[0][0]]
            self.face[1] = [tab[2][1], tab[1][1], tab[0][1]]
            self.face[2] = [tab[2][2], tab[1][2], tab[0][2]]
        else:
            self.face[0] = [tab[0][2], tab[1][2], tab[2][2]]
            self.face[1] = [tab[0][1], tab[1][1], tab[2][1]]
            self.face[2] = [tab[0][0], tab[1][0], tab[2][0]]


    
    def rotation_horizontale (self, direction_voisin, ligne):
        tab = self.face[ligne]
        if direction_voisin == self.voisin1:
            self.face[ligne] = self.voisin3.face[ligne]
            self.voisin3.face[ligne] = self.voisin3.voisin3.face[ligne]
            self.voisin3.voisin3.face[ligne] = self.voisin1.face[ligne]
            self.voisin1.face[ligne] = tab
        else:
            self.face[ligne] = self.voisin1.face[ligne]
            self.voisin1.face[ligne] = self.voisin1.voisin1.face[ligne]
            self.voisin1.voisin1.face[ligne] = self.voisin3.face[ligne]
            self.voisin3.face[ligne] = tab
        if ligne != 1:
            if direction_voisin == self.voisin1:
                if ligne == 2:
                    self.voisin2.pivot(self.voisin1)
                else:
                    self.voisin0.pivot(self.voisin3)
            else:
                if ligne == 2:
                    self.voisin2.pivot(self.voisin3)
                else:
                    self.voisin0.pivot(self.voisin1)

    def rotation_verticale (self, direction_voisin, colonne):
        tab1 = self.colonne(colonne)
        if direction_voisin == self.voisin0:
            tab2 = self.voisin2.colonne(colonne)
            for i in range(3):
                self.face[i][colonne] = tab2[i]
            tab2 = self.voisin2.voisin2.colonne(colonne)
            for i in range(3):
                self.voisin2.face[i][colonne] = tab2[i]
            tab2 = self.voisin0.colonne(colonne)
            for i in range(3):
                self.voisin2.voisin2.face[i][colonne] = tab2[i]
            for i in range(3):
                self.voisin0.face[i][colonne] = tab1[i]
        else:
            tab2 = self.voisin0.colonne(colonne)
            for i in range(3):
                self.face[i][colonne] = tab2[i]
            tab2 = self.voisin0.voisin0.colonne(colonne)
            for i in range(3):
                self.voisin0.face[i][colonne] = tab2[i]
            tab2 = self.voisin2.colonne(colonne)
            for i in range(3):
                self.voisin0.voisin0.face[i][colonne] = tab2[i]
            for i in range(3):
                self.voisin2.face[i][colonne] = tab1[i]
        if colonne != 1:
            if direction_voisin == self.voisin0:
                if colonne == 2:
                    self.voisin1.pivot(self.voisin1)
                else:
                    self.voisin3.pivot(self.voisin3)
            else:
                if colonne == 2:
                    self.voisin1.pivot(self.voisin3)
                else:
                    self.voisin3.pivot(self.voisin1)

    def colonne (self, colonne):
        tab = []
        for i in range(len(self.face)):
            tab.append(self.face[i][colonne])
        return tab

    def face_color (self):
        print (self.face[1][1])

    def voisins(self, list_voisins):
        self.list_voisins = list_voisins
        self.voisin0 = list_voisins[0]#voisin du dessus
        self.voisin1 = list_voisins[1]#voisin de droite
        self.voisin2 = list_voisins[2]#voisin du dessous
        self.voisin3 = list_voisins[3]#voisin de gauche


    def show (self):
        for i in G.face:
            print (i)
        print ('---------------')
        for i in range(3):
            print(R.face[i]+W.face[i]+O.face[i])
        print ('---------------')
        for i in B.face:
            print (i)
        print ('---------------')
        for i in Y.face:
            print (i)
        print ('---------------')
        for i in range(3):
            print ('---------------')

W = Face('W')
G = Face('G')
Y = Face('Y')
B = Face('B')
O = Face('O')
R = Face('R')
W.voisins([G, O, B, R])
G.voisins([Y, O, W, R])
Y.voisins([B, O, G, R])
B.voisins([W, O, Y, R])
O.voisins([G, W, B, Y])
R.voisins([G, Y, B, W])


W.show()
W.rotation_verticale(G, 1)
W.show()
W.rotation_horizontale(R, 0)
W.show()
