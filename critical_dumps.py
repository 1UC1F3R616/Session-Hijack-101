import cheat_cookie as cc

cj = cc.load()

cjl = [str(x) for x in cj]

tokens = []
for x in cjl:
    if 'token' in x:
        tokens.append(x)
        print(x)

sessions = []
for x in cjl:
    if 'session' in x.lower():
        print(x)
        sessions.append(x)
