def linearis_kereses(also, felso):
    i = also
    van = False
    while i <= felso and not (i % 10 == 0):
        i += 1
    van = i <= felso
    if van:
        print(f"Van: {i}")
    else:
        print("nincs")


linearis_kereses(42, 67)

