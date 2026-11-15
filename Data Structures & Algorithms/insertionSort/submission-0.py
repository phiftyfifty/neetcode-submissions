# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []


        for i in range(len(pairs)):
            j = i - 1

            # move the elements greater than the current key one position to the right, look backward at the left (sort backward if the key is greater than the current element at i)
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j + 1] = pairs[j+1], pairs[j]
                j -= 1

            # after one sweep, we can store the state of the array into output         
            output.append(pairs[:])
        return output