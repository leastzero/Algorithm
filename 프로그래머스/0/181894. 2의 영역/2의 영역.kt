class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var first = arr.indexOfFirst { it == 2 }
        var last = arr.indexOfLast { it == 2 }
        if (first != -1 && last != -1) {
            answer = arr.sliceArray(first..last)
        } else {
            answer += -1
        }
    
        return answer
    }
}