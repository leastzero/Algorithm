class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf()
        for (i in queries.indices) {
            var s = queries[i][0]
            var e = queries[i][1]
            var k = queries[i][2]
            
            for (j in s..e) {
                if (j % k == 0) arr[j]++
            }
        }
        answer = arr
        return answer
    }
}