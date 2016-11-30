from machine import Knn

j = Knn(
    int(input("k = ")),
    "/home/hafizhme/Documents/Docs/AI/Data_TuPro_AI_1617/Train.csv"
    )
j.rout("/home/hafizhme/Documents/Docs/AI/Data_TuPro_AI_1617/Test.csv")
# j.testing()
# j.running("/home/hafizhme/Documents/Docs/AI/Data_TuPro_AI_1617/Train.csv")
