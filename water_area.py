heights = [4, 0, 2, 4, 3, 6, 0, 0, 7]

def waterArea(heights):

    indexOfLastValueInArray = len(heights) - 1
    spaceLoIndex = 0
    spaceHiIndex = 0
    totalArea = 0
    maxHeight = 0

    # iterate thru entire array
    for i in range(0, indexOfLastValueInArray):

        # if we found a low pillar to the right of a high pillar
        if heights[i + 1] < heights[i]:
            spaceLoIndex = i + 1

            # iterate through the rest of the array
            for j in range(i + 2, indexOfLastValueInArray):

                # if we found the next high pillar (as high as or higher than the first)
                if heights[j] >= heights[i]:
                    spaceHiIndex = j
                    maxHeight = heights[i]

                    # calculate area
                    currentArea = maxHeight - heights[spaceLoIndex]
                    
                    # iterate through the range of the space to add up the area
                    for index in range(spaceLoIndex + 1, spaceHiIndex):
                        currentArea += maxHeight - heights[index]

                    print(f'adding {currentArea} to total area')
                    # add area in the current space to total area
                    totalArea += currentArea

    print(totalArea)
    return totalArea

# call the function
waterArea(heights)