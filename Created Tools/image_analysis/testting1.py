import multiprocessing, time

que = multiprocessing.Queue()


def puttoqueue(q1):
    while (True):
        for i in range(0,10):
            q1.put(i)
            print("on put")




def getfromqueue1(q1):
    while (True):
        print("on get 1")
        print(q1.get())

def getfromqueue2(q1):
    while (True):
        print("on get 2")
        print(q1.get())


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=puttoqueue,args=(que,))
    p1.start()

    p2 = multiprocessing.Process(target=getfromqueue1,args=(que,) )

    p2.start()

    p3 = multiprocessing.Process(target=getfromqueue2, args=(que,))

    p3.start()
