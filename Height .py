import java.util.*;
public class Nd{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int x,y;
        x=sc.nextInt();
        y=sc.nextInt();
        if(x<y){
            System.out.println(y);
        }
        else{
            System.out.println(x);
        }
    }
}