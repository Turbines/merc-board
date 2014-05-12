import os
from py2neo import neo4j
from py2neo.packages.urimagic import URI

GRAPHENEDB_URL = os.environ.get("GRAPHENEDB_URL", "http://localhost:7474/")
SERVICE_ROOT = neo4j.ServiceRoot(URI(GRAPHENEDB_URL).resolve("/"))
GRAPH_DATABASE = SERVICE_ROOT.graph_db

