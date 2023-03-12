# python3

swaps = []

def heapify(i, n, data):
    min = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if n > left and data[left] < data[min]:
        min = left
    if n > right and data[right] < data[min]:
        min = right
    if min != i:
        swaps.append([i, min])
        data[i], data[min] = data[min], data[i]
        heapify(min, n, data)
        
        
def build_heap(data):
    
    n = len(data)
    for i in range(n//2, -1, -1):
        heapify(i, n, data)
    # TODO: Create heap and heap sort
    # try to achieve  O(n) and not O(n2)
    return swaps
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
            with open("./test/"+ num, mode="r") as fails:
                text = fails.read()
                x = text.splitlines()
                n = int(x[0])
                txt = x[1]
                data = (list(map(int, txt.split())))
                assert len(data) == n
                swaps = build_heap(data)



    # input from keyboard
# n = int(input())
# data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
#assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
#swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
