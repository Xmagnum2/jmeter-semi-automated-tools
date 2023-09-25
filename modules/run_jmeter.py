import subprocess
import os

def run_jmeter(test_plan, properties, base_folder, custom_folder, execution_num):
    """
    Function to run JMeter CLI
    
    :param test_plan: Path to the JMeter test plan
    :param properties: Dictionary of JMeter property settings
    :param base_folder: Path to the base output folder
    :param custom_folder: Name of the additional custom folder
    :param execution_num: Number of executions
    """
    # Convert property settings to command line arguments
    prop_args = " ".join([f"-J{k}={v}" for k, v in properties.items()])
    
    # Create output folder
    output_folder = os.path.join(base_folder, custom_folder)
    os.makedirs(output_folder, exist_ok=True)
    
    # Create JMeter execution command
    cmd = f"jmeter -n -t {test_plan} {prop_args} -l {output_folder}/result.jtl -e -o {output_folder}"
    
    print("\n")
    print(cmd)
    print("\n")
    # Execute the command
    print(f"Starting JMeter test plan: {test_plan} with properties: {properties} (Execution {execution_num})")
    subprocess.run(cmd, shell=True)
    print(f"Finished JMeter test plan: {test_plan} (Execution {execution_num})")
