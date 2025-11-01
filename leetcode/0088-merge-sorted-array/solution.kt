class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        for (x in 0 until n) {
            nums1[m + x] = nums2[x]
        }
        nums1.sort()
    }
}
