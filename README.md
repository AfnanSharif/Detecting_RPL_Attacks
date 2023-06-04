# Machine Learning Algorithm for IoT Devices Vulnerability Detection

📚 **Overview**
These machine learning algorithms were developed as part of a master's thesis titled "Comparison of Machine Learning Algorithms to Detect RPL-Based IoT Devices Vulnerability". The purpose of these algorithms is to detect attacks on IoT devices based on the RPL protocol. 

📝 **Introduction**
The algorithms are designed to analyze meaningful datasets obtained from raw data. The data preprocessing steps, including data extraction and normalization, are performed before applying the machine learning algorithms. The algorithms are trained and tested using labeled datasets containing benign and malicious IoT motes.

🔍 **Dataset Preparation**
Two CSV files are required for the algorithms:
1. Dataset with benign IoT motes (labeled as 0)
2. Dataset with a malicious mote (labeled as 1)

To ensure a balanced dataset, an equal number of rows are randomly selected from each dataset. The source and destination IP addresses are extracted from the datasets before normalization to prevent the machine from learning the attacks based on these addresses. The data is then normalized using the StandardScaler library in Python.

🧩 **Algorithm Selection**
The datasets are split into training and testing sets in a 2:1 ratio (2/3 training, 1/3 testing). Six different machine learning algorithms are tested to determine the most appropriate algorithm for detecting Flooding, Version Number Increase, and Decreased Rank Attack in the RPL protocol:

1. Logistic Regression Classification
2. Decision Trees
3. Random Forest
4. Naive Bayes
5. KNN Classifier
6. Artificial Neural Networks

⏱️ **Performance Evaluation**
The algorithms' performance is evaluated based on accuracy rate and training time. The accuracy rate (AR) is calculated using the True Positive (TP), True Negative (TN), False Positive (FP), and False Negative (FN) values obtained from the confusion matrix.

⚙️ **Implementation**
No code is provided here. Please refer to the actual code file for implementation details.

## Results

Here are the accuracy rates and training times for each algorithm:

- Logistic Regression Classification:
  - Accuracy Rate: [accuracy_rate_lr]
  - Training Time: [training_time_lr] ms

- Random Forest Classification:
  - Accuracy Rate: [accuracy_rate_rfc]
  - Training Time: [training_time_rfc] ms

- Decision Tree Classifier:
  - Accuracy Rate: [accuracy_rate_dtc]
  - Training Time: [training_time_dtc] ms

- Naive Bayes Classifier:
  - Accuracy Rate: [accuracy_rate_nb]
  - Training Time: [training_time_nb] ms

- KNN Classifier:
  - Accuracy Rate: [accuracy_rate_knn]
  - Training Time: [training_time_knn] ms

- Deep Learning:
  - Accuracy Rate: [accuracy_rate_dl]
  - Training Time: [training_time_dl] ms

Note: The performance of each algorithm is not represented using Big O notation or big omega notation, as time is used as an indicator in this experiment.

📝 **Author**
This code was developed by Murat Ugur KIRAZ as part of a master's thesis.

For further details, please refer to the actual code file and the thesis documentation.