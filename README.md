# PROG8850 – Assignment 2: Database CI/CD Automation

This assignment demonstrates a CI/CD pipeline that deploys MySQL database schema and data using a combination of:
- SQL scripts
- Python automation
- GitHub Actions workflow
- Ansible for setup automation
- Adminer GUI for manual verification

---

## Purpose

Automate database changes (DDL and DML) using DevOps tools in a reproducible and portable way.

---

## Commands and Their Purpose

### 1. Start Services

```bash
ansible-playbook up.yml
```
- Brings up MySQL and Adminer using Docker
- Installs MySQL client, Python dependencies, and ACT (local GitHub Actions runner)

### 2. Manually Run Python Script (optional)

```bash
python3 database_automation.py
```
- Connects to MySQL database
- Creates `projects` table and conditionally adds `budget` column
- Inserts data if required

### 3. Access MySQL to Verify

```bash
mysql -u root -h 127.0.0.1 -p
```
- Login to the database and verify data manually

SQL commands:

```sql
USE companydb;
SHOW TABLES;
DESC departments;
SELECT * FROM departments;
```

### 4. Run GitHub Actions Locally (CI/CD)

```bash
bin/act
```

If that doesn’t work in Codespaces:

```bash
bin/act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04
```

- Executes the full GitHub Actions workflow locally
- Deploys schema, inserts data, and uploads a report

### 5. Tear Down Environment

```bash
ansible-playbook down.yml
```
- Shuts down and removes containers

---

## Files and Structure

| File | Description |
|------|-------------|
| `add_departments.sql` | Creates departments table and inserts records |
| `projects_schema.sql` | Fallback SQL schema for projects |
| `database_automation.py` | Python automation for schema changes |
| `ci_cd_pipeline.yml` | GitHub Actions workflow |
| `up.yml / down.yml` | Ansible playbooks to setup/teardown environment |
| `mysql-adminer.yml` | Docker Compose stack |
| `README.md` | This documentation |
| `bin/act` | Local GitHub Actions runner |
| `screenshots` | Contains all screenshots |

---

## Deployment Verification

Adminer: `http://localhost:8080`  
Login with:
- **Server**: db
- **User**: root
- **Password**: Secret5555
- **Database**: companydb

GitHub Actions: check `Actions` tab → `database-deployment`  
- Install MySQL
- Run Python Script
- Generate and Upload Report

---

## Deployment Report

A text file named `deployment_report.txt` is generated and uploaded via GitHub Actions. It includes:
- Deployment Date/Time
- Workflow Run #
- Commit SHA
- GitHub Actor
- SUCCESS/FAILURE status

---

## Author

- Jithin Jyothi  
- Course: PROG8850 – Database Automation & Scripting
