# Rain in Australia

## About Dataset

### Context

Ever wondered if you should carry an umbrella tomorrow? With this dataset, you can predict **next-day rain** by training classification models on the target variable  **RainTomorrow** .

### Content

This dataset comprises about 10 years of daily weather observations from numerous locations across Australia.

**RainTomorrow is the target variable to predict. It answers the crucial question: will it rain the next day? (Yes or No).**

* This column is marked 'Yes' if the rain for that day was 1mm or more.

### Source & Acknowledgements

The observations were gathered from a multitude of weather stations. You can access daily observations from [http://www.bom.gov.au/climate/data](http://www.bom.gov.au/climate/data).
For example, you can check the latest weather observations in Canberra here: [Canberra Weather](http://www.bom.gov.au/climate/dwo/IDCJDW2801.latest.shtml).

Definitions have been adapted from the Bureau of Meteorology's [Climate Data Online](http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml).
Data source: [Climate Data](http://www.bom.gov.au/climate/dwo/) and [Climate Data Online](http://www.bom.gov.au/climate/data).

Copyright Commonwealth of Australia 2010, Bureau of Meteorology.

#### Model used

###### XGBoost Classifier

###### Accuracy Score: 85%




#### STEPS:

[](https://github.com/AIAkashMukherjee/Student-Performance#steps)

Clone the repository

```shell
https://github.com/AIAkashMukherjee/Rain-in-Australia
```

### STEP 01- Create a environment after opening the repository

[](https://github.com/AIAkashMukherjee/Student-Performance#step-01--create-a-environment-after-opening-the-repository)

```shell
virtualenv my_env
```

```shell
source ml_package/bin/activate
```

### STEP 02- install the requirements

[](https://github.com/AIAkashMukherjee/Student-Performance#step-02--install-the-requirements)

```
[https://github.com/AIAkashMukherjee/Student-Performance.git]
```

```shell
pip install -r requirements.txt
```

```shell

```
