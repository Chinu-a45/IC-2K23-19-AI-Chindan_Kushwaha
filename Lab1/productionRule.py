def production_system(temperature, cough):

    if temperature > 38 and cough:
        return "Possible infection"

    elif temperature > 38:
        return "Fever"

    elif cough:
        return "Possible respiratory problem"

    else:
        return "No significant symptoms"


print(production_system(39, True))