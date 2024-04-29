class Solution {
    fun solution(myString: String, pat: String): Int {
        var answer: Int = 0
        if (myString.toLowerCase().contains(pat.toLowerCase())) answer = 1
        return answer
    }
}