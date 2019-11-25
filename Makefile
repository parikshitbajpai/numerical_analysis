RUN_A3_PATH=./Assignment_3/src/
REPORT_A1_PATH=./Assignment_3/latex/
RUN_A1_PATH=./Assignment_1/src/
REPORT_A1_PATH=./Assignment_1/latex/

run-random:
	python $(RUN_A3_PATH)main_random.py

run-ones:
	python $(RUN_A3_PATH)main_ones.py

run-A1:
	python $(RUN_A1_PATH)run_cofactor-lu.py
	python $(RUN_A1_PATH)run_lu.py

run-lu:
	python $(RUN_A1_PATH)run_lu.py

	run-cofactor:
		python $(RUN_A1_PATH)run_cofactor-lu.py

clean:
	find $(RUN_A3_PATH) -name '*.pyc' -exec rm --force {} +
	find $(RUN_A3_PATH) -name '*.pyo' -exec rm --force {} +
	find $(RUN_A3_PATH) -name '*~' -exec rm --force  {}
	find $(RUN_A1_PATH) -name '*.pyc' -exec rm --force {} +
	find $(RUN_A1_PATH) -name '*.pyo' -exec rm --force {} +
	find $(RUN_A1_PATH) -name '*~' -exec rm --force  {}
