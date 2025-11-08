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
    
    for test in tests:
        source, dest, start, split, end, expected = test
        try:
            mergeRanges(source, dest, start, split, end)
            assert dest == expected
        except AssertionError:
            assert expected == "assertion error"

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
    
    for test in tests:
        arr, start, expected = test
        try:
            result = inOrderAt(arr, start)
            assert result == expected
        except AssertionError:
            assert expected == "assertion error"

def test_sort() -> None:
    tests = [
        ([1,2,3,4,5], [0,0,0,0,0],       [1,2,3,4,5]),
        ([5,4,3,2,1], [0,0,0,0,0],       [1,2,3,4,5]),
        ([5,1,4,3,2], [0,0,0,0,0],       [1,2,3,4,5]),
        ([1,2,3,4,5],          [], "assertion error"),
        (         [], [0,0,0,0,0], "assertion error"),
        (         [],          [],                []),
        (        [0],         [0],               [0]),
        ([5,5,5,5,5], [0,0,0,0,0],       [5,5,5,5,5]),
    ]
    
    for test in tests:
        source, dest, expected = test
        try:
            sort(source, dest)
            assert dest == expected
        except AssertionError:
            assert expected == "assertion error"

def runTests() -> None:
    test_inOrderAt()
    test_mergeRanges()
    test_sort()

if __name__ == "__main__":
    runTests()