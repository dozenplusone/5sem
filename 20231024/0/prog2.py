def walk2d():
    pt = 0, 0
    while upd := (yield pt):
        pt = pt[0] + upd[0], pt[1] + upd[1]

send = None
walker = walk2d()
while send != 0:
    pt = walker.send(send)
    print(pt)
    send = eval(input())
