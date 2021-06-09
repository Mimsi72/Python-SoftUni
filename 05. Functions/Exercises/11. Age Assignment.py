def age_assignment(*names, **kwargs):
    ages = {name: 0 for name in names}

    for letter, age in kwargs.items():
        for name in ages:
            if name.startswith(letter):
                ages[name] = age
    return ages


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))