def is_anagram(first_string, second_string):
    firts_str = first_string.lower()
    second_str = second_string.lower()

    if len(firts_str) != len(second_str):
        return is_not_anagram(first_string, second_string)
    if len(firts_str) & len(second_str) == 0:
        return is_not_anagram(first_string, second_string)

    for x in firts_str:
        if x not in second_str:
            return is_not_anagram(first_string, second_string)
    return (my_sort(firts_str), my_sort(second_str), True)


def is_not_anagram(first_string, second_string):
    first = my_sort(first_string)
    second = my_sort(second_string)
    return (first, second, False)


def my_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = my_sort(string[:mid])
    right = my_sort(string[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    x = y = 0

    while x < len(left) and y < len(right):
        if left[x] < right[y]:
            result.append(left[x])
            x += 1
        else:
            result.append(right[y])
            y += 1

    result.extend(left[x:])
    result.extend(right[y:])
    return ''.join(result)
