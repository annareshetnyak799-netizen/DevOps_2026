# Changes

All notable repository changes are documented in this file.

## [Lab 2] - 2026-05-03

### Added

- PySpark job `spark_job.py` in a new `spark/` directory.
- New DAG `lab2_pipeline` using `SparkSubmitOperator` to submit the Spark job.
- `spark-master` and `spark-worker` services in `docker-compose.yml`.
- `./spark:/opt/airflow/spark` volume mount for all Airflow services.

### Updated

- `Dockerfile` to install `procps` and `default-jre` via apt (as root) and `pyspark==3.5.0` and `apache-airflow-providers-apache-spark==4.1.1` via pip.
- `docker-compose.yml` with Spark services and updated startup order.
- `README.md` with Lab 2 description, project structure, and Spark connection setup instructions.

### Verified

- Successful startup of spark-master and spark-worker containers.
- Successful execution of the `lab2_pipeline` DAG in the Airflow UI.
- Completed Spark application visible in the Spark UI at `http://localhost:4040`.

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
