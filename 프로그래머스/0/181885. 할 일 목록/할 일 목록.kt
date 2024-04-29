class Solution {
    fun solution(todo_list: Array<String>, finished: BooleanArray): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        for (i in todo_list.indices) {
            if (finished[i] == false) {
                answer += todo_list[i]
            }
        }
        return answer
    }
}