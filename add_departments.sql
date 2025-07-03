-- PROG8850 Assignment 2 - Question 2: Add Departments Table
-- Author: Jithin
-- Purpose: Create departments table for CI/CD pipeline testing

-- Create the companydb database if it doesn't exist
CREATE DATABASE IF NOT EXISTS companydb;

-- Use the companydb database
USE companydb;

-- Create the departments table with specified columns
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255)
);

-- Insert sample data for testing purposes
INSERT INTO departments (department_name, location) VALUES 
    ('Information Technology', 'Toronto'),
    ('Human Resources', 'Vancouver'),
    ('Finance', 'Calgary'),
    ('Marketing', 'Montreal')
ON DUPLICATE KEY UPDATE 
    department_name = VALUES(department_name),
    location = VALUES(location);

-- Verify the table creation and data insertion
SELECT COUNT(*) as department_count FROM departments;