import json

import xlrd


class Param(object):
    def __init__(self, paramConf='{}'):
        self.paramConf = json.loads(paramConf)

    def paramRowsCount(self):
        pass

    def paramColCount(self):
        pass

    def paramHeader(self):
        pass

    def paramAllline(self):
        pass

    def paramAlllineDict(self):
        pass


class XLS(Param):
    '''
    XLS基本格式（如果要把xls中存储的数字按照文本读出来的话，纯数字前要加上英文单
    引号：
    第一行是参数的注释，就是每一行的参数是什么
    第二行是参数名，参数名和对应模块的PO页面的变量名一直
    第3~N行是参数
    最后一列是预期默认头Exp
    '''

    def __init__(self, paramConf):
        '''
        参数 paramConf：xls文件位置（绝对路径）

        '''

        self.paramConf = paramConf
        self.paramfile = self.paramConf['file']
        self.data = xlrd.open_workbook(self.paramfile)
        self.getParamSheet(self.paramConf['sheet'])

    def getParamSheet(self, nsheets):
        '''
        设定参数所处的sheet
        参数在第几个sheet中
        '''
        self.paramsheet = self.data.sheets()[nsheets]

    def getOneline(self, nRow):
        '''
        返回一行数据
        '''

        return self.paramsheet.row_values(nRow)

    def getOneCol(self, nCol):
        '''
        返回一列
        '''
        return self.paramsheet.col_values(nCol)

    def paramRowsCount(self):
        '''
        获取参数文件行数
        '''
        return self.paramsheet.nrows

    def paramColCount(self):
        '''
        互殴参数文件列数
        '''
        return self.paramsheet.ncols

    def paramHeader(self):
        '''
        获取参数名称
        '''
        return self.getOneline(1)

    def paramAlllineDict(self):
        '''
        获取全部参数，其中dict的key值是header的值
        '''
        nCountRows = self.paramRowsCount()
        nCountCols = self.paramColCount()
        ParamAllListDict = {}
        iRowStep = 2
        iColStep = 0
        ParamHeader = self.paramHeader()
        while iRowStep < nCountRows:
            ParamOneLinelist = self.getOneline(iRowStep)
            ParamOneLineDict = {}
            while iColStep < nCountCols:
                ParamOneLineDict[ParamHeader[iColStep]] = ParamOneLinelist[iColStep]
                iColStep = iColStep + 1
            iColStep = 0
            ParamAllListDict[iRowStep - 2] = ParamOneLineDict
            iRowStep = iRowStep + 1
        return ParamAllListDict

    def paramAllline(self):
        '''
        获取全部参数
        '''
        nCountRows = self.paramRowsCount()
        paramall = []
        iRowStep = 2
        while iRowStep < nCountRows:
            paramall.append(self.getOneline(iRowStep))
            iRowStep = iRowStep + 1
        return paramall

    def __getParamCell(self, numberRow, numberCol):
        return self.paramsheet.cell_value(numberRow,numberCol)

class ParamFactory(object):
    def chooseParam(self,type,paramConf):
        map_={
            'xlsx':XLS(paramConf)
        }
        return map_[type]

if __name__ == '__main__':
    param = ParamFactory().chooseParam('xlsx',{'file':'test11111.xlsx','sheet':0})
    print(param.paramAllline())