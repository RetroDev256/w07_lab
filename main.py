def mergeRanges(unsorted: list[int], start: int, split: int, end: int) -> None:
    ''' Given two consecutive sorted ranges into an unsorted list, this
    function merges the two ranges to produce one larger sorted range. '''

    # If the length of one of the ranges is zero, the ranges are already merged
    assert end >= split and split >= start
    if start == split or split == end:
        return

    left_list: list[int] = unsorted[start:split]
    right_list: list[int] = unsorted[split:end]

    left: int = 0 # index into left_list
    right: int = 0 # index into right_list
    index: int = start # index into unsorted

    # Merge the two lists until one is exhausted
    while left < len(left_list) and right < len(right_list):
        # Using <= here for a stable sort, even though it really doesn't matter
        if left_list[left] <= right_list[right]:
            unsorted[index] = left_list[left]
            left += 1
        else:
            unsorted[index] = right_list[right]
            right += 1
        index += 1

    # Copy any remaining elements from the right list
    while right < len(right_list):
        unsorted[index] = right_list[right]
        index += 1
        right += 1

    # Copy any remaining elements from the left list
    while left < len(left_list):
        unsorted[index] = left_list[left]
        index += 1
        left += 1

def inOrderAt(unsorted: list[int], start: int) -> int:
    ''' Returns the length of the in-order sublist at the start index '''
    for index in range(start + 1, len(unsorted)):
        if unsorted[index] < unsorted[index - 1]:
            return index - start
    return len(unsorted) - start

def sort(unsorted: list[int]) -> None:
    while True:

        # End condition - the list is already sorted
        if inOrderAt(unsorted, 0) == len(unsorted):
            return

        # Reduction step - merge consecutive pairs of in-order segments
        start = 0
        while start < len(unsorted):
            split = start + inOrderAt(unsorted, start)
            end = split + inOrderAt(unsorted, split)
            mergeRanges(unsorted, start, split, end)
            start = end

def main():
    # unsorted = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    # unsorted = [2,4,1,8,10,17,14,19,18,16,15,13,7,0,12,6,9,11,5,3]
    # unsorted = [14,0,7,12,16,17,11,15,3,18,4,10,1,9,5,13,19,8,2,6]
    unsorted = [9,5,6,4,19,15,16,10,12,7,2,8,1,11,0,14,18,13,17,3]
    sort(unsorted)
    print(unsorted)

if __name__ == "__main__":
    main()