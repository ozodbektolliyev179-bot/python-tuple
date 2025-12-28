people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

def find_oldest(people: list[tuple[str, int]]) -> tuple[str, int] | None:
    if not people:
        return None
    oldest_person = people[0]
    for person in people:
        if person[1] > oldest_person[1]:
            oldest_person = person
    return oldest_person
print(find_oldest(people)) 