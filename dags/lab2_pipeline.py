"""Airflow DAG for lab 2: submits a PySpark job to a Spark cluster."""

import pendulum
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG(
    dag_id="lab2_pipeline",
    schedule=None,
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["lab2", "spark"],
    description="Submit a PySpark job to the Spark cluster.",
) as dag:
    spark_job = SparkSubmitOperator(
        task_id="spark_job",
        application="/opt/airflow/spark/spark_job.py",
        name="lab2_spark_job",
        conn_id="spark_local",
        dag=dag,
    )
