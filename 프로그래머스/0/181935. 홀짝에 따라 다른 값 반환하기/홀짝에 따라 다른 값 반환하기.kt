class Solution {
    fun solution(n: Int): Int {
        var answer: Int = 0
        if (n % 2 == 1) {
            for (i in n downTo 0 step 2) answer += i
        } else {
            for (i in n downTo 0 step 2) answer += i * i
        }
        return answer
    }
}