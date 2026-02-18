import heapq
import math

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set_list1 = set(list1)
        set_list2 = set(list2)
        result = []
        final_result = []
        intersection = set_list1.intersection(set_list2)
        for word in intersection:
            index1 = list1.index(word)
            index2 = list2.index(word)
            if not result:
                result.append((index1 + index2, word))
                heapq.heapify(result)
            else:
                heapq.heappush(result, (index1 + index2, word))
        smallest_sum = math.inf
        while result:
            index_sum, word = heapq.heappop(result)
            if index_sum < smallest_sum:
                smallest_sum = index_sum
                final_result.append(word)
            elif index_sum == smallest_sum:
                final_result.append(word)
            else:
                break
        return final_result
        