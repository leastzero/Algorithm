class Solution {
    fun solution(n: Int, slicer: IntArray, num_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var a = slicer[0]
        var b = slicer[1]
        var c = slicer[2]
        when (n) {
            1 -> answer = num_list.sliceArray(0..b)
            2 -> answer = num_list.sliceArray(a..num_list.size-1)
            3 -> answer = num_list.sliceArray(a..b)
            else -> answer = num_list.slice(a..b step c).toIntArray()
        }
        return answer
    }
}