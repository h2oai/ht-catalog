import os
import yaml

import pandas as pd

ASSETS_URL = "https://github.com/h2oai/HT-Catalog/blob/1432be958ab3f41b67c57c241b946b4a3d4699e1/Assets/"
UCS_FOLDER_PATH = "DL_Models/"
UC_CSV_FILE = "docs/use_cases.csv"


def get_cfg_log_dict(uc_id, dataset):
    folder_path = f"{UCS_FOLDER_PATH}{uc_id}_{dataset}"
    usecase_files = os.listdir(folder_path)
    for usecase_file in usecase_files:
        if "logs" in usecase_file:
            folder_path = f"{folder_path}/{usecase_file}"
            log_files = os.listdir(folder_path)
            for log_file in log_files:
                if "cfg" in log_file:
                    yaml_file_path = f"{folder_path}/{log_file}"
                    break
            break

    with open(yaml_file_path, 'r') as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
    return yaml_dict


uc_df = pd.read_csv(UC_CSV_FILE)

for idx, uc in uc_df.iterrows():
    UC_FOLDER_PATH = f"{UCS_FOLDER_PATH}{uc['Sr. No']}_{uc['Dataset']}/"
    UC_FOLDER_URL = f"{ASSETS_URL}{UC_FOLDER_PATH.replace(' ', '%20')}"

    cfg_log_dict = get_cfg_log_dict(uc['Sr. No'], uc['Dataset'])

    readme_content = f"""\
# {uc['Usecase'].upper()}
### {uc['Industry']} | {uc['Data Type']} | {uc['Problem Type']}

![]({UC_FOLDER_URL}cover.png)
![]({UC_FOLDER_URL}cover.jpg)
![]({UC_FOLDER_URL}cover.jpeg)
![]({UC_FOLDER_URL}cover.webp)
![]({UC_FOLDER_URL}cover)

### BUSINESS PROBLEM
<p style='text-align: justify; text-indent: 30px;'>{uc['Use Case Description']}.</p>

### BUSINESS IMPACT
<p style='text-align: justify; text-indent: 30px;'>{uc['Business Impact']}.</p>

### DATASET
- {uc['Dataset'].capitalize()} dataset has been used.
- You can access the dataset [here]({uc['Dataset Link']}).
- {uc['Dataset Description (1 liner)']}.

![train data]({UC_FOLDER_URL}train%20data.png)

### PREDICTION OUTPUT
<p style='text-align: justify; text-indent: 30px;'>{uc['Prediction Target']}.</p>

### MODEL TRAINING
<p style='font-family:JackInput Regular;'><b>Architecture</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>backbone: {cfg_log_dict['architecture'].get('backbone', None)}</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>pretrained: {cfg_log_dict['architecture']['pretrained']}</p>

<p style='font-family:JackInput Regular;'><b>Training</b></p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>batch_size: {cfg_log_dict['training']['batch_size']}</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>epochs: {cfg_log_dict['training']['epochs']}</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>gradient_clip: {cfg_log_dict['training']['gradient_clip']}</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>learning_rate: {cfg_log_dict['training']['learning_rate']}</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>optimizer: {cfg_log_dict['training']['optimizer']}</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>schedule: {cfg_log_dict['training']['schedule']}</p>
<p style='text-align: justify; text-indent: 30px;font-family:JackInput Regular;'>weight_decay: {cfg_log_dict['training']['weight_decay']}</p>

![chart]({UC_FOLDER_URL}chart.png)

### MODEL PREDICTIONS

![Validation Predictions]({UC_FOLDER_URL}Validation%20Predictions.png)

### LICENSE
<p style='text-align: justify; text-indent: 30px;'>{uc['License']}</p>
    """

    with open(f"{UC_FOLDER_PATH}README.md", "w") as readme_f:
        readme_f.write(readme_content)
