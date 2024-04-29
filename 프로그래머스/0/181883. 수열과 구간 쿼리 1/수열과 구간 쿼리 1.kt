class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf()
        answer = arr
        for (i in queries.indices) {
            var s = queries[i][0]
            var e = queries[i][1]
            for (j in s..e) {
                answer[j]++
            }
        }
        return answer
    }
}