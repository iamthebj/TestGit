import java.io.*;  
public class FileDemo {  
    void mai(String[] args) {  
  
        try {  
            File file = new File("javaFile123.txt");  
            if (file.createNewFile()) {  
                System.out.println("New File is created");
            } else {  
                System.out.println("File already exists.");  
            }  
        } catch (IOException e) {  
            e.printStackTrace();  
        }  
  
    }  
}  
