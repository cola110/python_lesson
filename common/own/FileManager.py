#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil


class ZxxAvi:

    def moveAvi(self, basePath=u'E:\张孝祥_Java基础加强'):
        list = os.listdir(basePath)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            path = os.path.join(basePath, list[i])
            if os.path.isfile(path):
                self.copyfile(path)
            else:
                self.moveAvi(path)

    def copyfile(self, fileName, targetPath=u"E:\\avi"):
        fpath, fname = os.path.split(fileName)  # 分离文件名和路径

        if os.path.exists(os.path.join(targetPath, fname)):
            return
        else:
            shutil.copyfile(fileName, os.path.join(targetPath, fname))  # 复制文件


if __name__ == '__main__':
    zxxAvi = ZxxAvi()
    zxxAvi.moveAvi();
