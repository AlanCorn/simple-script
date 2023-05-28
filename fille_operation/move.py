import os
import shutil

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
    path = r"/home/alancorn/Pictures/さより作品合集/さより"
    print("已输入目录：" + path)
    cmd = input("文件移动操作？(y/n)")
    if cmd == "y":
        moveFile(path)
    else:
        pass