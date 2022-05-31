# 5. zadanie: binarny strom
# autor: Adam Tomala
# datum: 12.4.

class Node:
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
    def __str__(self) -> str:
        return self.data
def add_node(root, string):
    if root is None:
        kde_som = Node(None)
        koren = kde_som
    else:
        kde_som = root
        koren = root
    data = string.split(':')[0]
    cesta =''.join(string.split(':')[1:])
    for i in cesta:
        if i in ['l','L'] and kde_som.left != None:
            kde_som = kde_som.left
        elif i in ['l','L'] and kde_som.left == None:
            kde_som.left = Node(None)
            kde_som = kde_som.left
        elif i in ['r','R'] and kde_som.right != None:
            kde_som = kde_som.right
        elif i in ['r','R'] and kde_som.right == None:
            kde_som.right = Node(None)
            kde_som = kde_som.right
    kde_som.data = data

    return koren


def create_tree(file_name):
    koren = Node(None)
    with open(file_name, 'r') as subor:
        for i in subor:
            add_node(koren,i)
    return koren


def write_tree_to_file(root, file_name):
    def loop(root, predchodcovia, file):
        if root.data is None:
            pass
        else:
            file.write(f'{root.data}:{predchodcovia}\n')
        if root.left is not None:
            loop(root.left, predchodcovia+'l', file)
        if root.right is not None:
            loop(root.right, predchodcovia+'r', file)
    with open(file_name, 'w+') as subor:
        loop(root, '', subor)
        pos = subor.tell() - 1

def most_frequent(root):
    if root is None:
        return ''
    else:
        def loop(root):
            zoz = str(root.data)
            if root.left is not None:
                zoz += ':' + str(loop(root.left))
            if root.right is not None:
                zoz += ':' + str(loop(root.right))
            return zoz
        k = loop(root)
        k = list(filter(lambda val: val !=  'None', k.split(':')))
        return max(set(k), key=k.count)

def number(root):
    if root is None:
        return (0,0)
    else:
        pocet = 1
        pocet_none = 1
        if root.data == None:
            pocet_none = 0
        if root is None:
            return 0
        if root is not None:
            if root.left is not None:
                pocet += number(root.left)[1]
                pocet_none += number(root.left)[0]
            if root.right is not None:
                pocet += number(root.right)[1]
                pocet_none += number(root.right)[0]
        return pocet_none, pocet 

# root = None
# root = add_node(root, 'KING')    
# print(root)                 # Node('KING')
# root = add_node(root, 'QUEEN:L')                  # Node('KING', Node('QUEEN'))
# print(root)
# print(root.left)
# root = add_node(root, 'PRINCE: L L L')            # Node('KING', Node('QUEEN', Node(None, Node('PRINCE'))))
# root = add_node(root, 'FROG:w h y a m i f r o g') # Node('KING', Node('QUEEN', Node(None, Node('PRINCE'))), Node('FROG'))

# root = add_node(root, 'KING:w h y a m i f r o grrrrr')
# print(root.left)
# print(number(root))
# print(most_frequent(root))
if __name__ == '__main__':
    s = add_node(None, 'a:rxl l')
    s = add_node(s, 'b:rl')
    s = add_node(s, 'c:LL')
    write_tree_to_file(s, 'strom1.txt')
    t = create_tree('strom1.txt')
    print(number(t))
    t = add_node(t, 'x')
    t = add_node(t, 'd:' + 'lr'*10)
    write_tree_to_file(t, 'strom2.txt')
    print('subor strom1.txt')
    print(open('strom1.txt').read())
    print('subor strom2.txt')
    print(open('strom2.txt').read())
