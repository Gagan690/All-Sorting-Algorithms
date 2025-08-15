class Solution:
    def sortArray(self, nums):
      # return sorted(nums)
        if not nums or len(nums) <= 1:
            return nums

        minNums = min(nums)
        maxNums = max(nums)

        if minNums == maxNums:
            return nums

        lenght = len(nums)

        bucket = [[] for _ in range(lenght)]
        range_per_bucket = (maxNums - minNums) / lenght

        for num in nums:
            if num == maxNums:
                bucketIdx = lenght - 1
            else:
                bucketIdx = int((num - minNums) / range_per_bucket)
            bucket[bucketIdx].append(num)
        for buckets in bucket:
            self.InsertionSort(buckets)

        result = []
        for buckets in bucket:
            result.extend(buckets)

        return result

    def InsertionSort(self, arr):
        n = len(arr)
        for i in range(1,n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
