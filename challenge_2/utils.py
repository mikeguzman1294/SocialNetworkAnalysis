import networkx
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import truncnorm
import math

import matplotlib.pyplot as plt
import pandas as pd
import random

houses = pd.read_csv('households.csv')
pro_contacts_adults = pd.read_csv('pro_contacts_adults.csv')
pro_contacts_children = pd.read_csv('pro_contacts_children.csv')

def get_household(id):
    id = int(id)
    if id < 6960 :
        adult = True
    else:
        adult = False
    if adult:
        #get the household from pro_contacts_adults
        household_id = pro_contacts_adults.loc[pro_contacts_adults['adult_id'] == id]['household_id'].values[0]
    else :
        #get the household from pro_contacts_children
        household_id = pro_contacts_children.loc[pro_contacts_children['child_id'] == id]['household_id'].values[0]
    return household_id

def get_job(id):
    id = int(id)
    if id < 6960 :
        adult = True
    else:
        adult = False
    if adult:
        #get the job from pro_contacts_adults
        job = pro_contacts_adults.loc[pro_contacts_adults['adult_id'] == id]['job_cat'].values[0]
    else :
        #get the job from pro_contacts_children
        job = "Student"
    return job

def get_job_cat(job):
   
    if job in ['Indus_food','Agriculture_fishing','Shops_market_food']:
        return "agriculture_and_agro_food_processing"
    elif job in ['Indus_other']:
        return "industries_except_agro_food_processing"
    elif job in ['Construction']:
        return "construction"
    elif job in ['Administration_schools','Services_other','Health']:
        return "non_market_services"
    elif job in ['Transportation','Shops_other','Hotel_Restaurant']:
        return "market_services"
    else :
        return "Student or unemployed"
