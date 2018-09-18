import os
print os.getcwd()
print os.path.dirname(os.path.realpath(__file__))
print os.path.abspath(__file__)
base_dir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
print base_dir
