// License: MIT (c) GitLab Inc.
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class EmptyDBPassword {
    private static final String URL = "jdbc:mysql://localhost:3306/your_database_name";
    private static final String USERNAME = "your_username";

    public static Connection getConnection() {
        Connection connection = null;
        try {
            // ruleid: java_password_rule-EmptyDBPassword
            connection = DriverManager.getConnection(URL, USERNAME, "");
            System.out.println("Connected to the database successfully!");
        } catch (SQLException e) {
            System.out.println("Error connecting to the database: " + e.getMessage());
            e.printStackTrace();
        }
        return connection;
    }

    public static void main(String[] args) {
        getConnection();
    }
}
