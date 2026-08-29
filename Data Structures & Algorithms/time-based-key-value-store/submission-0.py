class TimeMap:
#timestamp map key and value sorted in an increasing order -> binary search works (log n time)

    def __init__(self):
        self.store = {} #map time:value

    def set(self, key: str, value: str, timestamp: int) -> None:
        #empty list for new key 
        if key not in self.store: self.store[key] = []

        #append time and value to key in store since it's strictly increasing only 
        self.store[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        values = self.store[key]

        l,r = 0, len(values) - 1 
        res = ""

        while l <= r: 
            mid = (l + r) // 2
            saved_time, saved_val = values[mid]

            if saved_time <= timestamp: 
                res = saved_val #timestamp is valid, save it and search right for a newer valid time
                l = mid + 1 
            else: 
                r = mid - 1  #timestamp too large; search left 
        return res        
