def unique_domains(emails):
    listy = []
    for e in emails:
        findat = e.find('@')
        frag = e[findat+1:]
        if frag not in listy:
            listy.append(frag)
    return listy

unique_domains(['bcm822@gmail.com','cipher813@gmail.com','bm@cipherlab.co'])
