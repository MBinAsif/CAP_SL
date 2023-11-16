# Car Acceptability Prediction using SpaCy and Streamlit

This project involves predicting the acceptability of cars based on various features using a trained SpaCy model deployed with Streamlit.

## Overview

The repository contains code for a machine learning model that predicts the acceptability of cars based on multiple features such as buying price, maintenance price, number of doors, person capacity, size of luggage, and safety. The machine learning model is trained using SpaCy and deployed using Streamlit.

### Dataset Information

The dataset used for training and testing the model contains information about various car features:

- **Buying_Price**: Categories representing the buying price of the car ('vhigh', 'high', 'med', 'low').
- **Maintenance_Price**: Categories representing the maintenance price of the car ('vhigh', 'high', 'med', 'low').
- **No_of_Doors**: Number of doors in the car ('2', '3', '4', '5more').
- **Person_Capacity**: Person capacity of the car ('2', '4', 'more').
- **Size_of_Luggage**: Size of luggage ('small', 'med', 'big').
- **Safety**: Safety rating ('low', 'med', 'high').
- **Car_Acceptability**: Target variable representing the acceptability of the car ('unacc', 'acc', 'good', 'vgood').

The dataset is available in the [data folder](./data) of this repository.

### SpaCy Model Information

The machine learning model is built using the SpaCy library for natural language processing. The trained SpaCy model is used for predicting the acceptability of cars based on the provided features. For detailed information about the training process and the SpaCy model, refer to the [training model repository](https://github.com/MBinAsif/CAP).

### Streamlit Deployment

The trained SpaCy model is deployed using Streamlit, allowing users to interactively input car features and obtain predictions regarding car acceptability.

## Usage

To use the car acceptability prediction model:

1. Clone this repository:

   ```bash
   git clone https://github.com/YourUsername/YourRepository.git
   cd YourRepository
2. Install the required dependencies:
   pip install -r requirements.txt
3. Run the Streamlit app:
   streamlit run app.py
4. Access the Streamlit app in your web browser at http://localhost:8501.

### Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository, create a new branch, make your changes, and open a pull request.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For more information about the training process and the SpaCy model, refer to the training model repository.
For any questions or suggestions, feel free to open an issue in this repository.


Replace placeholders such as `YourUsername`, `YourRepository`, and update the description with specific details about your dataset and models. Additionally, provide accurate links and information about the model training repository for users who want to explore more about the training process.
