class Solution {
    fun solution(intStrs: Array<String>, k: Int, s: Int, l: Int): IntArray {
        var answer = ArrayList<Int>()
        for (i in 0..intStrs.size - 1) {
            var a = intStrs[i].substring(s, s + l).toInt()
            if (a > k) {
                answer.add(a)
            }
        }
        return answer.toIntArray()
    }
}