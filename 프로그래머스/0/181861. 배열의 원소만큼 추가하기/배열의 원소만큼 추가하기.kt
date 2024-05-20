class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        for (i in arr.indices) {
            for (j in 0 until arr[i]) answer += arr[i]
        }
        return answer
    }
}