# https://contest.yandex.ru/contest/27794/problems/J/

# Рассмотрим точки и матрицу расстояний между ними.
# Матрица получится квадратной и симметричной и можно было бы её как-то эффективнее хранить в памяти,
# но для удобства решения и наглядности будем хранить её именно как массив массивов.
# Будем хранить расстояние в квадрате, потому что нам необязательно честно считать расстояние и извлекать корень,
# на решение задачи это не влияет, а вычислений меньше.
# Нас интересуют случаи, когда есть одинаковые значения в одной строке –
# это означает, что от вершины, у которой значение в матрице 0 до двух других вершин одинаковое расстояние,
# а значит имеем кандидата в равнобедренный треугольник. Остаётся только проверить,
# что такой треугольник может существовать, что три его вершины не лежат на одной прямой.
# Равнобедренный треугольник невырожденный, если сумма длин его равных сторон больше длины третьей стороны.
# Эта проверка будет выглядеть так:
# 2 * длина_равной_стороны > длина_третьей_стороны
# Через квадраты расстояний:
# 4 * длина_равной_стороны^2 > длина_третьей_стороны^2
# Пример:
# ________|_(0, 0)_|_(1, 1)_|_(0, 1)_|_(1, 0)_|_(0, -1)
# (0, 0)  | 0      | 2      | 1      | 1      | 1
# (1, 1)  | 2      | 0      | 1      | 1      | 5
# (0, 1)  | 1      | 1      | 0      | 2      | 4
# (1, 0)  | 1      | 1      | 2      | 0      | 2
# (0, -1) | 1      | 5      | 4      | 2      | 0
# Идём по строкам сверху вниз, рассматриваем каждую пару одинаковых значений,
# если такая пара вместе с вершиной 0 образует невырожденный треугольник,
# то увеличиваем счётчик равнобедренных треугольников.
# В примере получается, что кандидатов 7, но один является вырожденным ((0, 0) (0, 1) (0, -1)), поэтому ответ 6.
from collections import defaultdict


def get_squared_distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def triangles(points):
    matrix = [[0] * len(points) for _ in range(len(points))]
    for first_idx, first_point in enumerate(points):
        for second_idx in range(first_idx + 1, len(points)):
            squared_distance = get_squared_distance(first_point, points[second_idx])
            matrix[first_idx][second_idx] = squared_distance
            matrix[second_idx][first_idx] = squared_distance

    triangles_count = 0
    for row in matrix:
        points_by_distances = defaultdict(list)
        for point_idx, squared_distance in enumerate(row):
            point = points[point_idx]
            for previous_point in points_by_distances[squared_distance]:
                if 4 * squared_distance > get_squared_distance(previous_point, point):
                    triangles_count += 1
            points_by_distances[squared_distance].append(point)

    return triangles_count


assert triangles([(0, 0), (2, 2), (-2, 2)]) == 1
assert triangles([(0, 0), (2, 2), (-2, -2)]) == 0
assert triangles([(0, 0), (1, 1), (1, 0), (0, 1)]) == 4
assert triangles([(0, 0), (1, 1), (0, 1), (1, 0), (0, -1)]) == 6


def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(triangles(points))


if __name__ == '__main__':
    main()
