class Solution {
    fun solution(arr: IntArray, flag: BooleanArray): IntArray {
        val answer = mutableListOf<Int>()

        for (i in arr.indices) {
            if (flag[i] == true) {
                for (j in 0 until arr[i] * 2) {
                    answer.add(arr[i])
                }
            } else {
                for (j in 0 until arr[i]) {
                    if (answer.isNotEmpty()) {
                        answer.removeAt(answer.size - 1)
                    }
                }
            }
        }
        return answer.toIntArray()
    }
}