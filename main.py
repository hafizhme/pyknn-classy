from machine import Knn

j = Knn(int(input("k = ")))

j.readdt("/home/hafizhme/Documents/Docs/AI/Data_TuPro_AI_1617/Train.csv")
j.testing()
