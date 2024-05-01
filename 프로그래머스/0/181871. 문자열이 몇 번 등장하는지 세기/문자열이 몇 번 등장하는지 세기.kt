class Solution {
    fun solution(myString: String, pat: String): Int {
        var answer: Int = 0
        for (i in 0..myString.length - pat.length) {
            if (pat == myString.substring(i, i + pat.length)) answer++
        }
        return answer
    }
}