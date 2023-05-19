# Initialize your population

We create a dummy population... from public statistics and a lot of approximations!!!

## Households
Realistic distribution of households are inspired from [American statistics (United States Census Bureau)](https://data.census.gov/cedsci/table?q=Families%20and%20Living%20Arrangements&tid=ACSDP1Y2018.DP02&vintage=2018&layer=VT_2018_040_00_PY_D1)

Let `P` be the population.

1. Load notebook `1 Households hypothetical dataset.ipynb`
2. Set your desired `P` 
3. Run the cells.

This notebook creates `households.csv` file with 4 types of households and 6 fields. the first one is the index of the pandas.DataFrame
~~~
,nb_children,nb_adults,type,size 
0,1,2,two_parent_family,3.0
1,3,2,two_parent_family,5.0
2,5,2,two_parent_family,7.0
...
1858,1,1,single_parent_family,2.0
1859,1,1,single_parent_family,2.0
...
2627,0,4.0,roomates_household,4.0
2628,0,3.0,roomates_household,3.0
...
3434,0,1,leaving_alone,1
3435,0,1,leaving_alone,1
~~~
NB: The final population may differ from `P` as with create random adults and children according to distribution laws. `P` is used to create the number of households of each types. Their composition is drawn with probabilitic functions.


## Create people id and their professional contact number 

Here we create nodes id and their "professional" degree.

1. Load notebook `2 contacts.ipynb`
2. Run the cells.

From the households' composition (`households.csv`, previous step), we create `adult_ids` and `child_ids`, the nodes of our graphs.

But we also create a profesionnal life to these nodes.

Professional contacts: 

* For children, we assign a number of contacts in school. 
* For adults, we assign a line of business and number of contacts when they are at work , or `(NaN,0)` if they don't have a job

Sources: 

* [Insee](https://www.insee.fr/fr/statistiques/2582785?sommaire=2587886), onglets population active, emploi par activité
* File `Donnees_Emploi_par_taille_unite_legale_et_secteur_2009_et_2010.xls`
* [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/la-taille-des-colleges-et-lycees/)

This notebook creates `pro_contacts_adults.csv`
~~~
household_id,adult_id,job_cat,pro_contacts,company_id
0,0,Services_other,888,43.0
0,1,Administration_schools,15,48.0
1,2,Shops_mecanics,5,75.0
1,3,Indus_food,44,10.0
2,4,Health,243,2.0
2,5,Administration_schools,82,33.0
2,6,Shops_mecanics,5,137.0
3,8,Administration_schools,68,4.0
4,9,Agriculture_fishing,2,64.0
4,10,,0,
5,11,Indus_other,42,18.0

~~~

This notebook creates also `pro_contacts_children.csv`
~~~
household_id,child_id,school_contacts,school_id
0,6960,93,2
0,6961,43,1
1,6962,99,2
3,6963,74,0
3,6964,30,3
4,6965,33,9
4,6966,20,0
7,6967,37,8
~~~


## Design strategies to fight COVID-19

1. Create the graphs corresponding to the situations you want to simulate, i.e. different kind of confinement.
2. Implement an epidemic model
3. Simulate the outbreak diffusion (non stochastic systems, so run 10, 100 times your models
4. For each scenario and each simulation : measure loss in terms of deaths, infectious rate, recovery rate, but also economic indicators you will define. Provide a synthetic table with your results and maybe you should send them to our President de la République ;-)

### Graphs

It's up to you to create:

* Households graphs (cliques)
* Friendship graphs for adults and children (NetworkX provides many Network Models, such as Preferential Attachment)
* Professional graphs with the ids of companies/schools
* Add a transportation layer if you want...

> Be creative, autonomous, take initiative: modify the way of creating your population (size, but also number of contacts. Test with different population size, networks models, diffusion models, etc.

### Epidemic model

* `R0=2.5`:  the average number of individuals infected by an infected person
* Between 1% and 3% infected individuals will die (estimations; [How epidemiologic models are designed, CNRS](https://news.cnrs.fr/articles/covid-19-how-are-epidemic-models-designed))
* Estimate SIR model parameters from cases data (Confirmed, Deaths, Recovered): the `infection rate β` and the `recovery rate μ`
[A blog post with code and data to estimate these parameter for France](https://www.lewuathe.com/covid-19-dynamics-with-sir-model.html)
[The Humanitarian Data Exchange: COVID-19 cases data](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases)

### KPI
`Point_de_conjoncture_INSEE_26mars2020_7h30.pdf` gives some information on economic losses. 



