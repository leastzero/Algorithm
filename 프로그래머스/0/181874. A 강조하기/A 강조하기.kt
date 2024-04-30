class Solution {
    fun solution(myString: String): String {
        var answer: String = ""
        myString.forEach {
            if (it == 'a' || it == 'A') answer += it.toUpperCase()
            else answer += it.toLowerCase()
        }
        return answer
    }
}