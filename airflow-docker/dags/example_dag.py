from datetime import datetime
from email.mime import image
from enum import auto
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

with DAG(
    dag_id="exemplo-dag-docker",
    schedule_interval=None,
    start_date=datetime(2022,9,20)
) as dag:

    message_and_save_csv_task = DockerOperator(
        docker_url="tcp://docker-socket-proxy:2375",
        auto_remove=False,
        image="docker-operator-etl:latest",
        task_id="message_and_save_csv",
        command="src/task.py",
        force_pull=False,
        mounts=[Mount('/app/data', r'#SEU DIRETÓRIO', type='bind')]
    )

if __name__ == "__main__":
    dag.cli()
