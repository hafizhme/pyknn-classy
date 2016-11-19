from sys import argv

class Knn(object):
    """docstring for Knn."""
    def __init__(self, k):
        super(Knn, self).__init__()
        self.k = k
        self.data = []
        self.test = []
        self.accuracy = 0

    def readdt(self, filedir):
        f = open(filedir, "r")
        f.readline()
        a = f.readline()
        n = 0
        while ( a is not "" ):
            n += 1
            if (n <= 70000):
                self.data.append([float(x) for x in a.replace("\n", "").split(',')])
            else:
                self.test.append([float(x) for x in a.replace("\n", "").split(',')])
            a = f.readline()

    def testing(self):


        i = 0
        while (i < 30000):
            check = self.test[i]


            # Calculate the distance between the query instance and all the training samples
            # print("  Step 1")
            distance = []
            j = 0
            while (j < 70000):
                train = self.data[j]
                k = 0
                distance.append(0)
                while (k < 11):
                    distance[j] += (train[k]-check[k])*(train[k]-check[k])
                    k += 1
                # print(j, distance[j])
                j += 1

            # Find the k first minimum distance
            # print("  Step 2")
            minimum = []
            k = 0
            while (k < self.k):
                j = 1
                mini = 0
                while (j < 70000):
                    if (distance[i] <= distance[mini] ):
                        if (j not in minimum):
                            mini = j
                    j += 1
                minimum.append(mini)
                k += 1

            # Gather classification
            # print("  Step 3")
            yes = 0
            no = 0
            k = 0
            while (k < self.k):
                if (self.data[minimum[k]][11] == 1.0):
                    yes+=1
                else:
                    no+=1
                k += 1

            if (yes >= no):
                if (check[11] == 1.0):
                    self.accuracy += 1
                    # print("  Verdict is TRUE")
                # else:
                    # print("  Verdict is FALSE")
            else:
                if (check[11] == 0.0):
                    self.accuracy += 1
                    # print("  Verdict is TRUE")
                # else:
                    # print("  Verdict is FALSE")
            print("Data Testing ", i, "/", 29999, "| progress :", ((i+1)/30000)*100, "%")
            print(" ", check[11])
            print("  yes : no =", yes, ":", no)
            print("  Current accuracy :", (self.accuracy / (i+1))*100, "%")
            print()
            i += 1

        print("Your accuracy :", (self.accuracy / 30000)*100, "%")
