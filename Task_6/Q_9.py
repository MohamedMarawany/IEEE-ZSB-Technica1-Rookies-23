class DetectSquares:

    def __init__(self):
        self.__x_to_ys = collections.defaultdict(set)
        self.__point_counts = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.__x_to_ys[point[0]].add(point[1])
        self.__point_counts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        result = 0
        for y in self.__x_to_ys[point[0]]:
            if y == point[1]:
                continue
            dy = y-point[1]
            result += self.__point_counts[(point[0], y)]*self.__point_counts[(point[0]+dy, point[1])]*self.__point_counts[(point[0]+dy, y)]
            result += self.__point_counts[(point[0], y)]*self.__point_counts[(point[0]-dy, point[1])]*self.__point_counts[(point[0]-dy, y)]
        return result 


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
