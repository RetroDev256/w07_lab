# 1. Name:
#      Eric Petersen
#
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
#
# 3. Assignment Description:
#      The program is meant to sort a list of integers, with the assignment
#      purpose being implementation of the functions and an automation driver
#      to test the code, with the test cases from last week.
#
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this week was thinking of good test cases for the
#      sort function. Everything else that may have been difficult was
#      completed previously.
#  
# 5. How long did it take for you to complete the assignment?
#     This assignment took about 45 minutes to complete, including recording
#     the video.

def mergeRanges(
    source: list[int], dest: list[int], start: int, split: int, end: int
) -> None:
    ''' Given two consecutive sorted ranges in source, this function merges
    the two ranges into dest to produce one larger sorted range. '''
    
    assert 0 <= len(source) == len(dest)
    assert start <= split <= end <= len(source)

    # If the length of one of the ranges is zero, just copy to dest
    if split == start or split == end:
        dest[start:end] = source[start:end]
        return
    
    left: int = start # index into left range of source
    right: int = split # index into right range of source
    index: int = start # index into dest
    
    # Merge the two ranges until one is exhausted
    while left < split and right < end:
        # Using <= here for a stable sort
        if source[left] <= source[right]:
            dest[index] = source[left]
            left += 1
        else:
            dest[index] = source[right]
            right += 1
        index += 1
    
    # Copy any remaining elements from the right range
    while right < end:
        dest[index] = source[right]
        index += 1
        right += 1
    
    # Copy any remaining elements from the left range
    while left < split:
        dest[index] = source[left]
        index += 1
        left += 1

def inOrderAt(arr: list[int], start: int) -> int:
    ''' Returns the length of the in-order sublist at the start index '''
    assert 0 <= start <= len(arr)

    for index in range(start + 1, len(arr)):
        if arr[index] < arr[index - 1]:
            return index - start
    return len(arr) - start

def sort(source: list[int], dest: list[int]) -> None:
    assert len(source) == len(dest)
    
    while True:
        # End condition - the list is already sorted
        if inOrderAt(source, 0) == len(source):
            dest[:] = source
            return
        
        # Reduction step - merge consecutive pairs of in-order segments
        start = 0
        while start < len(source):
            split = start + inOrderAt(source, start)
            end = split + inOrderAt(source, split)
            mergeRanges(source, dest, start, split, end)
            start = end
        
        # Swap references to source and dest for next iteration
        source, dest = dest, source

def test_mergeRanges() -> None:
    tests = [
        ([1,2,3,4,5], [0,0,0,0,0], 0, 0,   3,         [1,2,3,0,0]),
        ([5,4,3,2,1], [0,0,0,0,0], 0, 1,   2,         [4,5,0,0,0]),
        ([3,4,5,1,2], [0,0,0,0,0], 0, 3,   5,         [1,2,3,4,5]),
        ([1,2,3,4,5],          [], 0, 0,   0,   "assertion error"),
        ([1,2,3,4,5], [0,0,0,0,0], 0, 0, 100,   "assertion error"),
        (         [], [0,0,0,0,0], 0, 0,   0,   "assertion error"),
        ([1,2,3,4,5], [0,0,0,0,0], 0, 0,   0,         [0,0,0,0,0]),
        (         [],          [], 0, 0,   0,                  []),
        (        [1],         [0], 0, 0,   1,                 [1]),
    ]
    
    for (index, test) in enumerate(tests):
        print(f"TEST mergeRanges() #{index}... ", end="")
        source, result, start, split, end, expected = test
        try:
            mergeRanges(source, result, start, split, end)
            if result == expected:
                print("PASS")
            else:
                print("FAIL !!!")
        except AssertionError:
            if expected == "assertion error":
                print("PASS")
            else:
                print("FAIL !!!")

def test_inOrderAt() -> None:
    tests = [
        ([1,2,3,4,5],   0,                 5),
        ([1,2,3,4,5],   3,                 2),
        ([1,2,5,0,0],   0,                 3),
        ([1,2,3,4,5], -10, "assertion error"),
        ([1,2,3,4,5],  10, "assertion error"),
        ([1,2,3,4,5],   5,                 0),
        (         [],   0,                 0),
    ]
    
    for (index, test) in enumerate(tests):
        print(f"TEST inOrderAt() #{index}... ", end="")
        arr, start, expected = test
        try:
            result = inOrderAt(arr, start)
            if result == expected:
                print("PASS")
            else:
                print("FAIL !!!")
        except AssertionError:
            if expected == "assertion error":
                print("PASS")
            else:
                print("FAIL !!!")

def test_sort() -> None:
    tests = [
        # Valid cases correctly sort elements from smallest to largest
        (                  [0],                   [0],                   [0]),
        (              [0,1,2],               [0,0,0],               [0,1,2]),
        (          [5,1,4,3,2],           [0,0,0,0,0],           [1,2,3,4,5]),
        (        [0,5,3,4,1,2],         [0,0,0,0,0,0],         [0,1,2,3,4,5]),
        (    [3,4,0,7,2,1,6,5],     [0,0,0,0,0,0,0,0],     [0,1,2,3,4,5,6,7]),
        ([6,2,8,4,3,0,7,9,1,5], [0,0,0,0,0,0,0,0,0,0], [0,1,2,3,4,5,6,7,8,9]),

        # Invalid inputs have mismatching lengths on input and output
        (          [1,2,3,4,5],                    [],     "assertion error"),
        (                   [],           [0,0,0,0,0],     "assertion error"),

        # Boundary cases - zero elements, reversed, in-order and all-identical
        (                   [],                    [],                    []),
        (          [1,2,3,4,5],           [0,0,0,0,0],           [1,2,3,4,5]),
        (          [5,4,3,2,1],           [0,0,0,0,0],           [1,2,3,4,5]),
        (          [5,5,5,5,5],           [0,0,0,0,0],           [5,5,5,5,5]),
    ]
    
    for (index, test) in enumerate(tests):
        print(f"TEST sort() #{index}... ", end="")
        source, result, expected = test
        try:
            sort(source, result)
            if result == expected:
                print("PASS")
            else:
                print("UNEXPECTED RESULT !!!")
        except AssertionError:
            if expected == "assertion error":
                print("PASS")
            else:
                print("UNEXPECTED ASSERT !!!")

def runTests() -> None:
    test_inOrderAt()
    test_mergeRanges()
    test_sort()

if __name__ == "__main__":
    runTests()