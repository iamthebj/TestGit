import java.io.*;  
public class FileDemo {  
    public static void main(String[) {  
  
        try {  
            File file = new File("javaFile123.txt");  
            if (file.createNewFile()) {  
                System.out.println("New File is created");
            } els
                System.out.println("File already exists.");  
            }  
        } catch (IOExcept 

  
    }  
}  
