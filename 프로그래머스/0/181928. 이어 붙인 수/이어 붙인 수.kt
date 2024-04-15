class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        var a: String = ""
        var b: String = ""
        for (i in 0 until num_list.size) {
            if (num_list[i] % 2 == 1) {
                a += num_list[i].toString()
            } else {
                b += num_list[i].toString()
            }
        }
        answer = a.toInt() + b.toInt()
        return answer
    }
}