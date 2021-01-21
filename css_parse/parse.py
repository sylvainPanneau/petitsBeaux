file = open("/home/ouicmoi/Documents/css_parse/parse.txt", "r")
words = file.read()

index = open("/home/ouicmoi/Documents/iut/condoc/projet/secoursPOP_iutv/index.html", "r").read()
aide = open("/home/ouicmoi/Documents/iut/condoc/projet/secoursPOP_iutv/aide.html", "r").read()
benevole = open("/home/ouicmoi/Documents/iut/condoc/projet/secoursPOP_iutv/bénévole.html", "r").read()
don = open("/home/ouicmoi/Documents/iut/condoc/projet/secoursPOP_iutv/don.html", "r").read()
missions = open("/home/ouicmoi/Documents/iut/condoc/projet/secoursPOP_iutv/missions.html", "r").read()

def file_to_tab(words):
    i = 0
    tab = []
    s = ""
    j = 0
    while i < len(words):
        s = ""
        while j < len(words) and (words[j]!="," and words[j] != " " and words[j] != "\n"):
            s+=words[j]
            j+=1
        while j < len(words) and (words[j]=="," or words[j] == " " or words[j] == "\n"):
            j+=1
        if s != "":
            tab.append(s)
        i+=1
    tab.append(s)
    return tab

tab = file_to_tab(words)

def words_not_in_pages(tab, p1, p2, p3, p4, p5):
    t = []
    i = 0
    while i < len(tab):
        x = "<"+tab[i]
        if x not in p1 and x not in p2 and x not in p3 and x not in p4 and x not in p5:
            t.append(tab[i])
        i+=1
    return t

x = words_not_in_pages(tab, index, aide, benevole, don, missions)
print(x)