class Solution {
    fun solution(my_string: String, overwrite_string: String, s: Int): String {
        var answer: String = ""
        answer = my_string.substring(0, s) + overwrite_string + my_string.substring(s + overwrite_string.length)
        return answer
    }
}

fun main(args: Array<String>) {
    val my_string = readLine()!!
    val overwrite_string = readLine()!!
    val s = readLine()!!.toInt()
    
    val solution = Solution()
    val result = solution.solution(my_string, overwrite_string, s)
    println(result)
}