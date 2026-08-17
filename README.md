# Wall-Following Robot Navigation - Neural Network Classifier

## Setup
1. Open this folder in VS Code / Antigravity.
2. Terminal: python -m venv venv
3. Activate: venv\Scripts\activate (Windows) or source venv/bin/activate (Mac/Linux)
4. Install: pip install -r requirements.txt
5. Run: python wall_following_mlp.py


## Instructions
```bash
python -m venv venv
```
```bash
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```
```bash
venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```
```bash
python wall_following_mlp.py
```


output:
```bash
Dataset shape: (5456, 24)

Class distribution:
 Class
Move-Forward         2205
Sharp-Right-Turn     2097
Slight-Right-Turn     826
Slight-Left-Turn      328
Name: count, dtype: int64

Test Accuracy: 90.66%

Classification Report:
                   precision    recall  f1-score   support

     Move-Forward       0.90      0.91      0.91       454
 Sharp-Right-Turn       0.93      0.93      0.93       427
 Slight-Left-Turn       0.93      0.85      0.89        60
Slight-Right-Turn       0.84      0.87      0.85       151

Test Accuracy: 90.66%

Classification Report:
                   precision    recall  f1-score   support

     Move-Forward       0.90      0.91      0.91       454
 Sharp-Right-Turn       0.93      0.93      0.93       427
 Slight-Left-Turn       0.93      0.85      0.89        60
Slight-Right-Turn       0.84      0.87      0.85       151

                   precision    recall  f1-score   support

     Move-Forward       0.90      0.91      0.91       454
 Sharp-Right-Turn       0.93      0.93      0.93       427
 Slight-Left-Turn       0.93      0.85      0.89        60
Slight-Right-Turn       0.84      0.87      0.85       151


     Move-Forward       0.90      0.91      0.91       454
 Sharp-Right-Turn       0.93      0.93      0.93       427
 Slight-Left-Turn       0.93      0.85      0.89        60
Slight-Right-Turn       0.84      0.87      0.85       151

     Move-Forward       0.90      0.91      0.91       454
 Sharp-Right-Turn       0.93      0.93      0.93       427
 Slight-Left-Turn       0.93      0.85      0.89        60
Slight-Right-Turn       0.84      0.87      0.85       151

 Sharp-Right-Turn       0.93      0.93      0.93       427
 Slight-Left-Turn       0.93      0.85      0.89        60
Slight-Right-Turn       0.84      0.87      0.85       151

 Slight-Left-Turn       0.93      0.85      0.89        60
Slight-Right-Turn       0.84      0.87      0.85       151

Slight-Right-Turn       0.84      0.87      0.85       151


         accuracy                           0.91      1092
         accuracy                           0.91      1092
        macro avg       0.90      0.89      0.89      1092
     weighted avg       0.91      0.91      0.91      1092
```
