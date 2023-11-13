#1-)
def flatten_list(lst):
    result = []

    for item in lst:
        if type(item) == list:
            # Eğer eleman bir liste ise, elemanları düzleştir ve sonuca ekle
            for subitem in item:
                result.append(subitem)
        else:
            # Eğer eleman bir liste değilse, direkt sonuca ekle
            result.append(item)

    return result


#2-)
def reverse_nested_list(lst):
    reversed_result = []

    for item in reversed(lst):
        if isinstance(item, list):
            # Eğer eleman bir liste ise, içindekileri de tersine çevirerek sonuca ekle
            reversed_result.append(reverse_nested_list(item))
        else:
            # Eğer eleman bir liste değilse, direkt olarak sonuca ekle
            reversed_result.append(item)

    return reversed_result