# RESUME-PARSER
A Tool use to automatically extract, structure, and analyze information from resumes to make the hiring process more efficient.

### Why we build this
- A Resume Parser helps organizations eliminate the error-prone and time-consuming process and improves recruiters' efficiency.

- Resume parsing technology converts an unstructured form of resume data into a structured format.

### Steps

- Step 1: Prepare and convert raw data into .spacy forma
```python
python3 src/main.py
```

- Step 2: Generate full training config from base config
```python
python3 -m spacy init fill-config data/train/base_config.cfg data/train/config.cfg 
```
- Step 3: Train the model using your data and config
```python
python3 -m spacy train data/train/config.cfg --output ./output --paths.train ./train_data.spacy --paths.dev ./test_data.spacy --gpu-id 0
```