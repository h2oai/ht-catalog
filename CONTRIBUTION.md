# How To Contribute

To contribute to the project, follow these steps:

### Add a new use-case 

1. Create the Hydrogen Torch experiment for your use-case and download the following artifacts:
   - download logs files of the experiments
   - capture screenshots: train visualization, charts, and validation predictions
2. Create a new folder folder in `Assets/use-cases` with the correct name (no spacing), add following files:
   - logs files as a folder (extracted from downloaded zip)
   - charts screenshot as `chart.png`
   - validation predictions screenshot as `Validation Predictions.png`
   - train data screenshot as `train data.png`
   - relevant cover image as `cover.*`

### Update the webpage, use-case readme, and main readme

1. Update the master csv file in `Assets/metadata/use_cases.csv` with the new use case details
2. Run the python file `Assets/metadata/util.py` to update the readme files.
   - `master_readme` to update the readme of master.
   - `individual_usecases` to create individual readme for your usecase.
   - `html_generator` to update the `index.html` file.


After verifying these changes, make a pull request to submit your contribution