# 1. zadanie: vyraz
# autor: Adam Tomala
# datum: 22.2.2022


class EmptyError(Exception): pass

class Stack:

    def __init__(self):
        '''inicializuje zoznam'''
        self._prvky = []

    def push(self, data):
        '''na vrch zásobníka vloží novú hodnotu'''
        self._prvky.append(data)

    def pop(self):
        '''z vrchu zásobníka vyberie hodnotu, alebo vyvolá EmptyError'''
        if self.is_empty():
            raise EmptyError('prazdny zasobnik')
        return self._prvky.pop()

    def top(self):
        '''z vrchu zásobníka vráti hodnotu, alebo vyvolá EmptyError'''
        if self.is_empty():
            raise EmptyError('prazdny zasobnik')
        return self._prvky[-1]

    def is_empty(self):
        '''zistí, či je zásobník prázdny'''
        return self._prvky == []

class Expression:
    def __init__(self):
        self.tab = {}

    def __repr__(self):
        toto = ''
        for i in self.tab:
            toto += f"{i}: '{self.tab[i]}'\n"
        toto = toto[:-1]
        return toto


    def to_prefix(self, expr):
        k = self.nadrobne(expr)
        s = ''
        for i in k:
            s += i + ' '
        s = s[:-1]
        return s

    def assign(self, var, expr):
        self.tab[var] = self.to_prefix(expr)

    def evaluate(self, retaz):
        s = self.to_prefix(retaz)
        k = s.split()
      
        for index, item in enumerate(k):
            if item in self.tab:
                k[index] = self.evaluate(self.tab[item])
            else:
                try:
                    if item in "+-*/%()" or isinstance(int(item), int):
                        continue
                except:
                    return None

        try:
            s = Stack()
            for prvok in reversed(k):
                if prvok == '+':
                    s.push(s.pop() + s.pop())
                elif prvok == '-':
                    s.push(s.pop() - s.pop())
                elif prvok == '*':
                    s.push(s.pop() * s.pop())
                elif prvok == '/':
                    s.push(s.pop() // s.pop())
                elif prvok == '%':
                    s.push(s.pop() % s.pop())
                else:
                    s.push(int(prvok))
            return s.pop()
        except:
            return None

    def nadrobne(self, retaz):
        pomoc = ''
        vysledok = []
        co = ''
        prefix = False
        infix = False
        postfix = False
        for i in retaz:
            pomoc += i
        retaz = retaz.replace('+',' + ')
        retaz = retaz.replace('-',' - ')
        retaz = retaz.replace('*',' * ')
        retaz = retaz.replace('/',' / ')
        retaz = retaz.replace('(',' ( ')
        retaz = retaz.replace(')',' ) ')
        retaz = retaz.replace('%',' % ')
        vysledok = retaz.split()
        if vysledok[-1] == '+' or vysledok[-1] == '-' or vysledok[-1] == '*' or vysledok[-1] == '/' or vysledok[-1] == '%':
            try:
                if vysledok.index('(') == -1:
                    pass
            except ValueError:
                postfix = True
        elif len(vysledok) >=2 and ((vysledok[-1] != '+' and vysledok[-1] != '-' and vysledok[-1] != '*' and vysledok[-1] != '/' and vysledok[-1] != '%') and (vysledok[-2] != '%' and vysledok[-2] != '+' and vysledok[-2] != '-' and vysledok[-2] != '*' and vysledok[-2] != '/')):
            try:
                if vysledok.index('(') == -1:
                    pass
            except ValueError:
                prefix = True
        else:
            infix = True

        if prefix:
            return vysledok
        elif postfix:
            vrat = []
            pom = [i for i in vysledok]
            for i in range(len(pom[1:])):
                if i % 2 == 1:
                    pom[i], pom [i+1] = pom[i+1], pom[i]
            infix = True
            vysledok = pom

        if infix:
            pomocnik = Stack()
            navrat = []
            for i in vysledok[::-1]:
                if i !='%' and i != '+' and i != '-' and i != '*' and i != '/' and i != '(' and i != ')':
                    navrat.append(i)
                elif i == ')':
                    pomocnik.push(i)
                elif i == '(':
                    while pomocnik.top() != ')':
                        navrat.append(pomocnik.pop())
                    pomocnik.pop()
                else:
                    if pomocnik.is_empty() == True:
                        pomocnik.push(i)
                    else:
                        if i == '+' or i == '-':
                            while not pomocnik.is_empty():
                                if pomocnik.top() == '*' or pomocnik.top() == '/' or pomocnik.top() == '%':
                                    navrat.append(pomocnik.pop())
                                else:
                                    break
                            pomocnik.push(i)

                        elif i == '*' or i == '/' or i == '%':
                            pomocnik.push(i)
            while not pomocnik.is_empty():
                navrat.append(pomocnik.pop())
            return navrat[::-1]


def pocitaj_prefix(vyraz):
    s = Stack()
    for prvok in reversed(vyraz):
        if prvok == '+':
            s.push(s.pop() + s.pop())
        elif prvok == '-':
            s.push(s.pop() - s.pop())
        elif prvok == '*':
            s.push(s.pop() * s.pop())
        elif prvok == '/':
            s.push(s.pop() // s.pop())
        elif prvok == '%':
            s.push(s.pop() % s.pop())
        else:
            s.push(int(prvok))
    return s.pop()



e = Expression()
print(e.to_prefix('9 9 * 5 %'))
print(e.evaluate('17'))
print(e.evaluate('22/7*3'))