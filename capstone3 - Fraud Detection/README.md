# Fraud Detection Prediction  
The objective of this project is Develop an accurate fraud detection prediction system using advanced analytics and machine learning techniques to identify and prevent fraudulent activities, improving financial security and minimizing losses.

# This project utilizes the following libraries and frameworks:

- [NumPy](https://github.com/numpy/numpy) - [Pandas](https://github.com/pandas-dev/pandas)
- [Matplotlib](https://github.com/matplotlib/matplotlib) - [Seaborn](https://github.com/seaborn/seaborn)
  <div>
Feel free to explore the repositories of these libraries and frameworks for more information and detailed documentation.
  </div>

# Run the project 
- To run the Jupyter Notebook in the repository on your local machine or using Google Colab.

# EDA 
| Class | Count   |
|-------|---------|
| 0     | 284,315 |
| 1     | 492     |

Considering the imbalanced nature of the data, we employed various techniques such as oversampling, undersampling, and adjusting class weights to tackle the issue. However, in real-life scenarios, it is common for fraud detection datasets to be imbalanced since fraudulent instances are typically much less frequent compared to non-fraudulent instances.

# MOdeling 

The random forest model yielded the best results among the machine learning models and the deep learning model, even without adjusting the class weights. The random forest model outperformed other models in terms of performance and achieved the highest accuracy.

 ## Optimal Hyperparameters and result for Random Forest:
 | Parameter      | Value       |
| -------------- | ----------- |
| max_depth              | 7         |

| F1_1 | Precision_1 | Recall_1 |
| ----------- | ----------------- | --------------- |
| 0.85    | 0.95         | 0.78        |

# Acknowledgements
This project is part of ML bootcamp provided by [clarusway](https://clarusway.com/)
