import pickle
from WMComponent.RetryManager.RetryManagerPoller import RetryManagerPoller

### Antonio ###

def changeJobPkl(new_memory, pkl_file):
    """
    Modifies the pkl_file job.pkl by changing the estimatedMemoryUsage to a new_memory value

    """
    with open(pkl_file, 'rb') as file:
        data = pickle.load(file)
    #print(data['estimatedMemoryUsage'])
    data['estimatedMemoryUsage'] = new_memory
    with open('job.pkl', 'wb') as file:
        pickle.dump(data, file)

def checkNewJobPkl(pkl_file):
    with open(pkl_file, 'rb') as file:
        data = pickle.load(file)
    print (data['estimatedMemoryUsage'])

checkNewJobPkl()


### German ###

def changeSandbox():
    """
    Modifies the parameter maxPSS in the sandbox. This is a change that applies for all jobs in that workflow that remain to be submitted 
    """
    pass

### Antonio and German ###

def changeMemory(new_memory):
    """
    The "main" function in charge of modifying the memory before a retry. 
    It needs to modify the job.pkl file and the workflow sandbox
    It gets the cachedir from the database. There it has the sandbox and the job.pkl file accessible
    """

    loadAction = RetryManagerPoller.daoFactory(classname="Jobs.LoadFromID") # RetryManagerPoller has no attribute daoFactory. I am certainly accessing it wrong. How do I access it?
    print(loadAction) 

    # I think loadAction is a dictionary whose keys are columns from the database. What is the exact name of the cachedir column?
    cacheDir = loadAction[cachedir]
    
    #Finds job.pkl file
    pkl_file = '{}/job.pkl'.format(cacheDir) 
    changeJobPkl(new_memory, pkl_file)
    changeSandbox()