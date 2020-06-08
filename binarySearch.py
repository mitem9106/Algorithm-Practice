#returns the index of x in array if present, else -1
def binarySearch(array, x, low, high):

    #check base case
    if high >= low:
        mid = low + (high-low) // 2

        #if element is present at the middle(interval) index
        if array[mid] == x:
            return mid

        #if element is smaller than mid, then it must be
        #present in the left subarray
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        #Else the element can only be present in the
        #right subarray
        else:
            return binarySearch(array, x, mid + 1, high)
    #Element is not present in the array
    else:
        return -1
    
def main():
    array = [2, 5, 8, 12, 16, 23, 38, 56, 72]

    print("Search: ")
    x = int(input())
    n = len(array)-1

    result = binarySearch(array, x, 0, n)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
