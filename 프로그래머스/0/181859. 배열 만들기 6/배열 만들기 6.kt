class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var i = 0
        while (i < arr.size) {
            if (answer.isEmpty()) {
                answer += arr[i]
                i++
            } else if(answer.last() == arr[i]) {
                answer = answer.copyOf(answer.size - 1)
                i++
            } else if(answer.last() != arr[i]) {
                answer += arr[i]
                i++
            }
        }
        if (answer.isEmpty()) {
            answer += -1
        }
        return answer
    }
}