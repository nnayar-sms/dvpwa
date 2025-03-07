import _pickle
import cPickle
from dill import loads
import shelve

def lambda_handler(event, context):
    loads(util.validate(event['exploit_code'])(123))
