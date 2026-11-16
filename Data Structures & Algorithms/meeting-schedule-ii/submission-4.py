"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        tracker = 0
        maximum = 0

        assert(len(starts) == len(ends))
        n = len(starts)
        i, j = 0, 0
        while i < n and j < n:
            if starts[i] < ends[j]:
                tracker += 1
                i += 1
            else:
                tracker -= 1
                j += 1
            
            maximum = max(maximum, tracker)
        
        while i < n:
            tracker += 1
            i += 1 
            maximum = max(maximum, tracker)
            
        while j < n:
            tracker -= 1
            j += 1 
        
        return maximum


