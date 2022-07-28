#!/usr/bin/env python
import os

class Maker:
    def create_dir(self, path):
        isdir = os.path.isdir(path)
        if (isdir):
            raise Exception("Directory exists - Path: " + path)
        else:
            os.mkdir(path)

    def create_file(self, path, filename):
        filepath = path + "/" + filename
        isfile = os.path.isfile(filepath)
        if (os.path.isdir(path) == False):
          print("creating directory: " + path)
          self.create_dir(path)
        if (isfile):
            raise Exception(filename + " exists - File: " + path)
        else:
            myfile = open(filepath, "w")
            myfile.close()

    def make_project_directories(self, path, date, adnames):
        pass
