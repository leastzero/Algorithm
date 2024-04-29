class Solution {
    fun solution(numbers: IntArray, n: Int): Int {
        var answer: Int = 0
        for (i in numbers.indices) {
            if (answer > n) break
            answer += numbers[i]
        }
        return answer
    }
}