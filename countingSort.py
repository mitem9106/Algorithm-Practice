#Time complexity: O(n+k) where n is the number of elements in input array
#and k is the range of the input
#Auxiliary Space: O(n+k)

#The main problem with this counting sort is that we cannot sort the elements
#if we have negative numbers in it. Getting around that requires storing the
#count of the minimum element at zero index.git 


def main():
    print("Input a string: ")
    data = str(input())
    
    print("%s" %("".join(countingSort(data))))

def countingSort(data):
    #The output character array containing the sorted data
    output = [0 for i in range(256)]

    #Count array to store count of individual characters
    count = [0 for i in range(256)]

    #For storing the resulting answer
    answer = ["" for _ in data]

    #store the count of each character
    for i in data:
        count[ord(i)] += 1

    #Change count[i] so that count[i] now contains actual
    #position of this character in the output array
    for i in range(256):
        count[i] += count[i-1]

    #Build the output character array
    for i in range(len(data)):
        output[count[ord(data[i])]-1] = data[i]
        count[ord(data[i])] -= 1

    #Copy the output array to the answer array,
    #now sorted
    for i in range(len(data)):
        answer[i] = output[i]
    return answer
