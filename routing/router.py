# Core routing logic to map URL paths and HTTP methods to handler functions
# Resolves incoming requests to their appropriate methods in the methods folder
# May include route decorators or a centralised routing table.
from parsing.parse import Parser

class Router:
    def __init__(self):
        parser = Parser()