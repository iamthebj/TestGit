import ;  
public class FileDemo {  
    public static void main(String[] args) {  
  
        try {  
            File file = new File("javaFile123.txt");  
            if (file.)) {  
                System.out.println("New File is created");
            } else {  
                System.out.println("File already exists.");  
            }
        } catch (IOException e) {  
            printStackTrace();  
        }  
 
}  
