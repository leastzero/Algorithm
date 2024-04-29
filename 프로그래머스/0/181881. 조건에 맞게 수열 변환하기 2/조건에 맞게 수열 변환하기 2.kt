class Solution {
    fun solution(arr: IntArray): Int {
        var answer: Int = 0
        while (true) {
            val newArr = IntArray(arr.size) { i ->
                when {
                    arr[i] >= 50 && arr[i] % 2 == 0 -> arr[i] / 2
                    arr[i] < 50 && arr[i] % 2 == 1 -> arr[i] * 2 + 1
                    else -> arr[i]
                }
            }
            if (newArr.contentEquals(arr)) break
            for (i in arr.indices) {
                arr[i] = newArr[i]
            }
            answer++
        }
        return answer
    }
}