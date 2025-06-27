from pathlib import Path
from pytest_bdd import scenarios

if __name__ == Path(__file__).stem:
    scenarios('../features/ics_run_predefined_sample_sets.feature',
              '../features/ics_predefined_long_running_sample_sets.feature')

# all the steps are implemented in conftest, but we need this file to be able to run the feature files
