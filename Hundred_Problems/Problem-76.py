# #stats class for statistical operations

# class Stats:
#     def __init__(self,data:list):
#         self.data = data

#     def sum(self) -> float:
#         return sum(self.data)

#     def mean(self) -> float:
#         return sum(self.data) / len(self.data)

#     def min(self) -> float:
#         return min(self.data)

#     def max(self) -> float:
#         return max(self.data)

# data = [10,20,30,40,50]
# stats = Stats(data)
# print(stats.sum())
# print(stats.mean())
# print(stats.min())
# print(stats.max())



class Stats:
    def __init__(self, data: list):
        self.data = data
    
    def sum(self,) -> float:
        return float(sum(self.data))

    def mean(self) -> float:
        return float(sorted(self.data)[len(self.data) // 2])
    
    def min(self) -> float:
        return float(min(self.data))

    def max(self) -> float:
        return float(max(self.data))
    
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    stats = Stats(data)
    print(stats.sum(), stats.mean(), stats.min(), stats.max(), sep = "\n")