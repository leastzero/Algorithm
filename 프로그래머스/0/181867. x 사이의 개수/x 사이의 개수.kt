class Solution {
    fun solution(myString: String): IntArray {
        var answer: IntArray = intArrayOf()
        var list = myString.split('x')
        for (i in list.indices) {
            answer += list[i].length
        }
        return answer
    }
}