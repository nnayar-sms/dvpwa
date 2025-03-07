import _pickle
import cPickle
from dill import loads
import shelve

def lambda_handler(event, context):
  _pickle.load(event['exploit_code'])
