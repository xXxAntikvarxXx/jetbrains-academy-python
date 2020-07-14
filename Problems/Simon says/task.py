def what_to_do(instructions):
    if (
            instructions.startswith("Simon says")
            or instructions.endswith("Simon says")
    ):
        return "I " + instructions.replace("Simon says", "").strip()
    return "I won't do it!"
