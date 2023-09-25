## Overview
This tool is a semi-automated performance verification tool using JMeter.
It is a very effective tool when you want to verify multiple times by changing the parameter setting patterns of JMeter's test plans.
The default features provided by this tool are as follows:
- Automatic execution of JMeter with combinations of parameter settings
- Setting the execution interval for each combination
- Setting iterations for each combination
- Automatic setting of the output destination for each execution result
- Consolidating those results into one

Also, due to its simple design, it is easy to extend optionally by embedding preprocessing and post-processing before and after JMeter execution.

## Environment
java 11.0.18 2023-01-17 LTS
jmeter 5.5 (5.6 has a bug in CLI and does not work correctly)
python 3.11.1

## Performance Verification
### JMeter Settings
1. Create a test plan
2. Parameterize the parameters you want to change
   - Set as follows in User Defined Variables
   `parameter_name | ${__P(parameter_name)} | description`
   - Set the configured variable in the appropriate place
### Directory Structure
- jmeter: A place for JMeter's jmx etc.
   - performanceTest.jmx: Performance verification content setting file (It is preferable to edit in GUI and execute with the code groups below)
- modules: Modules used in performance_test.py
   - run_jmeter.py: A module that executes JMeter.
- results: A place to output verification results
   - combined_statistics.py: Consolidates and outputs to CSV the contents of statistics.json located under the specified directory. Use when you want to consolidate verification results in Excel
- performance_test.py: The main body of the tool
- setting.json: Performance verification setting file

### Setting.json Configuration
- property_sets
   - You can specify the properties to pass to JMeter's test plan.
   - The contents of the property can be changed with JMeter's user-defined variables.
- loop_count_per_set
   - Set how many times to repeat each set configured in property_sets.
   - For example, if you set 3, JMeter will start with the same settings three times for one set. Then it moves to the next set.
- wait_time
   - Set how much time to leave before running JMeter continuously. The unit is seconds.
   - It is expected to recover when considering CPU credits, etc.
- result_base_folder
   - You can set the folder to output the results.
- test_plan
   - Specify the file of JMeter's test plan.

### Execution
1. Execute `python performance_test.py`
2. After execution, accept the input to specify the result output destination and enter any name
   (There is no need to create a directory)

## Viewing Results
1. Move to results (result output directory)
2. `python -m http.server`
3. Go to http://localhost:8000

## Outputting in CSV for a List (such as when inserting into Excel)
1. Move to results (result output directory)
2. Change the root_dir (5th line) of combined_statistics.py to the directory you want to list the results
3. Execute `python combined_statistics.py`
4. Load combined_statics.csv into Excel
