CREATE DATABASE IF NOT EXISTS companydb;
USE companydb;

-- Create the projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Conditionally add the 'budget' column
SET @column_exists := (
  SELECT COUNT(*)
  FROM INFORMATION_SCHEMA.COLUMNS 
  WHERE TABLE_SCHEMA = 'companydb' 
    AND TABLE_NAME = 'projects' 
    AND COLUMN_NAME = 'budget'
);

SET @alter_stmt := IF(@column_exists = 0, 
  'ALTER TABLE projects ADD COLUMN budget DECIMAL(10,2)', 
  'SELECT "Column already exists"');

PREPARE stmt FROM @alter_stmt;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
