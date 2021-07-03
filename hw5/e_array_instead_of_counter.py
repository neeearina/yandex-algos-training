# https://contest.yandex.ru/contest/27794/problems/E/

def beautiful_trees(k, colors):
    left = 0
    segment_colors = [0] * (k + 1)
    best_segment = [0, len(colors)]
    distinct_colors_counter = 0

    for right, color in enumerate(colors):
        if not segment_colors[color]:
            distinct_colors_counter += 1
        segment_colors[color] += 1
        if distinct_colors_counter == k:
            while segment_colors[colors[left]] > 1:
                segment_colors[colors[left]] -= 1
                left += 1

            if right - left < best_segment[1] - best_segment[0]:
                best_segment = (left, right)

    # В ответе индексы 1-based, начинаются с единицы
    return best_segment[0] + 1, best_segment[1] + 1


assert beautiful_trees(3, [1, 2, 1, 3, 2]) == (2, 4)
assert beautiful_trees(4, [2, 4, 2, 3, 3, 1]) == (2, 6)
assert beautiful_trees(5, [5, 1, 1, 2, 2, 4, 4, 4, 3, 2, 1, 5]) == (8, 12)


def main():
    n, k = map(int, input().split())
    colors = list(map(int, input().split()))
    print(*beautiful_trees(k, colors))


if __name__ == '__main__':
    main()
