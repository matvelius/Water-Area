# heights = [4, 0, 2, 4, 3, 6, 0, 0, 7]
# heights = [0, 0, 0, 0, 0]
# heights = [0, 1, 0, 1, 0] ## MAKE THIS WORK
# [0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 0]), 39 ## MAKE THIS WORK
heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]  #48
                #8  8  3  8  8      3  3  2  2  3

def waterArea(heights):

    endOfArray = len(heights) - 1
    # print(f"endOfArray index is: {endOfArray}")
    totalArea = 0
    maxL = 0
    maxHeight = 0
    startingIndex = 0

    while startingIndex < endOfArray:
        print(f"STARTING INDEX: {startingIndex}")
        maxR = 0 

        # check if this is the start of a space & set maxL
        if heights[startingIndex + 1] < heights[startingIndex]:

            maxL = heights[startingIndex]

            # look thru the rest of the array to find maxR
            for indexOfMaxR in range(startingIndex + 2, endOfArray + 1):
                print("TEST!")
                # find the largest possible maxR...
                if heights[indexOfMaxR] > maxR:
                    maxR = heights[indexOfMaxR]
                    maxHeight = maxR

                # ... but if it's larger than maxL, set maxHeight to maxL & break out of the loop
                if maxR >= maxL:
                    maxHeight = maxL
                    print(f"found maxR({maxR}) >= maxL({maxL}) at index {indexOfMaxR}")
                    break

                # check if endOfArray has been reached and nothing larger than maxL has been found
                if indexOfMaxR == endOfArray and maxR < maxL:
                    # if so, we're done
                    
                    print(f"indexOfMaxR = {indexOfMaxR}, so EXITING EARLY!")
                    break
                    # return totalArea

            # loop thru current section between maxL and maxR add up totalArea
            for height in heights[startingIndex + 1:indexOfMaxR]:
                totalArea += maxHeight - height
                print(f'totalArea is now: {totalArea}')

            print("finished totalArea calculation loop \n")

            # update index
            # nonlocal index
            startingIndex = indexOfMaxR
            print(f"setting startingIndex to {startingIndex}")
        
        else:
            startingIndex += 1
    
    return totalArea
            

# def waterArea(heights):
#     endOfArray = len(heights) - 1
#     print(f"endOfArray index is: {endOfArray}")
#     totalArea = 0
#     maxL = 0
#     maxR = 0 
#     anotherIndex = 0
#     currentMaxHeight = 0

#     maxL = heights[0]
#     print(f'setting maxL to {maxL}')

#     for index in range(0, endOfArray):

#         # finding the beginning of a space
#         if heights[index + 1] < heights[index]:

#             currentMin = heights[index + 1]
#             print(f'setting currentMin to {currentMin}, at index {index + 1}')
#             anotherIndex = index + 2
#             print(f'anotherIndex is: {anotherIndex}')


#             for yetAnotherIndex in range(anotherIndex, endOfArray):
#                 print(f'yetAnotherIndex is now: {yetAnotherIndex}')

#                 # if a high pillar is never encountered all the way to the end of array
#                 if anotherIndex == endOfArray:
#                     print("reached end of array in the middle of the loop!")
#                     return totalArea

#                 # deal with the situation with multiple gaps in a row
#                 if heights[yetAnotherIndex] <= currentMin:
#                     currentMin = heights[yetAnotherIndex]
#                     print(f'currentMin is now {currentMin}, at index {yetAnotherIndex}')
#                     anotherIndex += 1


#                 if heights[anotherIndex] >= maxL:
#                     maxR = heights[anotherIndex]
#                     print(f'maxR has been set to {maxR} with anotherIndex')
#                     break
#                 elif heights[yetAnotherIndex] >= maxL:
#                     maxR = heights[yetAnotherIndex]
#                     print(f'maxR has been set to {maxR} with yetAnotherIndex')
#                     break

#             # # deal with the situation with multiple gaps in a row (?)
#             # while heights[anotherIndex] <= currentMin:

#             #     # if a high pillar is never encountered until the end of array
#             #     if anotherIndex == endOfArray:
#             #         return totalArea
                
