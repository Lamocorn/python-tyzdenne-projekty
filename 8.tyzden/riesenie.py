# 8. zadanie: min_sort
# autor: Adam Tomala
# datum: 7.5.2022


class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data, self.next = data, next

    def __init__(self, seq):
        self.front = self.Node(None)

        akt = self.front
        for i in seq:
            akt.next = self.Node(i)
            akt = akt.next

    def progress(self, first, reverse):
        before_first = first
        first = first.next
        before_second = first
        second = first.next
        while second is not None:
            if not reverse and second.data < first.data:
                if first.next == second:
                    pointer = second.next
                    before_first.next = second
                    first.next = pointer
                    second.next = first
                    first = second

                else:
                    pointer1 = second.next
                    pointer2 = first.next
                    before_second.next = first
                    first.next = pointer1
                    second.next = pointer2
                    before_first.next = second
                    second, first = first, second
            
            elif reverse and second.data > first.data:
                if first.next == second:
                    pointer = second.next
                    before_first.next = second

                    first.next = pointer
                    second.next = first
                    first = second


                else:
                    pointer1 = second.next
                    pointer2 = first.next

                    before_second.next = first
                    first.next = pointer1
                    second.next = pointer2
                    before_first.next = second

                    second, first = first, second

            before_second = second
            second = second.next


    def min_sort(self, reverse):
        first = self.front
        while first.next is not None:
            self.progress(first, reverse)
            first = first.next


    def get_list(self):
        vrat = []
        poc = 0
        try:
            kde = self.front.next
            while kde.next is not None or poc == 20:
                vrat.append(kde.data)
                kde = kde.next
                poc += 1
            vrat.append(kde.data)
            return vrat
        except:
            return []

def min_sort(seq, reverse=False):
    ll = LinkedList(seq)
    ll.min_sort(reverse)
    return ll.get_list()
    

if __name__ == '__main__':
    seq = z = (4, 30, 8, 31, 48, 19)
    print(type(seq))
    lst = min_sort(seq)
    print(lst)

    seq = 'kohutik jaraby nechod do zahrady'.split()
    lst = min_sort(seq, reverse=True)
    print(lst)