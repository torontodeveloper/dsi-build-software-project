# Tests for Analysis Package

Introduction
This document outlines the testing strategy for the Analysis package, which interacts with the New York Times API and performs data analysis.

Unit Tests

Initialization Tests

Test Config Loading: Ensure analysis_config correctly loads the configuration from YAML files.

Argument Parsing: Verify that the command-line arguments are correctly parsed and used.

API Interaction Tests
URL Formation: Test if the URL is correctly formed with the topic and API key.

API Response: Mock API responses to test how the package handles different response scenarios (e.g., success, failure, unexpected data).

Data Processing Tests
Data Loading: Test load_data to ensure it correctly paginates and aggregates articles.

Year Extraction: Validate the extract_year_from_pub_date function for correct year extraction from publication dates.

Plotting Tests
Plot Data: Test the plot_data method, ensuring it correctly processes data and generates a plot. This may require a visual inspection.

Integration Tests
End-to-End Test: Perform an end-to-end test of the package, from initialization to plotting, using a mock API.

Non-Automated Tests
Visual Verification of Plots: Manually check the generated plots for correctness.

Real API Interaction: Test the package with the real NY Times API (requires valid API key) and manually verify the output.

Tests for config.yml
Introduction
This document outlines the testing strategy for the config.yml file used in our Python package.

Tests
Format and Readability Tests
YAML Syntax: Validate the YAML syntax is correct and free of errors.
Required Fields: Check that all required fields (like api_key, url, etc.) are present.
Integration Tests with Python Code
Config Loading: Test loading the config.yml file in Python to ensure it's correctly parsed.
Field Accessibility: Verify that each configuration field is accessible and correctly interpreted by the Python code.
Validation Tests
Field Value Validation: Ensure that the values of fields (like URL formats, API keys) are valid and in the expected format.

# Test Documentation

## Overview
This document provides detailed information about the unit tests in the project. 
All test files are located within the `tests` directory at the root of the project.

## Test Files

- `test_analysis.py`: Contains unit tests for the Analysis class and its methods. 

## Running Tests

To run the tests, follow these steps:

1. Navigate to the root directory of the project.
2. Activate the virtual environment if you are using one.
3. Run the tests using the following command:

   ```bash
   python -m unittest


Tests
pytest

E   SystemExit: 2
----------------------------------------------------------------------------------------------------------------- Captured stderr ------------------------------------------------------------------------------------------------------------------ 
usage: pytest [-h] job_config
pytest: error: the following arguments are required: job_config
============================================================================================================= short test summary info ============================================================================================================== 
ERROR assignmentpkg/test_analysis.py - SystemExit: 2
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
================================================================================================================= 1 error in 0.88s ================================================================================================================= 

Test for functions
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

Published article test

.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
Analysis

The single dot . signifies that one test was run and it passed.

The dot (.) signifies that one test was executed and it passed.

NYT API mock call

Ran 1 test in 0.002s shows the test was completed very quickly.

OK confirms that there were no failures or errors in the test.

