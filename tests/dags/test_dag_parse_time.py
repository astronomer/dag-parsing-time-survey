import datetime
from airflow.models import DagBag

def test_dag_load_times():
    dagbag = DagBag()
    for dag_id, dag in dagbag.dags.items():
        start_time = datetime.datetime.now()
        dagbag.process_file(dag.fileloc)
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        errors = []
        if duration < datetime.timedelta(seconds=5):
            errors.append(f"DAG {dag_id} took {duration} seconds to load")
        assert not errors,  "Dags exceeded parsing time limit:\n{}".format("\n".join(errors))