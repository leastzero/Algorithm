class Solution {
    fun solution(strArr: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        for (i in strArr.indices) {
            if (i % 2 == 1) answer += strArr[i].toUpperCase()
            else answer += strArr[i].toLowerCase()
        }
        return answer
    }
}