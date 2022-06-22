import Console;

public class Menu{
  private String title;
  private String[] menuOptions;
  protected int option;
  private int optionExit;

  public Menu(String[] menuOptions){
    this.option = 0;
  }

  public Menu(String title, String[] menuOptions){
    this.title = title;
    this.menuOptions = menuOptions;
    this.optionExit = menuOptions.length + 1;
    this.repeatedMenu();
  }

  private void repeatedMenu() {
    do {
      this.showMenu();
      this.readOption();
      this.processOption();
    } while (this.option != this.optionExit);
  }

  private void showMenu(){
    Console.writeJumpLine(title, false);
    Console.writeJumpLine(menuOptions, false);
    Console.writeJumpLine(optionExit+". Exit...", false);
  }

  private void readOption() {
    this.option = 0;
    option = Console.read("Enter the desired option: ", this.option, false);
    if(option < 1 || option > optionExit) {
      Console.writeJumpLine("Invalid option", false);
    }
  }

  protected void processOption() { }
}
