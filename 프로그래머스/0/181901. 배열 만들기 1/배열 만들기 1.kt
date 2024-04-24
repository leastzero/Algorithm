class Solution {
    fun solution(n: Int, k: Int): IntArray {
        var answer = IntArray(n / k)
        var index = 0
        for (i in 1..n) {
            if (i % k == 0) {
                answer[index] = i
                index++
            }
        }
        return answer
    }
}