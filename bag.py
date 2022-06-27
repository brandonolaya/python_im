def bag (size_bag, weight, values, n):
    
    
    if n == 0 or size_bag == 0:
        return 0

    if weight[n - 1] > size_bag:
        return bag(size_bag, weight, values, n - 1)

    return max(values[n - 1] + bag(size_bag - weight[n - 1], weight, values, n - 1),
                bag(size_bag, weight, values, n - 1))


if __name__ == '__main__':
    values = [60, 100, 120]
    weight = [10, 20, 30]
    size_bag = 60
    n = len(values)

    result = bag(size_bag, weight,values, n)
    print(result)