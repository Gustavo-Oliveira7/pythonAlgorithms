def is_anagram(first_string, second_string):
    firts_str = first_string.lower()
    second_str = second_string.lower()

    if len(firts_str) != len(second_str):
        return is_not_anagram(first_string, second_string)
    if len(firts_str) & len(second_str) == 0:
        return is_not_anagram(first_string, second_string)
    
    for x in firts_str:
        if x in second_str:
            return (my_sort(firts_str), my_sort(second_str), True)
        else:
            return is_not_anagram(first_string, second_string)


def is_not_anagram(first_string, second_string):
    first = my_sort(first_string)
    second = my_sort(second_string)
    return (first, second , False)

def my_sort(string):
    str_list = list(string)
    for x in range(len(str_list)):
        min = x
        for y in range (x + 1, len(str_list)):
            if str_list[y] < str_list[min]:
                min = y

        str_list[x], str_list[min] = str_list[min], str_list[x]
    str = ''.join(str_list)
    return str

if __name__ == '__main__':
    print(is_anagram('ior', 'ory'))