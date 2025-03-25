import java.util.*;

public class EXAMPLE {

    public static void main(String[] args) {
        String password = "aaaa";
        String password1 = "";
        String URL_FORMAT = "mongodb+srv://%s:%s@%s:%d/%s";
        // ruleid: mongo
        String connectionString = String.format(URL_FORMAT, username, password, host, database, options);
        // ruleid: mongo
        String connectionString1 = String.format("mongodb://superusername:%s@%s/%s?%s",password, host, database, options);
        // ok: mongo
        String connectionString = String.format("mongodb://superusername:%s@%s/%s?%s",a,password, host, database, options);
        // ok: mongo
        String connectionString1 = String.format("mongodb://superusername:%s@%s/%s?%s",password1, host, database, options);
}
