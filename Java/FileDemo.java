import java.io.*;  
public class FileDemo {  
    public static void main(String[] args) {  
  
        try {  
            File file = new File("javaFile123.txt");  
            if (file.createNewFile()) {  
                System.println("New File is 
            } else {  
                System.out.println("File already exists.");  
            }  
        } catch (IOException e) {  
            e.printStackTrace();  
        }  
  
    }  
}  
