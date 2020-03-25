import pandas as pd
import seaborn as sns

""" Module allowing the creation of the dataset and data statistics """

def open_data(file,
              info = False):
    """ Open the data and transform it in a DataFrame 
        Arguments :
            :file: CSV to read and convert into a pandas DataFrame
            :info: default = False : Boolean to get summary information on the created object
        Output :
            A pandas DataFrame with all the data from the CSV file
    """
    df = pd.read_csv(file)
    if info is True :
        print('Five first rows of the generated DataFrame : \n {}'.format(df.head()))
        print('\nDataFrame shape : {}\n'.format(df.shape))
    return df


def create_train_test_set(dataframe,
                          train_frac,
                          test_frac):
    """ Create the train and test set for the training with a random method
        Arguments :
            :dataframe: pandas DataFrame containing the date to split
            :train_frac: float, fraction number of training data to keep
            :test_frac: float, fraction number of test data to keep
        Outputs : 
            :train_features: pandas DataFrame of the training points selected randomly
            :train_labels: pandas DataFrame, outputs for the training
            :test_features: pandas DataFrame of the test points selected randomly
            :test_labels: pandas DataFrame, outputs for the tests
    """
    train_dataset = dataframe.sample(frac = train_frac, random_state = 123)
    tmp = dataframe.drop(train_dataset.index)
    test_dataset = tmp.sample(frac = test_frac, random_state = 123)
    tmp.drop(test_dataset.index)
    train_labels = train_dataset.pop('energie')  
    train_features = train_dataset
    test_labels = test_dataset.pop('energie')
    test_features =test_dataset
    creturn train_features, train_labels, test_features, test_labels
