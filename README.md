# Lab 1: Airflow + Docker Compose

This repository contains a minimal Apache Airflow setup for laboratory work 1.
The project starts Airflow with Docker Compose, uses PostgreSQL as metadata
storage, and includes a custom DAG named `lab1_pipeline`.

## Project Structure

```text
.
├── dags/
│   └── lab1_pipeline.py
├── CHANGES.md
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
└── docker-compose.yml
```

## What the DAG Does

The `lab1_pipeline` DAG:

1. Generates a fixed list of integers.
2. Validates the input data.
3. Calculates basic statistics.
4. Prints the final report to the task logs.

## Change Log

Repository changes for each laboratory stage are tracked in `CHANGES.md`.

## Requirements

- Docker
- Docker Compose

## Quick Start

1. Create a local environment file:

   ```bash
   cp .env.example .env
   ```

2. Create a directory for Airflow logs:

   ```bash
   mkdir -p logs
   ```

3. Initialize the Airflow metadata database and create the admin user:

   ```bash
   docker compose up airflow-init
   ```

4. Start the remaining services:

   ```bash
   docker compose up -d
   ```

5. Open Airflow in the browser:

   `http://localhost:8080`

6. Sign in with the credentials from `.env`:

   - Username: `airflow`
   - Password: `airflow`

## How to Run the DAG

1. Open the Airflow UI.
2. Find the DAG `lab1_pipeline`.
3. Unpause it if needed.
4. Trigger a manual run.
5. Open the task logs to confirm that the report was generated successfully.

## Stop the Environment

```bash
docker compose down
```

To also remove the PostgreSQL volume:

```bash
docker compose down -v
```
