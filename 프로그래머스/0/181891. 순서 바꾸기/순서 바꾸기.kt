class Solution {
    fun solution(num_list: IntArray, n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        answer += num_list.slice(n..num_list.size-1)
        answer += num_list.slice(0..n-1)
        return answer
    }
}