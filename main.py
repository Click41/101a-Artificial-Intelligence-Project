import pandas as pd
# will have to add in more imports as we go along depending on what we use
###scikit-learn is what we are using

def preprocess_data(dataset):
    
    # where format our data to make sure everything matches for reading
    
    return dataset 

def evaluation_model(model, x-test, y-test):
        
        # where we evaluate the model
        ## predictions
        ## accuracy
        
        return model 
    
def main():
    
    # ################ LOADING DATA SETS ################
    # reliability datasets - the col reliability_percentage = % of buses that are ON TIME (1 - % = late)
    reliability_553 = pd.read_csv('data/MBTA_Reliability_Bus553.csv')
    reliability = pd.read_csv('data/MBTA_Reliability.csv')
    # alerts - gives dates buses are receiving alerts (particularly for delays) + reason
    alerts = pd.read_csv('data/BUS_Service_Alerts.csv') 
    # gives weather (avg temp + precipitation) for boston area
    boston_weather = pd.read_csv('data/boston_weather.csv')

    ### add in extra lines for more data
    print(reliability.head())

    # call preprocessing function
    
    ### choose model
    # When we talk about choosing a model like the Random Forest Classifier, 
    # we're referring to selecting a machine learning algorithm that suits 
    # the nature of your data and the problem you're trying to solve. 
    # The Random Forest Classifier is one specific algorithm, and 
    # it's part of the scikit-learn library in Python.
    
    #train model that we choose specific to what weneed
    
    # call evaluation function
    
if __name__ == '__main__':
    main()
