class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict()


        ele=list(set(nums))
        
        for n in ele:
            res[n]=0

        for i in nums:
            res[i]+=1

        ress=[]

        # Sort elements by their frequencies in descending order
        ele.sort(key=lambda x: res[x], reverse=True)
            
        # Take the first k elements from the sorted list
        for i in range(k):
            ress.append(ele[i])

        return ress
        