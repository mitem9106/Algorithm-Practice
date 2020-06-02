def binarySearch(array, x, r, n):
    interval = int(n/2)
    if array[interval] == x:
        return interval
    if array[interval] > x
def main():
    array = [2, 5, 8, 12, 16, 23, 38, 56, 72]

    print("Search: ")
    x = int(input())
    n = len(array)

    binarySearch(array, x, n)
