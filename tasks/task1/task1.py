def slice_less(my_list, lesser):
    for i in sorted(my_list):
        if i <= lesser:
            my_list.remove(i)
    return sorted(my_list, reverse=True)


print(slice_less([1, 2, 3, 4, 5, 6, 10, 2, 4, 5, 12], 2))


def slice_less_filter(my_list, lesser):
    return sorted(list(filter(lambda x: x > lesser, my_list)), reverse=True)


print(slice_less_filter([1, 2, 3, 4, 5, 6, 10, 2, 4, 5, 12], 2))
