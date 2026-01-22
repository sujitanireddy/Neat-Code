#Travelling Salesman Problem

def tsp(cities, paths, dist):

    possible_paths = permutations(cities)

    for possible_path in possible_paths:

        total_distance = 0

        for i in range(len(possible_path) - 1):

            total_distance += paths[possible_path[i]][possible_path[i+1]]

        if total_distance < dist:
            return True

    return False

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

#given a path function to verify (Runs in polynomial time)
def verify_tsp(paths, dist, actual_path):

    distance = 0
    
    for i in range(len(actual_path) - 2):

        distance += paths[actual_path[i]][actual_path[i+1]]

    if distance < dist:

        return True

    else:

        return False
