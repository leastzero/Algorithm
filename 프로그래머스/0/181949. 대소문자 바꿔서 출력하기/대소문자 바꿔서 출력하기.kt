fun main(args: Array<String>) {
    val s1 = readLine()!!
    val result = StringBuilder()
    for (i in 0 until s1.length) {
        if (s1[i].isUpperCase()) {
            result.append(s1[i].toLowerCase())
        } else {
            result.append(s1[i].toUpperCase())
        }
    }
    println(result)
}