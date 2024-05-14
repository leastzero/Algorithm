class Solution {
    fun solution(myString: String): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        answer += myString.split("x").filter {
            it.isNotEmpty()
        }
        answer.sort()
        return answer
    }
}