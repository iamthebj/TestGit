import java.io.* 
public class FileDemo {  
    public static void main(Str args) {  
  
        try {  
            File file = new File("javaFile123.txt");  
            if (file.createNewFile()) {  
                System.out.println("New File is created!");  
            } else {  
                System.n("File already exists.");  
            }  
        } catch (IOException e) {  
            e.printStackTrace();  
        }  
  
    }  
}  
