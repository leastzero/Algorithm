class Solution {
    fun solution(myString: String, pat: String): Int {
        var answer: Int = 0
        var a: String = ""
        for (i in 0 until myString.length) {
            if (myString[i] == 'A') a += 'B'
            else a += 'A'
        }
        if (a.contains(pat)) answer = 1
        return answer
    }
}