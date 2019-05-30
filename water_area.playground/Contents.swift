import UIKit

//let array = [2, 0, 7, 0, 3, 0, 7]
//let array = [0, 1, 0, 1, 0]
let array = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3] //48
//let array = [4, 0, 2, 4, 3, 6, 0, 0, 7] //19
//let array = [0, 0, 0, 0, 0]
print("original array: \(array)")

func waterArea(array: [Int]) -> Int {
    
    var totalArea = 0
    var maxHeight = 0
    
    var enumeratedHeightsArray = [(value: Int, index: Int)]()
    
    // enumerate the original array
    for height in array.enumerated() {
        // store to a new array as (value, index)
        enumeratedHeightsArray.append((value: height.element, index: height.offset))
    }
    print("enumeratedHeightsArray: \(enumeratedHeightsArray)")
    
    // sorting the array from largest to smallest
    var sortedHeightsArray = enumeratedHeightsArray.sorted { $0 > $1 }
    
    print("sortedHeightsArray: \(sortedHeightsArray)")
    
    
    // first, find water area between two highest peaks
    
    // 1) figure out which of the first two peaks is leftmost
    var leftPeakIndex = sortedHeightsArray[0].index < sortedHeightsArray[1].index ? sortedHeightsArray[0].index : sortedHeightsArray[1].index
    var rightPeakIndex = sortedHeightsArray[0].index > sortedHeightsArray[1].index ? sortedHeightsArray[0].index : sortedHeightsArray[1].index
    print("leftPeakIndex: \(leftPeakIndex); rightPeakIndex: \(rightPeakIndex)")
    
    // COME BACK TO THIS EDGE CASE!!
    // check if the two highest peaks are right next to each other
    if (leftPeakIndex + 1) != rightPeakIndex {
        // if yes, we need a loop that finds the next set of left & right peaks...
        // or perhaps start with a loop that performs this check every time
        
        // 2) figure out which of the first two peaks is lower (that's our max height!)
        maxHeight = array[leftPeakIndex] < array[rightPeakIndex] ? array[leftPeakIndex] : array[rightPeakIndex]
        print("maxHeight: \(maxHeight)")
        
        // 3) figure out water area between the two peaks
        totalArea += calculateArea(leftIndex: leftPeakIndex, rightIndex: rightPeakIndex, maxHeight: maxHeight)
        
        print("totalArea is at first: \(totalArea)\n")
    }
    
    
    // iterate through the rest of the array to find other peaks,
    // check if they are to the left or to the right
    // if so, set the new left & right peak indices
    for height in sortedHeightsArray[2...] {
        
        // if new peak is left of leftmost peak
        if height.index < leftPeakIndex {
            
            print("height.index(\(height.index)) < leftPeakIndex(\(leftPeakIndex))")
            maxHeight = height.value
            rightPeakIndex = leftPeakIndex
            leftPeakIndex = height.index
            
            totalArea += calculateArea(leftIndex: leftPeakIndex, rightIndex: rightPeakIndex, maxHeight: maxHeight)
            
            print("leftPeakIndex: \(leftPeakIndex); rightPeakIndex: \(rightPeakIndex)")
            print("maxHeight is now: \(maxHeight)")
            print("totalArea is now: \(totalArea)\n")
            
            continue
        
        // if new peak is right of rightmost peak
        } else if height.index > rightPeakIndex {
            print("height.index(\(height.index)) > rightPeakIndex(\(rightPeakIndex))")
            maxHeight = height.value
            leftPeakIndex = rightPeakIndex
            rightPeakIndex = height.index
            
            totalArea += calculateArea(leftIndex: leftPeakIndex, rightIndex: rightPeakIndex, maxHeight: maxHeight)
            
            print("leftPeakIndex: \(leftPeakIndex); rightPeakIndex: \(rightPeakIndex)")
            print("maxHeight is now: \(maxHeight)")
            print("totalArea is now: \(totalArea)\n")
            
            continue
        }
        
        // check if the two peaks are adjacent
        if (leftPeakIndex + 1) == rightPeakIndex {
            print("(leftPeakIndex + 1) == rightPeakIndex")
            continue
        }
        
    }
    
    print("and we're done, totalArea = \(totalArea)")
    return(totalArea)
    
}


func calculateArea(leftIndex: Int, rightIndex: Int, maxHeight: Int) -> Int {
    
    if leftIndex < rightIndex && (leftIndex + 1) <= (rightIndex - 1) {
        
        var total = 0
        
        for index in (leftIndex + 1)...(rightIndex - 1) {
            total += maxHeight - array[index]
            print("adding \(maxHeight - array[index]) to totalArea")
        }
        
        if total < 0 {
            return(0)
        } else {
            return(total)
        }
    }
    
    print("returning 0")
    return(0)
}

waterArea(array: array)
