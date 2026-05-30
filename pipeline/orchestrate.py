from dagster import job, op, Nothing, In
from typing import Generator
import os

@op
def ingest() -> None:
    os.system("python pipeline/ingest.py")

@op(ins={"start": In(Nothing)})
def validate() -> None:
    os.system("python pipeline/validate.py")

@op(ins={"start": In(Nothing)})
def transform() -> None:
    os.system("cd dbt_pipeline && dbt run --profiles-dir .")

@op(ins={"start": In(Nothing)})
def test_data() -> None:
    os.system("cd dbt_pipeline && dbt test --profiles-dir .")

@job
def ventes_pipeline():
    test_data(transform(validate(ingest())))