class Solution {
    fun solution(names: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        for (i in names.indices) {
            if (i % 5 == 0) answer += names[i]
        }
        return answer
    }
}