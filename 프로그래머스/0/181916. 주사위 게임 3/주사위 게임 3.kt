import java.util.*

class Solution {
    fun solution(a: Int, b: Int, c: Int, d: Int): Int {
        var answer: Int = 0
        var nums = IntArray(4)
        nums[0] = a
        nums[1] = b
        nums[2] = c
        nums[3] = d
        nums.sort()
        
        var multi = 1
        var dice = IntArray(6)
        for (i in 0..3) {
            dice[nums[i] - 1]++
        }
        for (i in 0..5) {
            if (dice[i] == 4) {
                answer = 1111 * (i + 1)
                break
            } else if (dice[i] == 3) {
                for (j in 0..5) {
                    if (dice[j] == 1) {
                        answer = (10 * (i + 1) + (j + 1)) * (10 * (i + 1) + (j + 1))
                        break
                    }
                }
            } else if (dice[i] == 2) {
                for (j in 0..5) {
                    if (dice[j] == 2) {
                        if (i == j) {
                            continue
                        } else {
                            answer = (i + 1 + j + 1) * (i + 1 - (j + 1))
                            break
                        }
                    } else if (dice[j] == 1) {
                        multi *= (j + 1)
                    }
                }
                if (multi != 1) {
                    answer = multi
                }
            }
            if (nums[0] != nums[1] && nums[1] != nums[2] && nums[2] != nums[3]) {
                answer = nums[0]
            }
        }
        return answer
    }
}