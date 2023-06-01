

import java.io.*;
import java.io.IOException;

//import bkool.codegeneration.IllegalRuntimeException;


public class io {
	
	public static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	public static Writer writer = new BufferedWriter(new OutputStreamWriter(System.out));
	
	// truncate the given floating-point number to an integer.
	public static int int_of_float(float a) {
	    return (int) a;
        }
	// convert an integer to floating-point
	public static float float_to_int(int a) {
            return (float) a;
        }
        //convert the given string to an integer.
	public static int int_of_string(String a) {
 	    return Integer.parseInt(a);
	}
        // return the string representation of an integer, in decimal
	public static String string_of_int(int a) {
	    return Integer.toString(a);
	}
	// convert the given string to a float.
	public static float float_of_string(String a) {
	    return Float.parseFloat(a);
	}
	// convert the given string to a boolean
	public static String string_of_float(float a) {
	    return Float.toString(a);
	}
	// convert the given string to a boolean
	public static boolean bool_of_string(String a) {
	    return Boolean.parseBoolean(a);
	}
	// convert a boolean to string
	public static String string_of_bool(boolean a) {
	    return Boolean.toString(a);
	}

    /** reads and returns a string value from the standard input
     *  @return int a string value read from standard input
     */
    public static String read() {
        String tmp = "";
        try {
            tmp = input.readLine();
            return tmp;
        } catch (IOException e) {
        	e.printStackTrace();
        }
        return tmp;
    }

    /** prints the value of the string to the standard output
     *	@param a the string is printed out
     */
     public static void print(String a ) {
    	 System.out.print(a);
    }
    
    /** same as putString except that it also prints a new line
     *	@param a the string is printed out
     */
    public static void printStrLn(String a)  {
    	System.out.println(a);
    }
    /** print out an empty line
     **/
    public static void printLn()  {
    	System.out.println();
    }
    
    public static void close() {
    	try {
    		writer.close();
    	} catch (IOException e) {
			 e.printStackTrace();
		}
    }
}

