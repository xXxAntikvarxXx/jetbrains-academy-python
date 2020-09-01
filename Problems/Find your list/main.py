def find_my_list(lists, my_list):
    for ind, lst in enumerate(lists):
        # Change the next line
        if lst is my_list:
            return ind
    return -1
