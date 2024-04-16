class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf()
        var tmp: Int = 0
        for (i in 0 until queries.size) {
            tmp = arr[queries[i][0]]
            arr[queries[i][0]] = arr[queries[i][1]]
            arr[queries[i][1]] = tmp
        }
        answer = arr
        return answer
    }
}