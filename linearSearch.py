def linearSearch(array, x):
    for i in range(len(array)):
        if int(array[i]) == int(x):
             return i
    return -1

def main():
    array = [88, 40, 10, 150, 34, 55, 20, 111]

    print("Search for: ")
    x = int(input())
    result = linearSearch(array, x)
    if result == -1:
        print("Element x is not present in array[].")
    else:
        print("Element x is present at index %s" %(result))
