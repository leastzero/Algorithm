class Solution {
    fun solution(myString: String, pat: String): String {
        var answer: String = ""
        answer = myString.substringBeforeLast(pat) + pat
        return answer
    }
}