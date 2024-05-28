Overview
========

This is a set of tools for monitoring and testing dag parsing times against a benchmark.


Project Contents
================

- dags/dag_parsing_survey.py - a dag that parses all dags in the dagbag and records the parsing time to logs.
- tests/dags/test_dag_parse_time.py - a pytest that uses similar logic and fails if the parsing time exceed an arbitrary threshhold. Intended to be integrated into CICD pipelines