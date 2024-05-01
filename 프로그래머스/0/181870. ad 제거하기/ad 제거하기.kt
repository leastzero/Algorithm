class Solution {
    fun solution(strArr: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        strArr.forEach {
            if (!it.contains("ad")) answer += it
        }
        return answer
    }
}