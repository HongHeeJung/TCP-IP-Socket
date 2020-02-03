'''''''''''''''
코드 내용 
// 우분투 server의 멀티스레드 client

'''''''''''''''

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;


public class Main {
    static Thread sent;
    static Thread receive;
    static Socket socket;

    public static void main(String args[]){
            try {
                socket = new Socket("localhost",9999);
            } catch (UnknownHostException e1) {
                // TODO Auto-generated catch block
                e1.printStackTrace();
            } catch (IOException e1) {
                // TODO Auto-generated catch block
                e1.printStackTrace();
            }
            sent = new Thread(new Runnable() {

                @Override
                public void run() {
                    try {
                        BufferedReader stdIn =new BufferedReader(new InputStreamReader(socket.getInputStream()));
                        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                        while(true){
                            System.out.println("Trying to read...");
                                String in = stdIn.readLine();
                                System.out.println(in);
                                out.print("Try"+"\r\n");
                                System.out.println("Message sent");
                            }

                    } catch (IOException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                    }


                }
            });
        sent.start();
        try {
            sent.join();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }

}
