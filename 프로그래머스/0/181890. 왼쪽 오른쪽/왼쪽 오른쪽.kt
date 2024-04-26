class Solution {
    fun solution(str_list: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        for (i in 0..str_list.size - 1) {
            if (str_list[i] == "l") {
                answer = str_list.sliceArray(0..i-1)
                break
            } else if (str_list[i] == "r") {
                answer = str_list.sliceArray(i+1..str_list.size-1)
                break
            } else {
                answer = emptyArray()
            }
        }
        return answer
    }
}