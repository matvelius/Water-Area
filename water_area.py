heights = [4, 0, 2, 4, 3, 6, 0, 0, 7]

def waterArea(heights):

    indexOfLastValueInArray = len(heights)
    spaceLoIndex = 0
    spaceHiIndex = 0
    totalArea = 0
    maxHeight = 0

    i = 0

    # iterate thru entire array
    while i < indexOfLastValueInArray:
        print(f"i is {i}")

        # if we found a low pillar to the right of a high pillar
        if heights[i + 1] < heights[i]:
            spaceLoIndex = i + 1
            print(f"spaceLoIndex: {spaceLoIndex}")

            x = 1
            # iterate through the rest of the array
            for j in range(i + 2, indexOfLastValueInArray):

                print(f'iteration #{x} thru "rest of array" for loop')
                x += 1

                # if we found the next high pillar (as high as or higher than the first)
                if heights[j] >= heights[i]:
                    spaceHiIndex = j
                    maxHeight = heights[i]
                    print(f"spaceHiIndex: {spaceHiIndex}")
                    print(f"maxHeight: {maxHeight}")

                    spaceLoIndex = i + 1
                    print(f"spaceLoIndex: {spaceLoIndex}")
                    # calculate area
                    currentArea = maxHeight - heights[spaceLoIndex]

                    # iterate through the range of the space to add up the area
                    for index in range(spaceLoIndex + 1, spaceHiIndex):
                        currentArea += maxHeight - heights[index]

                    print(f'ADDING {currentArea} TO TOTAL AREA')
                    print("")
                    # add area in the current space to total area
                    totalArea += currentArea

                    # look for the next space
                    # nonlocal i
                    i = spaceHiIndex
                    print(f'setting i to: {i}')
                    
            print("exited the for loop")
        
        i += 1


    print(totalArea)
    return totalArea

# call the function
waterArea(heights)