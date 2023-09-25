## Environment
java 11.0.18 2023-01-17 LTS
jmeter 5.5 (5.6 has a bug in CLI and does not work correctly)
python 3.11.1

## Performance Verification
### Setting up jmeter
1. Create a Test Plan
2. Parameterize the parameters you want to change
    - Set as follows in User Defined Variables  
    `parameter_name | ${__P(parameter_name)} | description`
    - Set the configured variables in the corresponding places
### Directory Structure
- jmeter: A place for jmeter's jmx, etc.
    - performanceTest.jmx: Performance verification content setting file (It is preferable to edit in GUI and execute with the following code groups)
- modules: Modules used in performance_test_for_XXXX.py
- results: A place to output the verification results
    - combined_statistics.py: Outputs the contents of statistics.json located under the specified directory in a list to csv. Use when you want to summarize the verification results in Excel
- performance_test_template.py: A template to customize according to each performance test (You can use this if there is no need to customize)
- setting.json: Performance verification setting file

### Setting up setting.json
- property_sets
    - You can specify the properties to pass to jmx.
    - The contents of the properties can be changed with user definitions on the jmeter side.
- loop_count_per_set
    - Set how many times to repeat each set configured in property_sets.
    - For example, if you set 3, you will start jmeter with the same settings three times for one set. Then move on to the next set.
- wait_time
    - Set how much time to leave before running jmeter continuously. The unit is seconds.
    - Setting this considering CPU credits, etc., can be expected to recover.
- result_base_folder
    - You can set the folder to output the results.
- test_plan
    - Specify the file of jmeter's test plan.

### Execution
1. Run the created `python performance_test_for_XXXX.py` for performance verification
2. After execution, accept the input to specify the result output destination, and enter any name  
(No need to create a directory in advance)

## Viewing the Results
1. Move to results (result output directory)
2. `python -m http.server`
3. Go to http://localhost:8000

## Outputting in a List to CSV (For Inserting into Excel)
1. Move to results (result output directory)
2. Change the root_dir (line 5) of combined_statistics.py to the directory you want to list the results
3. Run `python combined_statistics.py`
4. Load combined_statics.csv into Excel
