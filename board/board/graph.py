import os

from py2neo import neo4j, ogm
from py2neo.packages.urimagic import URI

GRAPHENEDB_URL = os.environ.get("GRAPHENEDB_URL", "http://localhost:7474/")
SERVICE_ROOT = neo4j.ServiceRoot(URI(GRAPHENEDB_URL).resolve("/"))
GRAPH_DATABASE = SERVICE_ROOT.graph_db


class User(object):
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return self.identifier


class Client(User):
    pass


class Mercenary(User):
    pass


def create_node(identifier, user_class):
    assert user_class in [Client, Mercenary]
    store = ogm.Store(GRAPH_DATABASE)

    node = user_class(identifier)
    store.save_unique(user_class.__name__, "id", identifier, node)


def endorse(endorser_id, endorser_class, endorsee_id, endorsee_class):
    assert {endorser_class, endorsee_class}.issubset({Client, Mercenary})
    store = ogm.Store(GRAPH_DATABASE)
    endorser = store.load_unique(endorser_class.__name__, "id", endorser_id, endorser_class)
    endorsee = store.load_unique(endorsee_class.__name__, "id", endorsee_id, endorsee_class)

    store.relate(endorser, "ENDORSES", endorsee)
    store.save(endorser)


def remove_endorsement(endorser_id, endorser_class, endorsee_id, endorsee_class):
    assert {endorser_class, endorsee_class}.issubset({Client, Mercenary})
    store = ogm.Store(GRAPH_DATABASE)
    endorser = store.load_unique(endorser_class.__name__, "id", endorser_id, endorser_class)
    endorsee = store.load_unique(endorsee_class.__name__, "id", endorsee_id, endorsee_class)

    store.separate(endorser, "ENDORSES", endorsee)
    store.save(endorser)