import java.io.File
fun main(args: Array<String>) {
val fileName = "data.txt"
var file = File(fileName)
File("./").walk().forEach {
println(it.extension + " is the extension of " + it.name)
}
}
