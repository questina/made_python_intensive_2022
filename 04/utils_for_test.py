def compare_custom_lists(l1, l2):
    if len(l1) != len(l2):
        return False
    i = 0
    while i < len(l1):
        if l1[i] != l2[i]:
            return False
        i += 1
    return True
