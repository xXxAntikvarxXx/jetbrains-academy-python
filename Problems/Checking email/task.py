def check_email(string: str):
    pos_at = string.find("@")
    return (
        " " not in string
        and "@" in string
        and pos_at > -1
        and string[pos_at + 1:].find(".") > 0
    )
