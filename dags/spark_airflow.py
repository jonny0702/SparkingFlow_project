from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

#Creating a DAG Task
dag = DAG(
    dag_id="spark_flow",
    schedule_interval="@daily",
    default_args={
        "owner": "Jonathan Vergara",
        "start_date": days_ago(1)
    }
)

start_task = PythonOperator(
    task_id= "start_task",
    python_callable= lambda: print("Just start task DAG"),
    dag= dag
)

##The Apache Airflow SparkSubmitOperator is an operator that allows users to run Spark jobs within Airflow DAGs
python_job = SparkSubmitOperator(
    task_id="python_job",
    conn_id="spark_conn", ##SPARK_CONECTION ID
    application="jobs/python/wordcountjob.py",
    name="SparkApp",
    dag=dag
)

end_task = PythonOperator(
    task_id= "end_task",
    python_callable= lambda: print("Complete succesfully"),
    dag=dag
)

start_task >> python_job >> end_task