import cheat_cookie

cj = cheat_cookie.load()

f = open('mass_dump.txt', 'w')
f.write(str(cj))
f.close()