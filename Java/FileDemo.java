import java.io.*;  
public class FileDemo {  
    public static void main(String[] args) {  
  
        {  
            File file = new File("javaFile123.txt");  
            f (file.createNewFile()) {  
                System.out.println("New File is created");
            } else {  
                System.out.println("File already exists.");  
            }  
        } catch (IOException e) {  
            e.printStackTrace();  
        }  
  
    }  
}  