#             #     anotherIndex += 1

#             print(f'anotherIndex is now: {anotherIndex}')
            

#             # maxR = heights[anotherIndex]
#             # for height in heights[index + 1:]:
#             #     if height > maxR:
#             #         maxR = height

            
#             print(f'maxR ended up being {maxR}')

#             if maxL < maxR:
#                 maxHeight = maxL
#             else:
#                 maxHeight = maxR

#             print(f'maxHeight is now: {maxHeight}')
#             print(f'currently, index is {index}')

#             # for finalIndex in range(index + 1, yetAnotherIndex):
#             #     print(f"finalIndex is: {finalIndex}")
#             #     print(f"adding {maxHeight - heights[finalIndex]} to the area")
#             #     totalArea += maxHeight - heights[finalIndex]
                
#             #     # ????
#             #     if finalIndex < endOfArray:
#             #         finalIndex += 1
#             #         totalArea += maxHeight - heights[finalIndex]
                
#             #     print(f'totalArea is now: {totalArea}')
#             #     print("")
#             for height in heights[index + 1:yetAnotherIndex]:
#                 print(f"adding {maxHeight - height} to the area")
#                 totalArea += maxHeight - height
#                 print(f'totalArea is now: {totalArea}')
#                 print("")

#         else:
#             # if index + 1 == endOfArray:
#             #     totalArea += maxL - heights[index]

#             maxL = heights[index + 1]
#             print(f"setting maxL to: {maxL}")

            

#     return totalArea

# def waterArea(heights):

#     indexOfLastValueInArray = len(heights)
#     spaceLoIndex = 0
#     spaceHiIndex = 0
#     totalArea = 0
#     maxHeight = 0

#     i = 0

#     # iterate thru entire array
#     while i < indexOfLastValueInArray:
#         print(f"i is {i}")

#         # make sure we don't go out of bounds
#         if i + 1 >= indexOfLastValueInArray:
#             break

#         # if we found a low pillar to the right of a high pillar
#         if heights[i + 1] < heights[i]:
#             spaceLoIndex = i + 1
#             print(f"spaceLoIndex: {spaceLoIndex}")

#             currentArea = 0

#             x = 1
#             # iterate through the rest of the array
#             for j in range(i + 2, indexOfLastValueInArray):

#                 print(f'iteration #{x} thru "rest of array" for loop')
#                 x += 1

#                 # if we found the next high pillar (higher than on at spaceLoIndex)
#                 if heights[j] > heights[spaceLoIndex]:
#                     spaceHiIndex = j
#                     # maxHeight = heights[i]
#                     print(f"spaceHiIndex: {spaceHiIndex}")
#                     print(f"maxHeight: {maxHeight}")

#                     # ???
#                     # spaceLoIndex = i + 1
#                     print(f"spaceLoIndex: {spaceLoIndex}")

#                     # look for the next high pillar (as high as or higher than the one we started with)
#                     for k in range(j + 1, indexOfLastValueInArray):
                        
#                         if heights[k] >= heights[i]:
#                             # does this update the nonlocal variable??
#                             spaceHiIndex = k
#                             maxHeight = heights[i]
                    
#                     print(f"spaceHiIndex is still/now: {spaceHiIndex}")

#                     if spaceHiIndex == j:
#                         maxHeight = heights[j]
#                         # but what if we have 2 low spaces in a row???
#                         # calculate area
#                         currentArea += maxHeight - heights[spaceLoIndex]
#                     else:
#                         # iterate through the range of the space to add up the area
#                         for index in range(spaceLoIndex + 1, spaceHiIndex):
#                             currentArea += maxHeight - heights[index]

#                     print(f'ADDING {currentArea} TO TOTAL AREA')
#                     print("")
#                     # add area in the current space to total area
#                     totalArea += currentArea

#                     # look for the next space
#                     # nonlocal i
#                     i = spaceHiIndex
#                     print(f'setting i to: {i}')
                    
#             print("exited the for loop")
        
#         i += 1


#     print(totalArea)
#     return totalArea

# call the function
result = waterArea(heights)
print(result)