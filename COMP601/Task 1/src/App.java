import static java.lang.System.out;

class Main {
    public static void main(String[] args) throws Exception {
        // Declare FMT as final and use CONSTANT naming convention
        final String FMT = "%-20s%-10s\n";

        out.printf(FMT, "Escape sequence", "Description");
        out.println("-".repeat(42));
        out.printf(FMT, "\\n", "New Line Character");
        out.printf(FMT, "\\t", "Tab character");
        out.printf(FMT, "\\\"", "Double quote Character");
        out.printf(FMT, "\\b", "Backspace Character");
    }
}