# How To Contribute

To contribute to the project, follow these steps:

1. Create an experiment using Hydrogen Torch for a dataset.
2. Download log files generated from the experiment.
3. Capture screenshots of train visualization, charts, and validation predictions.
4. Create a folder in `Assets/use-cases` with the correct dataset name.
5. Organize files in the folder:
   - Logs Files as a folder (extracted from downloaded zip)
   - Validation Predictions Screenshot as `Validation Predictions.png`
   - Charts Screenshot as `chart.png`
   - Train Data Screenshot as `train data.png`
   - Relevant Cover Image as `cover.*`
6. Update the CSV file in `Assets/metadata/use_cases.csv` with the new use case details.
7. Run the `Assets/metadata/util.py` to update the readme files.
   - `master_readme` to update the readme of master.
   - `individual_usecases` to create individual readme for your usecase.
   - `html_generator` to update the `index.html` file.
9. Make a pull request to submit your contribution.

By following these steps, you can contribute to this project.
