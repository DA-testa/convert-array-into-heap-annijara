# python3

swaps = []    

# TODO: Create heap and heap sort
# try to achieve  O(n) and not O(n2)      
def build_heap(data):
    
    n = len(data)
    for i in range(n//2, -1, -1):  # parent(i) = floor(i/2)
        heapify(data, i, n)       
    return swaps

def heapify(data, i, n):
 
    min = i  #atrod virsotnes min vērtību
    left = 2 * i + 1 
    right = 2 * i + 2
    
    #sakārto koku augošā secībā 
    if n > left and data[left] < data[min]:
        min = left
    if n > right and data[right] < data[min]:
        min = right
    if min != i: #ja dotā min vērtība nav koka virsotne, tad notiek swapping 
        swaps.append([i, min]) #i, j vērtības
        data[i], data[min] = data[min], data[i] #swapping
        heapify(data, min, n) #veido heap
        
def main():
   
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    modee = input()
    if "I" in modee:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)

    elif "F" in modee:
        num = input()
        if num != "a":
            with open("./tests/"+ num, mode="r") as fails:
                text = fails.read()
                x = text.splitlines()
                n = int(x[0])
                txt = x[1]
                data = (list(map(int, txt.split())))
                assert len(data) == n
                swaps = build_heap(data)
                
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
        
    # input from keyboard
# n = int(input())
# data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
#assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
#swaps = build_heap(data)

    # output all swaps


if __name__ == "__main__":
    main()
