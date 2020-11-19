import openpyxl


def change(x):
    if x==1:
        return 1
    else:
        return -1

class Loader:
    def __init__(self, filename =  "data.xlsx",data_size = (6,3)):
        wb = openpyxl.load_workbook(filename)
        sh = wb['data']
        max_row = sh.max.row()
        full_size = data_size[0]*data_size[1]
        self.__train_set = [
            [
               1 if sh[chr(i%data_size[1]+ord('A')) + str(i//data_size[1] + 1)].value==1 else -1
                for i in range(k*full_size,(k+1)*full_size)
            ] for k in range(max_row//data_size[0]*data_size[0])
        ]

    def get_data(self):
        set = self.__train_set.copy()
        set = list(map(change,set))
        return self.__train_set