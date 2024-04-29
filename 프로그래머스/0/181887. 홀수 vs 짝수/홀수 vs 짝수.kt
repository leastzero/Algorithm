class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        var a = 0
        var b = 0
        for (i in num_list.indices) {
            if (i % 2 == 0) a += num_list[i]
            else b += num_list[i]
        }
        if (a > b) answer = a
        else if (a < b) answer = b
        else answer = a
        
        return answer
    }
}