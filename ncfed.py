import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset_1 = pd.read_csv('apartments_for_rent_classified_10K.csv', encoding='latin1' , delimiter=';')
dataset_2 = pd.read_csv('apartments_for_rent_classified_100K.csv', encoding='latin1' , delimiter=';')

print(dataset_1['amenities'])