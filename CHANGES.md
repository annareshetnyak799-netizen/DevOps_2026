# Changes

All notable repository changes are documented in this file.

## [Lab 1] - 2026-05-03

### Added

- Initial project structure for the `Airflow + Docker Compose` laboratory work.
- Custom `Dockerfile` based on `apache/airflow:2.7.1`.
- `docker-compose.yml` with `postgres`, `airflow-init`, `airflow-webserver`,
  and `airflow-scheduler` services.
- Example environment template in `.env.example`.
- Custom DAG `lab1_pipeline` with multiple tasks and basic calculations.
- `README.md` with local setup and run instructions.

### Configured

- `LocalExecutor` as the Airflow executor.
- PostgreSQL as the Airflow metadata database.
- Disabled example DAGs with `AIRFLOW__CORE__LOAD_EXAMPLES=false`.
- Custom Airflow web UI credentials through environment variables.

### Verified

- Airflow metadata database initialization and migrations.
- Successful startup of the Airflow webserver and scheduler.
- Successful execution of the `lab1_pipeline` DAG in the Airflow UI.
