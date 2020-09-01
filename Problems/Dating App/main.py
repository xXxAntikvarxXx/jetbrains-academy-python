def select_dates(potential_dates):
    names = [
        date.get("name")
        for date in potential_dates
        if (
            date.get('age', 0) > 30
            and "art" in date.get('hobbies', [])
            and date.get('city') == 'Berlin'
        )
    ]
    return ", ".join(names)
