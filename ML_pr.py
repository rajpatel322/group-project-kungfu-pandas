
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd 


def feature_selection_and_evaluation(X_train, y_train):
    
    encoder = OneHotEncoder()
    k_folds = KFold(n_splits=4, shuffle=True, random_state=42)
    combination = [['Primary Type'], ['Primary Type', 'Location Description'], ['Primary Type', 'Location Description', 'RegionName'], ['Location Description'],['Location Description','RegionName'],['RegionName'], ['Primary Type','RegionName' ]]
    avg_accuracy = []

    for features in combination:
        X_encoded = encoder.fit_transform(X_train[features]) # convert the string type to float for ML Model
        accuracies = []
        
        for train_idx, val_idx in k_folds.split(X_encoded):
            # train_fold is for training and val_fold is for validation
            X_train_fold, X_val_fold = X_encoded[train_idx], X_encoded[val_idx] #Iterates over each combination, encoding the features, and perform k-fold cross-validation
            y_train_fold, y_val_fold = y_train.iloc[train_idx], y_train.iloc[val_idx]

            model = LogisticRegression(random_state=42, solver='sag', penalty='l2', C=1.0)  
            model.fit(X_train_fold, y_train_fold)
            
            y_pred_val = model.predict(X_val_fold)
            accuracy = accuracy_score(y_val_fold, y_pred_val)
            accuracies.append(accuracy)
        
        avg_accuracy.append(sum(accuracies) / len(accuracies))

    best_index = avg_accuracy.index(max(avg_accuracy))
    best_combination = combination[best_index]
    best_accuracy = avg_accuracy[best_index]
    return best_combination, best_accuracy
