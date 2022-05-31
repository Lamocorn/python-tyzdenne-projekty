# 9. zadanie: karel
# autor: Adam Tomala
# datum: 10.12.2021

class RobotKarel:
    def __init__(self, meno_suboru):
        sub = open(meno_suboru, 'r')

        for i in sub:
            tab = i.split()
            break
        self.table = [['' for i in range(int(tab[1]))] for j in range(int(tab[0]))]

        for line in sub.readlines():
            x = line[:-1].split()
            self.table[int(x[1])][int(x[2])] += x[0]
        self.bag = []
        sub.close()
        self.aktualne_umiestnenie = [-1,-1]
        



    def __str__(self):
        vypisatelny = [['' for i in range(len(self.table[0]))] for j in range(len(self.table))]
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if self.table[i][j] == '':
                    vypisatelny[i][j] += '.'
                elif self.table[i][j][0] == '0' and i == self.aktualne_umiestnenie[0] and j == self.aktualne_umiestnenie[1]:
                    vypisatelny[i][j] = '>'
                elif self.table[i][j][0] == '1' and i == self.aktualne_umiestnenie[0] and j == self.aktualne_umiestnenie[1]:
                    vypisatelny[i][j] = 'v'
                elif self.table[i][j][0] == '2' and i == self.aktualne_umiestnenie[0] and j == self.aktualne_umiestnenie[1]:
                    vypisatelny[i][j] = '<'
                elif self.table[i][j][0] == '3' and i == self.aktualne_umiestnenie[0] and j == self.aktualne_umiestnenie[1]:
                    vypisatelny[i][j] = '^'
                else:
                    vypisatelny[i][j] = self.table[i][j][-1]
        return '\n'.join([''.join([str(cell) for cell in row]) for row in vypisatelny])

    def robot(self, riadok, stlpec, smer):
        if len(self.aktualne_umiestnenie) == 0: 
            self.table[riadok][stlpec] = str(smer) + self.table[riadok][stlpec]
            self.aktualny_smer = int(smer)
            self.aktualne_umiestnenie = [int(riadok), int(stlpec)]
        else:
            self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]] = self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]][1:]
            self.aktualny_smer = int(smer)
            self.aktualne_umiestnenie = [int(riadok), int(stlpec)]
            self.table[riadok][stlpec] = str(smer) + self.table[riadok][stlpec]
    def rob(self, prikaz):
        self.pocet_povelov = 0
        prikazy = prikaz.split()
        for i in range(len(prikazy)):
            try:
                k = int(prikazy[i])
            except ValueError:
                try:
                    opakovania = int(prikazy[i-1])
                except ValueError:
                    opakovania = 1
                for j in range(opakovania):
                    # eval('self.'+prikazy[i]+'()')
                    if prikazy[i] == 'vlavo':
                        self.vlavo()
                    elif prikazy[i] == 'vpravo':
                        self.vpravo()
                    elif prikazy[i] == 'zdvihni':
                        self.zdvihni()
                    elif prikazy[i] == 'poloz':
                        self.poloz()
                    elif prikazy[i] == 'batoh':
                        self.batoh()
                    else:
                        self.krok()
        return self.pocet_povelov

    def vlavo(self):
        if self.aktualny_smer == 0:
            self.aktualny_smer = 3
        else:
            self.aktualny_smer -= 1
        l = list(self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]])
        l[0] = str(self.aktualny_smer)
        self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]] = ''.join(l)
        self.pocet_povelov += 1

    def vpravo(self):
        if self.aktualny_smer == 3:
            self.aktualny_smer = 0
        else:
            self.aktualny_smer += 1
        l = list(self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]])
        l[0] = str(self.aktualny_smer)
        self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]] = ''.join(l)
        self.pocet_povelov += 1

    def zdvihni(self):
        if len(self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]])>=2:
            self.bag.append(self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]][-1])
            k = list(self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]])
            k = k[:-1]
            self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]] = ''.join(k)
            self.pocet_povelov += 1
        else:
            pass
    
    def poloz(self):
        try:
            karticka = self.bag[-1]
            policko = list(self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]])
            policko = policko[:1] + [karticka] + policko[1:]
            self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]] = ''.join(policko)
            self.bag.pop(-1)
            self.pocet_povelov += 1
        except IndexError:
            pass

    def krok(self):
        try:
            self.pocet_povelov += 1
            self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]] = self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]][1:]
            if self.aktualny_smer == 0:
                self.aktualne_umiestnenie[1] += 1
            elif self.aktualny_smer == 2:
                if self.aktualne_umiestnenie[1] - 1 < 0:
                    self.pocet_povelov -= 1
                else:
                    self.aktualne_umiestnenie[1] -= 1
            elif self.aktualny_smer == 1:
                self.aktualne_umiestnenie[0] += 1
            else:
                if self.aktualne_umiestnenie[0] - 1 < 0:
                    self.pocet_povelov -= 1
                else:
                    self.aktualne_umiestnenie[0] -= 1
            self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]] = str(self.aktualny_smer) + self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]]
        except IndexError:
            self.pocet_povelov -= 1
            if self.aktualny_smer == 0:
                self.aktualne_umiestnenie[1] -= 1
            elif self.aktualny_smer == 2:
                self.aktualne_umiestnenie[1] += 1
            elif self.aktualny_smer == 1:
                self.aktualne_umiestnenie[0] -= 1
            else:
                self.aktualne_umiestnenie[0] += 1
            self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]] =str(self.aktualny_smer) + self.table[self.aktualne_umiestnenie[0]][self.aktualne_umiestnenie[1]]

    def batoh(self):
        return self.bag

if __name__ == '__main__':
    k = RobotKarel('subor1.txt')
    k.robot(0, 0, 0)
    print(k)
    print(k.rob('krok'))
    print(k.rob('2 zdvihni'))
    k.rob('krok')
    k.rob('vpravo')
    k.rob('krok')
    k.rob('2 zdvihni')
    k.rob('2 krok')
    print(k)
    print('batoh =', k.batoh())
    k.rob('poloz vlavo')
    k.rob('krok 6 vlavo')
    print(k)
    print('batoh =', k.batoh())
    k.robot(1, 3, 2)
    print(k)