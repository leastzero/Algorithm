class Solution {
    fun solution(arr: IntArray, intervals: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf()
        for (i in intervals.indices) {
            var a = intervals[i][0]
            var b = intervals[i][1]
            answer += arr.slice(a..b)
        }
        return answer
    }
}