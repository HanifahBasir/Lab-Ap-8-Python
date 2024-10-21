def acronym(acronym):
    akronim = ""
    A = acronym.split(" ")
    for i in (A):
        akronim+=i[0]
    print(akronim)
acronym(input())