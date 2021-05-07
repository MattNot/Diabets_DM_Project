import pandas as pd


def dataNormalization(row):
    if row['age'] == "[0-10)":
        row['age'] = 0
    elif row['age'] == "[10-20)":
        row['age'] = 10
    elif row['age'] == "[20-30)":
        row['age'] = 20
    elif row['age'] == "[30-40)":
        row['age'] = 30
    elif row['age'] == "[40-50)":
        row['age'] = 40
    elif row['age'] == "[50-60)":
        row['age'] = 50
    elif row['age'] == "[60-70)":
        row['age'] = 60
    elif row['age'] == "[70-80)":
        row['age'] = 70
    elif row['age'] == "[80-90)":
        row['age'] = 80
    elif row['age'] == "[90-100)":
        row['age'] = 90

    if row['gender'] == 'Male':
        row['gender'] = 0
    elif row['gender'] == 'Female':
        row['gender'] = 1

    if row['readmitted'] == '>30':
        row['readmitted'] = 'NO'
    return row


if __name__ == '__main__':
    csv = pd.read_csv("dataset_diabetes/diabetic_data.csv", index_col='encounter_id')
    csv = csv.apply(dataNormalization, axis=1)
