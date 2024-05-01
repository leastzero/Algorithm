class Solution {
    fun solution(my_string: String): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        answer = my_string.split(" ").filter {
            it.isNotEmpty()
        }.toTypedArray()
        return answer
    }
}