#!/bin/sh
python -m src.db.create_table

python -m src.jobs.sinapi_job
