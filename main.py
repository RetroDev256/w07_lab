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
        
        # Swap source and destination for next iteration
        source[:] = dest

def main():
    # unsorted = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    # unsorted = [2,4,1,8,10,17,14,19,18,16,15,13,7,0,12,6,9,11,5,3]
    # unsorted = [14,0,7,12,16,17,11,15,3,18,4,10,1,9,5,13,19,8,2,6]
    unsorted = [9,5,6,4,19,15,16,10,12,7,2,8,1,11,0,14,18,13,17,3]
    sorted = [0] * len(unsorted)
    sort(unsorted, sorted)
    print(sorted)

if __name__ == "__main__":
    main()