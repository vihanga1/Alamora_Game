def openTextFile(filePath, assignArray):
    fileOne = open(filePath, 'r')
    for item in fileOne:
        assignArray.append(item.strip())
    return assignArray