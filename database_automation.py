#!/usr/bin/env python3
"""
PROG8850 Assignment 2 - Question 1: Database Automation Script
Author: Jithin
Purpose: Automate execution of SQL schema changes using mysql-connector-python
"""

import mysql.connector
from mysql.connector import Error
import os
import sys

def connect_to_database():
    """
    Establish connection to MySQL database using environment variables or defaults
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', '3306')),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'Secret5555'),
            database=os.getenv('DB_NAME', 'companydb')
        )
        
        if connection.is_connected():
            print(f"Successfully connected to MySQL database: {connection.database}")
            return connection
            
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def execute_sql_script(connection, sql_file_path):
    """
    Execute SQL script with proper transaction handling
    """
    cursor = None
    try:
        cursor = connection.cursor()
        
        # Read SQL script file
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()
        
        # Split script into individual statements
        sql_statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]
        
        print(f"Executing {len(sql_statements)} SQL statements...")
        
        # # Execute each statement
        # for i, statement in enumerate(sql_statements, 1):
        #     if statement:
        #         print(f"Executing statement {i}: {statement[:50]}{'...' if len(statement) > 50 else ''}")
        #         cursor.execute(statement)
        #         print(f"Statement {i} executed successfully")
        # Execute each statement
        for i, statement in enumerate(sql_statements, 1):
            if statement:
                print(f"Executing statement {i}: {statement[:50]}{'...' if len(statement) > 50 else ''}")
                cursor.execute(statement)

                # Fix: Clear unread results
                while cursor.nextset():
                    pass

                print(f"Statement {i} executed successfully")

        
        # Commit all changes
        connection.commit()
        print("All SQL statements executed successfully and changes committed!")
        return True
        
    except Error as e:
        print(f"Error executing SQL script: {e}")
        if connection:
            connection.rollback()
            print("Transaction rolled back due to error")
        return False
        
    finally:
        if cursor:
            cursor.close()

def verify_table_creation(connection):
    """
    Verify that the projects table was created successfully with all columns
    """
    try:
        cursor = connection.cursor()
        
        # Check if table exists and get its structure
        cursor.execute("DESCRIBE projects")
        columns = cursor.fetchall()
        
        print("\nTable 'projects' structure:")
        print("-" * 50)
        for column in columns:
            print(f"Column: {column[0]}, Type: {column[1]}, Null: {column[2]}, Key: {column[3]}")
        
        cursor.close()
        return True
        
    except Error as e:
        print(f"Error verifying table creation: {e}")
        return False

def main():
    """
    Main function to orchestrate the database automation process
    """
    print("PROG8850 Assignment 2 - Database Automation Script")
    print("=" * 55)

    # SQL script file paths
    scripts = ["projects_schema.sql", "add_departments.sql"]

    # ✅ Connect to database FIRST
    connection = connect_to_database()
    if not connection:
        print("Failed to connect to database. Exiting...")
        sys.exit(1)

    try:
        # ✅ Then loop through and execute each script
        for sql_script_path in scripts:
            print(f"\nExecuting script: {sql_script_path}")

            if not os.path.exists(sql_script_path):
                print(f"Error: SQL script file '{sql_script_path}' not found!")
                continue

            if execute_sql_script(connection, sql_script_path):
                print(f"✅ Executed {sql_script_path} successfully")
            else:
                print(f"❌ Failed to execute {sql_script_path}")

        print("\n" + "=" * 55)
        print("✅ All database schema changes completed successfully!")

        # Optional: Verify project table creation
        verify_table_creation(connection)

    finally:
        # ✅ Close DB connection at the end
        if connection and connection.is_connected():
            connection.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()