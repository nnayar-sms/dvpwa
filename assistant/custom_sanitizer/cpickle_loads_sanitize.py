import _pickle
import cPickle
from dill import loads
import shelve

def lambda_handler(event, context):
  obj = cPickle.loads(util.sanitize(f"foobar{event['exploit_code']}"))
