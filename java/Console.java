import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Console {

  public static <T> boolean writeJumpLine(T tagMessage, boolean isMessage) {
    try{
      System.out.println(tagMessage);
      if(isMessage) {
        writeJumpLine("It has been write correctly!", false);
      }
      return true;
    }catch (Exception e) {
      if (isMessage) {
        writeJumpLine("Could not write correctly for error: " + e.getMessage(), false);
      }
      return false;
    }
  }

  public static <T> boolean writeJumpLine(T [] list, boolean isMessage) { 
    for (int index = 0; index < list.length; index++) {
      if(!writeJumpLine((index + 1) + "." + list[index], isMessage)){
        writeJumpLine("There is an incorrect data in the vector to show", false);
        writeJumpLine(index + "Position of the vector with the error", false);
      }
    }
    return true;
  }
  public static <T> boolean write(T tagMessage, boolean isMessage) {
    try {
      System.out.print(tagMessage);
      if (isMessage) {
        writeJumpLine("It has been write correctly!", false);
      }
      return true;
    } catch (Exception e) {
      if (isMessage) {
        writeJumpLine("Could not write correctly for error: "+e.getMessage(), false);
      }
      return false;
    }
  }

  @SuppressWarnings("unchecked")
  private static <T> T read(T chainInput, boolean isMessage){
    BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    String value = "", option = "";
    T backupChainInput = chainInput;
    try{
      value = input.readLine();
      option = ((Object) chainInput).getClass().getSimpleName();
      switch(option) {
        case "String" -> { if(!isNumber(value)) chainInput = (T) String.valueOf(value.trim()); }
        case "Double" -> { if(isNumber(value) && value.contains(".")) chainInput = (T) Double.valueOf(value.trim()); }
        case "Float" -> { if(isNumber(value) && value.contains(".")) chainInput = (T) Float.valueOf(value.trim()); }
        case "Integer" -> { if(isNumber(value)) chainInput = (T) Integer.valueOf(value.trim()); }
      }
      if(isMessage) {
        writeJumpLine("It has been Read correctly!", false);
      }
    }catch (Exception e) {
      if(isMessage) {
        writeJumpLine("Could not read correctly for error: " + e.getMessage(), false);
      }
    }
    if (backupChainInput.equals(chainInput)) writeJumpLine("Invalid value entered", false);
    return chainInput;
  }

  public static <T> T read(String tagMessage, T chainInput, boolean isMessage) {
    T result;
    do {
      writeJumpLine(tagMessage, isMessage);
      result = read(chainInput, isMessage);
    } while (chainInput.equals(result));
    return result;
  }

  public static boolean isNumber(String chain){
    return chain.matches("[+-]?\\d*(\\.\\d+)?");
  }
}
