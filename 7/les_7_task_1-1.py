import random


class SortList(list):
    def __init__(self, *args, **kwargs):
        self.swap_pointer = None
        super(SortList, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '(' + ' '.join(
            ['\033[1m' + str(value) if i == self.swap_pointer - 1
             else str(value) + '\033[0m' if i == self.swap_pointer
            else str(value) for i, value in enumerate(self)]) + ')'


def swap(lst: SortList, i: int, j: int) -> None:
    buff = lst[i]
    lst[i] = lst[j]
    lst[j] = buff


def bubble_sort(lst: SortList, show_wasted: bool = False) -> None:
    length = len(lst)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, length):
            if lst[i - 1] < lst[i]:
                if isinstance(lst, SortList):
                    lst.swap_pointer = i
                    print(lst, end='')
                swap(lst, i - 1, i)
                if isinstance(lst, SortList):
                    print(' ->', lst)
                swapped = True
            else:
                if show_wasted:
                    lst.swap_pointer = None
                    print('\033[1m' + str(lst), '->', str(lst) + '\033[0m')
        length -= 1


def bubble_sort_improved(lst: SortList, show_wasted: bool = False) -> None:
    length = len(lst)
    while length > 1:
        new_length = 1
        for i in range(1, length):
            if lst[i - 1] > lst[i]:
                if isinstance(lst, SortList):
                    lst.swap_pointer = i
                    print(lst, end='')
                swap(lst, i - 1, i)
                if isinstance(lst, SortList):
                    print(' ->', lst)
                new_length = i
            else:
                if show_wasted:
                    lst.swap_pointer = None
                    print('\033[1m' + str(lst), '->', str(lst) + '\033[0m')
        length = new_length


if __name__ == '__main__':
    array = random.sample(range(-100, 100), 5)
    bubble_array = SortList(array)
    bubble_sort(bubble_array)
    '''
    (-49 -9 -82 88 51) -> (-9 -49 -82 88 51)
    (-9 -49 -82 88 51) -> (-9 -49 88 -82 51)
    (-9 -49 88 -82 51) -> (-9 -49 88 51 -82)
    (-9 -49 88 51 -82) -> (-9 88 -49 51 -82)
    (-9 88 -49 51 -82) -> (-9 88 51 -49 -82)
    (-9 88 51 -49 -82) -> (88 -9 51 -49 -82)
    (88 -9 51 -49 -82) -> (88 51 -9 -49 -82)
    '''
