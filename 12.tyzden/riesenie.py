# 12. zadanie: labyrint
# autor: Adam Tomala
# datum: 30.5.


class Labyrinth:
    class Vertex:
        def __init__(self, row, column):  # riadok, stĺpec
            self.adjacent = []         # zoznam susedov, susedia sú typu Vertex
            self.row, self.column = row, column
            self.reward = False           # odmena

        def is_adjacent(self, graph):
            adj = []
            try:
                adj.append(graph[(self.row - 1, self.column)])
            except KeyError:
                pass
            try:
                adj.append(graph[(self.row + 1, self.column)])
            except KeyError:
                pass
            try:
                adj.append(graph[(self.row, self.column + 1)])
            except KeyError:
                pass
            try:
                adj.append(graph[(self.row, self.column - 1)])
            except KeyError:
                pass
            self.adjacent = adj
        
        def wall(self, which):
            try:
                for i in range(len(self.adjacent)):
                    if self.adjacent[i].row == which[0] and self.adjacent[i].column == which[1]:
                        # print(f'{self} {self.adjacent} ' + f' {i}')
                        self.adjacent.pop(i)
            except IndexError:
                pass


        def __repr__(self):
            return f'<{self.row},{self.column}>'

    def __init__(self, file_name):
        self.graph = {}                   # slovník vrcholov grafu – obsahuje objekty typu Vertex
        self.reward_counter = 0
        with open(file_name) as file:
            first_line = file.readline()
            first_line = first_line.split()
            for row in range(int(first_line[0])):
                for col in range(int(first_line[1])):
                    vertex = self.Vertex(row,col)
                    self.graph[(row,col)] = vertex

            for vertex in self.graph:
                self.graph[vertex].is_adjacent(self.graph)
            zoz = []
            first = True
            for line in file:
                line = line.split()
                if len(line) == 2:
                    self.graph[(int(line[0]), int(line[1]))].reward = True
                    self.reward_counter += 1
                else:
                    for num in line:
                        if first:
                            a = int(num)
                            first = False
                        else:
                            first = True
                            zoz.append((a,int(num)))
                    for i in range(len(zoz)):
                        try:
                            self.graph[zoz[i]].wall(zoz[i+1])
                            self.graph[zoz[i+1]].wall(zoz[i])
                        except IndexError:
                            # print(f'nepreslo to pre i = {i}\n zoznam bol {zoz}')
                            pass
                    zoz = []


    def get_vertex(self, row, column):
        return self.graph[(row,column)]

    def change_rewards(self, *seq):
        for i in seq:
            if self.graph[(i[0],i[1])].reward == False:
                self.graph[(i[0],i[1])].reward = True
                self.reward_counter += 1
            else:
                self.graph[(i[0],i[1])].reward = False
                self.reward_counter -= 1

    def start(self, row, column):

        self.visited = set()
        self.cesta = [(row,column)]
        self.riesenia = []
        self.visited.add(self.graph[(row,column)])
        if self.graph[(row,column)].reward == True:
            self.najdene = 1
        else:
            self.najdene = 0
        
        if self.najdene == self.reward_counter:
            return self.cesta
        else:
            self.backtrack(row,column)
        try:
            if self.riesenia[0]:
                return self.riesenia[0]
        except IndexError:
            return []


    def backtrack(self, row, col):

        for i in self.graph[(row,col)].adjacent:
            if i not in self.visited:
                self.visited.add(i)
                self.cesta.append((i.row,i.column))
                if i.reward == True:
                    self.najdene += 1
                if self.najdene == self.reward_counter:
                    self.riesenia.append([i for i in self.cesta])
                else:
                    self.backtrack(i.row,i.column)

                self.cesta.pop()
                self.visited.remove(i)
                if i.reward == True:
                    self.najdene -= 1






if __name__ == '__main__':
    lab = Labyrinth('subor1.txt')
    v = lab.get_vertex(1, 0)
    print('vrchol:', v, 'susedia:', v.adjacent, 'odmena:', v.reward)
    v = lab.get_vertex(0, 2)
    print('vrchol:', v, 'susedia:', v.adjacent, 'odmena:', v.reward)
    print(lab.start(0, 0))
    print(lab.start(0, 2))
    lab.change_rewards((2, 2))
    print(lab.start(0, 0))
