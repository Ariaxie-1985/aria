# -*- coding: utf8 -*-
__author__ = 'yqzhang'
import os
import shutil
from ApkChannelBuildTool2.dsu import sort_strings_with_emb_numbers


class clear():

    def __init__(self, path):
        self.path = path

    def clearC(self):

        dirc = os.listdir(self.path)
        dircx = sort_strings_with_emb_numbers(dirc)
        # clearobj=dircx[-6]
        # print dircx
        for root, dirs, files in os.walk(self.path + dircx[-6]):
            for name in files:
                if '.apk' in name and 'lagou-ty' not in name:
                    # print self.path+"\\"+dircx[-9]
                    # print self.path+'\\'+os.path.join(root, name)
                    os.remove(os.path.join(root, name))

        for root, dirs, files in os.walk(self.path + dircx[-6]):
            for name in files:
                if 'apk' in name:
                    shutil.move(os.path.join(root, name), self.path + dircx[-6])

        shutil.rmtree(self.path + dircx[-6] + "/sem/")
        shutil.rmtree(self.path + dircx[-6] + "/other/")
        if os.path.isdir(self.path + dircx[-6] + "/new/"):
            shutil.rmtree(self.path + dircx[-6] + "/new/")
