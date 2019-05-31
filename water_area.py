# array = [2, 0, 7, 0, 3, 0, 7] #20
# array = [0, 1, 0, 1, 0] #1
# array = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3] #48
# array = [0, 8, 0, 0, 10, 0, 0, 10, 0, 0, 1, 1, 0, 3] #49
# array = [4, 0, 2, 4, 3, 6, 0, 0, 7] #19
# array = [0, 0, 0, 0, 0]

def waterArea(array):
    print(f"original array: {array}")

    totalArea = 0
    maxHeight = 0

    # enumerate the original array
    enumeratedHeightsArray = []
    for index in range(0, len(array)):
        enumeratedHeightsArray.append((array[index], index))
    print(f"enumeratedHeightsArray: {enumeratedHeightsArray}")


    # sorting the array from largest to smallest
    sortedHeightsArray = sorted(enumeratedHeightsArray, reverse = True)
    print(f"sortedHeightsArray: {sortedHeightsArray}")

    
    # first, find water area between two highest peaks
    # print(f"sortedHeightsArray[0][0]: {sortedHeightsArray[0][0]}")
    # print(f"sortedHeightsArray[0][1]: {sortedHeightsArray[0][1]}")
    # print(f"sortedHeightsArray[1][0]: {sortedHeightsArray[1][0]}")
    # print(f"sortedHeightsArray[1][1]: {sortedHeightsArray[1][1]}")
    # 1) figure out which of the first two peaks is leftmost, and which is rightmost
    leftPeakIndex = sortedHeightsArray[0][1] if sortedHeightsArray[0][1] < sortedHeightsArray[1][1] else sortedHeightsArray[1][1]
    rightPeakIndex = sortedHeightsArray[0][1] if sortedHeightsArray[0][1] > sortedHeightsArray[1][1] else sortedHeightsArray[0][1]
    print(f"leftPeakIndex: {leftPeakIndex}; rightPeakIndex: {rightPeakIndex}")
    
    # COME BACK TO THIS EDGE CASE!!
    # check if the two highest peaks are right next to each other
    if (leftPeakIndex + 1) != rightPeakIndex:
        # if yes, we need a loop that finds the next set of left & right peaks...
        # or perhaps start with a loop that performs this check every time
        
        # 2) figure out which of the first two peaks is lower (that's our max height!)
        maxHeight = array[leftPeakIndex] if array[leftPeakIndex] < array[rightPeakIndex] else array[rightPeakIndex]

        print(f"maxHeight: {maxHeight}")
        
        # 3) figure out water area between the two peaks
        
        totalArea += calculateArea(leftPeakIndex, rightPeakIndex, maxHeight)
        print(f"totalArea is at first: {totalArea}\n")

    
    
        # iterate through the rest of the array to find other peaks,
        # check if they are to the left or to the right
        # if so, set the new left & right peak indices
    for (height, index) in sortedHeightsArray[2:]:
        
        #if new peak is left of leftmost peak
        if index < leftPeakIndex:
            print(f"index({index}) < leftPeakIndex({leftPeakIndex})")
            maxHeight = height
            newRightPeakIndex = leftPeakIndex
            leftPeakIndex = index
            
            totalArea += calculateArea(leftPeakIndex, newRightPeakIndex, maxHeight)
            
            print(f"leftPeakIndex: {leftPeakIndex}; newRightPeakIndex: {newRightPeakIndex}")
            print(f"maxHeight is now: {maxHeight}")
            print(f"totalArea is now: {totalArea}\n")
            
            continue
        
        # if new peak is right of rightmost peak
        elif index > rightPeakIndex:
            print(f"index({index}) > rightPeakIndex({rightPeakIndex})")
            maxHeight = height
            newLeftPeakIndex = rightPeakIndex
            rightPeakIndex = index
            
            totalArea += calculateArea(newLeftPeakIndex, rightPeakIndex, maxHeight)
            
            print(f"newLeftPeakIndex: {newLeftPeakIndex}; rightPeakIndex: {rightPeakIndex}")
            print(f"maxHeight is now: {maxHeight}")
            print(f"totalArea is now: {totalArea}\n")
            
            continue
        
        # check if the two new peaks are adjacent
        if (leftPeakIndex + 1) == rightPeakIndex:
            print("(leftPeakIndex + 1) == rightPeakIndex")
            continue

    
    print(f"and we're done, totalArea = {totalArea}")
    return totalArea
    



# func calculateArea(leftIndex: Int, rightIndex: Int, maxHeight: Int) -> Int {

def calculateArea(leftIndex, rightIndex, maxHeight):
    if leftIndex < rightIndex and (leftIndex + 1) <= (rightIndex - 1):
        total = 0

        for index in range(leftIndex + 1, rightIndex):
            if (maxHeight - array[index]) >= 0:
                total += maxHeight - array[index]
                print(f"adding {maxHeight - array[index]} to totalArea")

        return total 

    print("returning 0")
    return 0
    
#     if leftIndex < rightIndex && (leftIndex + 1) <= (rightIndex - 1) {
        
#         var total = 0
        
#         for index in (leftIndex + 1)...(rightIndex - 1) where (maxHeight - array[index]) >= 0 {
#             total += maxHeight - array[index]
#             print("adding \(maxHeight - array[index]) to totalArea")
#         }
        
#         return total
        
#     }
    
#     print("returning 0")
#     return(0)
# }

waterArea(array)
