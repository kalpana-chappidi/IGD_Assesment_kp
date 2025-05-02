from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    'start_date': days_ago(1)
}

with DAG(
    'retail_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    start = DummyOperator(task_id='start')

    load_transactions = GCSToBigQueryOperator(
        task_id='load_transactions',
        bucket='retail-data',
        source_objects=['transactions/2025-04-30/sample_transactions.csv'],
        destination_project_dataset_table='project.dataset.staging_transactions',
        source_format='CSV',
        skip_leading_rows=1,
        write_disposition='WRITE_APPEND'
    )

    load_macro = GCSToBigQueryOperator(
        task_id='load_macro',
        bucket='retail-data',
        source_objects=['macro/sample_macro.csv'],
        destination_project_dataset_table='project.dataset.staging_macro',
        source_format='CSV',
        skip_leading_rows=1,
        write_disposition='WRITE_TRUNCATE'
    )

    end = DummyOperator(task_id='end')

    start >> [load_transactions, load_macro] >> end
