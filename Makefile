RUN_PATH=./Assignment_1/src/
REPORT_PATH=./Assignment_1/latex/

run:
	python $(RUN_PATH)run_cofactor-lu.py
	python $(RUN_PATH)run_lu.py

run-lu:
	python $(RUN_PATH)run_lu.py

run-cofactor:
	python $(RUN_PATH)run_cofactor-lu.py

clean:
	find $(RUN_PATH) -name '*.pyc' -exec rm --force {} +
	find $(RUN_PATH) -name '*.pyo' -exec rm --force {} +
	find $(RUN_PATH) -name '*~' -exec rm --force  {}
