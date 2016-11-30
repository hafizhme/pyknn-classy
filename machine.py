from sys import argv
import csv

class Knn(object):
    """docstring for Knn."""
    def __init__(self, k, filedir):
        super(Knn, self).__init__()
        self.k = k
        self.train = []
        self.__rtrain__(filedir)

    def __rtrain__(self, filedir):
        f = open(filedir, "r")

        ftrain = csv.reader(f)
        ftrain = iter(ftrain)

        self.train.append(next(ftrain))
        for row in ftrain:
            ready = []
            row = iter(row)
            ready.append(int(next(row)))
            for i in range(10):
                ready.append(float(next(row)))
            ready.append(int(next(row)))
            self.train.append(ready)

    def rout(self, filedir):
        fin = open(filedir, "r")
        fou = open("Out.csv", "w")

        ftest = csv.reader(fin)
        fout = csv.writer(fou, delimiter=",")

        ftest = iter(ftest)

        header = next(ftest)
        header.append("y")

        fout.writerow(header)

        count=1
        for test in ftest:
            distance = []
            distance.append("not used")


            # Find distance
            j = 1
            while (j < len(self.train)):
                train = self.train[j]
                asd = (train[4]-float(test[4]))**2 + (train[7]-float(test[7]))**2
                distance.append(
                    asd
                )
                j+=1

            # Find k first miminum
            minimum = []
            k = 0
            while (k < self.k):
                i = 1
                idMini = 1
                while (i < len(distance)):
                    if (distance[i] < distance[idMini]):
                        if (i not in minimum):
                            idMini = i
                    i += 1
                minimum.append(idMini)
                k += 1



            # Gather classification
            yes = 0
            no = 0
            k = 0
            while (k < self.k):
                if (self.train[minimum[k]][11] == 1):
                    yes+=1
                else:
                    no+=1
                k += 1

            verdi = 1
            if (yes > no):
                verdi = 1
            else:
                verdi = 0


            # Save
            test.append(verdi)
            fout.writerow(test)
            print()
            print("Done :",count,"/ 10000")
            print("Progress :",count/10000,"%")
            count+=1
