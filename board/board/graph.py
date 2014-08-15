import os

from py2neo import neo4j, ogm
from py2neo.packages.urimagic import URI

GRAPHENEDB_URL = os.environ.get("GRAPHENEDB_URL", "http://localhost:7474/")
SERVICE_ROOT = neo4j.ServiceRoot(URI(GRAPHENEDB_URL).resolve("/"))
GRAPH_DATABASE = SERVICE_ROOT.graph_db

MERCENARY = "Mercenary"
CLIENT = "Client"

TYPES = {MERCENARY, CLIENT}


def query(query_string):
    print query_string
    query = neo4j.CypherQuery(GRAPH_DATABASE, query_string)
    results = query.execute()
    return results.data


def create_node(identifier, user_type):
    assert user_type in TYPES

    query_string = "CREATE (node:%s {id:%s}) return node" % (user_type, identifier)
    query(query_string)


def endorse(endorser_id, endorser_type, endorsee_id, endorsee_type):
    assert {endorser_type, endorsee_type}.issubset(TYPES)
    store = ogm.Store(GRAPH_DATABASE)
    endorser = store.load_unique(endorser_type.__name__, "id", endorser_id, endorser_type)
    endorsee = store.load_unique(endorsee_type.__name__, "id", endorsee_id, endorsee_type)

    store.relate(endorser, "ENDORSES", endorsee)
    store.save(endorser)


def remove_endorsement(endorser_id, endorser_class, endorsee_id, endorsee_class):
    assert {endorser_class, endorsee_class}.issubset(TYPES)
    store = ogm.Store(GRAPH_DATABASE)
    endorser = store.load_unique(endorser_class.__name__, "id", endorser_id, endorser_class)
    endorsee = store.load_unique(endorsee_class.__name__, "id", endorsee_id, endorsee_class)

    store.separate(endorser, "ENDORSES", endorsee)
    store.save(endorser)


def endorsed_user(endorsed_id, endorsed_class):
    assert endorsed_class in TYPES
    # query_string = 'MATCH (u:%s {id:"%s"})<-[:ENDORSES]-(user) RETURN user' % (endorsed_class.__name__, endorsed_id)
    query_string = 'MATCH (u) return u'
    print query_string
    query = neo4j.CypherQuery(GRAPH_DATABASE, query_string)
    results = query.execute()
    return results
