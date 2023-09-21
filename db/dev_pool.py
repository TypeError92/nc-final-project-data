from importlib import import_module

pool = import_module('db.connect').pool('dev')
