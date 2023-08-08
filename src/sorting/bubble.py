

# Define a function named "bubble" that takes one input: a list
def bubbleSort(list: list):
    # This loop goes through each item in the list. 
    # The variable "i" is the current index, starting from 0 and going up to the length of the list.
    for i in range(len(list)):
        
        # This nested loop also goes through each item in the list, but only up to the second last item. 
        # That's because we're going to be comparing each item to the item directly after it. 
        # We don't want to go beyond the list's range, so we stop at the second last item.
        for j in range(len(list) - 1 - i):

            # print(list, " - nested for loop")
            
            # Here's where the comparison happens.
            # If the current item is greater than the next item in the list...
            if list[j] > list[j + 1]:

                # print(list, " - if statement")
                
                # ... then we swap the positions of the two items. 
                # This is done using Python's "simultaneous assignment" feature, which lets us swap two variables' values without needing a temporary variable.
                list[j], list[j + 1] = list[j + 1], list[j]

                print(list)

unsorted = [6, 5, 3, 1, 8, 7, 2, 4]
print("unsorted = ", unsorted)
bubbleSort(unsorted)
print("sorted = ", unsorted)