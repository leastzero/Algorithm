class Solution {
    fun solution(arr: IntArray): IntArray {
        var stk = mutableListOf<Int>()
        var i: Int = 0
        while (i < arr.size) {
            if (stk.isEmpty()) {
                stk.add(arr[i])
                i++
            } else if (stk.last() < arr[i]) {
                stk.add(arr[i])
                i++
            } else {
                stk.removeAt(stk.size - 1)
            }
        }
        return stk.toIntArray()
    }
}