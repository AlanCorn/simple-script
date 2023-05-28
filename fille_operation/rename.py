import os
import shutil


def rename(basePath):
    paths = os.listdir(basePath)
    print(paths)
    for fileDir in paths:
        fileDir = os.path.join(basePath,fileDir)
        if os.path.isdir(fileDir):
            tmpDir = os.path.join(basePath,fileDir)
            files = os.listdir(tmpDir)
            for fileName in files:
                src = os.path.join(basePath,fileDir,fileName)
                fileName = fileDir + "-" +fileName
                dst = os.path.join(basePath,fileDir,fileName)
                print("重命名" + src + " -> " + dst)
                os.rename(src,dst)

def moveFile(basePath):
    paths = os.listdir(basePath)
    for fileDir in paths:
        fileDir = os.path.join(basePath,fileDir)
        if os.path.isdir(fileDir):
            tmpDir = os.path.join(basePath,fileDir)
            files = os.listdir(tmpDir)
            for fileName in files:
                src = os.path.join(basePath,fileDir,fileName)
                dst = os.path.join(basePath,fileName)
                print("移动" + src + " -> " + dst)
                shutil.move(src,dst)
            print("删除空文件夹" + tmpDir)
            os.rmdir(tmpDir)

if __name__ == '__main__':
    path = r"/home/alancorn/Pictures/あらた作品合集"
    print("已输入目录：" + path)
    cmd = input("文件重命名？(y/n)")
    if cmd == "y":
        rename(path)
        # moveFile(path)
    else:
        pass