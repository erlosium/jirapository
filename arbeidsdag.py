def arbeidsdag (timer, minutter, prosent, sommertid):

    if sommertid == True:
        full_dag = (7*60)+15
    else:
        full_dag = (7*60)+30

    prosent = prosent/100
    login = ((timer*60) + minutter) * prosent
    total = str(round(((login + full_dag) /60),2))
    #total = str(round(total,2))
    t, m  = [int(s) for s in total.split('.')]
    m = round(m/1.66666667)
    print(f'{t}:{m}')

arbeidsdag(8, 23, 50, False)
