import os
import time
import json
from modules.run_jmeter import run_jmeter

if __name__ == "__main__":
    # Load JSON file
    with open("setting.json", "r") as file:
        setting = json.load(file)

    test_plan = setting["test_plan"]
    result_base_folder = setting["result_base_folder"]
    while True:
        custom_folder_name = input(
            "Enter the name of the output folder: "
        )  # Enter the name of the custom folder
        # Check if the input is an empty string
        if custom_folder_name.strip():
            break  # If the input is not an empty string, exit the loop

    # Execute the test plan with each property setting
    for properties in setting["property_sets"]:
        for i in range(setting["loop_count_per_set"]):
            dir_name = (
                "_".join([f"{k}_{v}" for k, v in properties.items()]) + f"_exec_{i+1}"
            )
            output_folder = os.path.join(
                result_base_folder, custom_folder_name, dir_name
            )

            # Execute jmeter
            run_jmeter(
                test_plan,
                properties,
                result_base_folder,
                os.path.join(custom_folder_name, dir_name),
                i + 1,
            )

            # Wait for the specified delay time
            if setting["wait_time"] > 0:
                print(
                    f"Waiting for {setting['wait_time']} seconds before next execution..."
                )
                time.sleep(setting["wait_time"])
