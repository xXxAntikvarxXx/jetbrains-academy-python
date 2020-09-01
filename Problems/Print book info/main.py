def print_book_info(title, author=None, year=None):
    #  Write your code here
    msg = f"\"{title}\""
    if author is not None or year is not None:
        msg = f"{msg} was written"
        if author is not None:
            msg = f"{msg} by {author}"
        if year is not None:
            msg = f"{msg} in {year}"
    print(msg)
