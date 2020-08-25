for q in [*open(0)][1:]:
    print(sum(len(o)*-~len(o)//2for o in q[:-1].split("X")))
