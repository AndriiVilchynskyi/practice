def get_unique_items(ls: list) -> list:
    # write code here
    unique_ls = list(set(ls))
    if len(unique_ls) == 0:
        return []
    else:
        return unique_ls
