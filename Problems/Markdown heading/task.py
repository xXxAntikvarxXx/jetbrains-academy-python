def heading(msg, level=1):
    if level < 1:
        level = 1
    elif level > 6:
        level = 6
    return f"{'#' * level} {msg}"
