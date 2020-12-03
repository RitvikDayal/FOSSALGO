def linearsearch(arr, x):
    '''
    We will traverse through out the list and will try to 
    compare every element one by one.
    '''
    for i,element in enumerate(arr):
        if x == element:
            return i
        else:
            return -1

def main():
    arr = [2, 3, 0, 4]
    result = linearsearch(arr, 0)
    
if __name__ == '__main__':
    main()