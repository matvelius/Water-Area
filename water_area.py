heights = [2, 0, 7, 0, 3, 0, 7] #20
# heights = [0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0] #39
##################10 10      9  9         1     
# heights = [0, 1, 0, 1, 0] #1
# heights = [0, 1, 0, 0, 0] #0
# heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3] #48
# heights = [0, 8, 0, 0, 10, 0, 0, 10, 0, 0, 1, 1, 0, 3] #49
# heights = [4, 0, 2, 4, 3, 6, 0, 0, 7] #19
# heights = [0, 0, 0, 0, 0]

def waterArea(heights):
    # print(f"original heights: {heights}")

    if len(heights) == 0:
        return 0

    totalArea = 0
    maxHeight = 0

    # enumerate the original heights
    enumeratedHeights = []
    for index in range(0, len(heights)):
        enumeratedHeights.append((heights[index], index))
    # print(f"enumeratedHeights: {enumeratedHeights}")


    # sorting the heights from largest to smallest
    sortedHeights = sorted(enumeratedHeights, reverse = True)
    # print(f"sortedHeights: {sortedHeights}")

    
    # first, find water area between two highest peaks
    
    # 1) figure out which of the first two peaks is leftmost, and which is rightmost
    leftPeakIndex = sortedHeights[0][1] if sortedHeights[0][1] < sortedHeights[1][1] else sortedHeights[1][1]
    rightPeakIndex = sortedHeights[0][1] if sortedHeights[0][1] > sortedHeights[1][1] else sortedHeights[1][1]
    # print(f"leftPeakIndex: {leftPeakIndex}; rightPeakIndex: {rightPeakIndex}")
    
    # COME BACK TO THIS EDGE CASE!!
    # check if the two highest peaks are right next to each other
    if (leftPeakIndex + 1) != rightPeakIndex:
        # if yes, we need a loop that finds the next set of left & right peaks...
        # or perhaps start with a loop that performs this check every time
        
        # 2) figure out which of the first two peaks is lower (that's our max height!)
        maxHeight = heights[leftPeakIndex] if heights[leftPeakIndex] < heights[rightPeakIndex] else heights[rightPeakIndex]
        # print(f"maxHeight: {maxHeight}")
        
        # 3) figure out water area between the two peaks
        
        totalArea += calculateArea(leftPeakIndex, rightPeakIndex, maxHeight, heights)
        # print(f"totalArea is at first: {totalArea}\n")

    
    
    # iterate through the rest of the heights to find other peaks,
    # check if they are to the left or to the right
    # if so, set the new left & right peak indices
    for (height, index) in sortedHeights[2:]:
        
        #if new peak is left of leftmost peak
        if index < leftPeakIndex:
            # print(f"index({index}) < leftPeakIndex({leftPeakIndex})")
            maxHeight = height
            newRightPeakIndex = leftPeakIndex
            leftPeakIndex = index
            
            totalArea += calculateArea(leftPeakIndex, newRightPeakIndex, maxHeight, heights)
            
            # print(f"leftPeakIndex: {leftPeakIndex}; newRightPeakIndex: {newRightPeakIndex}")
            # print(f"maxHeight is now: {maxHeight}")
            # print(f"totalArea is now: {totalArea}\n")
            
            continue
        
        # if new peak is right of rightmost peak
        elif index > rightPeakIndex:
            # print(f"index({index}) > rightPeakIndex({rightPeakIndex})")
            maxHeight = height
            newLeftPeakIndex = rightPeakIndex
            rightPeakIndex = index
            
            totalArea += calculateArea(newLeftPeakIndex, rightPeakIndex, maxHeight, heights)
            
            # print(f"newLeftPeakIndex: {newLeftPeakIndex}; rightPeakIndex: {rightPeakIndex}")
            # print(f"maxHeight is now: {maxHeight}")
            # print(f"totalArea is now: {totalArea}\n")
            
            continue
        
        # check if the two new peaks are adjacent
        if (leftPeakIndex + 1) == rightPeakIndex:
            # print("(leftPeakIndex + 1) == rightPeakIndex")
            continue

    
    # print(f"and we're done, totalArea = {totalArea}")
    return totalArea
    

def calculateArea(leftIndex, rightIndex, maxHeight, heights):
    if leftIndex < rightIndex and (leftIndex + 1) <= (rightIndex - 1):
        total = 0

        for index in range(leftIndex + 1, rightIndex):
            if (maxHeight - heights[index]) >= 0:
                total += maxHeight - heights[index]
                # print(f"adding {maxHeight - heights[index]} to totalArea")

        return total 

    # print("returning 0")
    return 0
    

result = waterArea(heights)
print(result)
