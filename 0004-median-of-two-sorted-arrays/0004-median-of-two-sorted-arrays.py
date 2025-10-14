class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2
        i, j = 0, 0
        cnt = 0
        ind1 = n//2
        ind2 = ind1 - 1
        index1 = -1
        index2 = -1

        while(i<n1 and j<n2):
            if(nums1[i]<nums2[j]):
                if(cnt == ind1):
                    index1 = nums1[i]
                if(cnt == ind2):
                    index2 = nums1[i]
                cnt += 1
                i += 1
            else:
                if(cnt == ind1):
                    index1 = nums2[j]
                if(cnt == ind2):
                    index2 = nums2[j]
                cnt += 1
                j += 1
        
        while(i<n1):
            if(cnt == ind1):
                index1 = nums1[i]
            if(cnt == ind2):
                index2 = nums1[i]
            cnt += 1
            i += 1

        while(j<n2):
            if(cnt == ind1):
                index1 = nums2[j]
            if(cnt == ind2):
                index2 = nums2[j]
            cnt += 1
            j += 1
        if(n%2==1):
            return float(index1)
        else:
            return (index1+index2)/2.0
