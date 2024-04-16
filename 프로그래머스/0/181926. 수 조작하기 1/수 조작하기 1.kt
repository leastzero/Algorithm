class Solution {
    fun solution(n: Int, control: String): Int {
        var answer = n
        for (i in 0 until control.length) {
            when (control[i]) {
                'w' -> answer += 1
                's' -> answer -= 1
                'd' -> answer += 10
                'a' -> answer -= 10
            }
        }

        return answer
    }
}