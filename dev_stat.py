# !/usr/bin/env python
#统计所有csv文件中设备信息，并导出为汇总表

from path import Path
import pandas as pd

class Stater():
  def __init__(self,base):
    self.base = Path(base)
    self.output_dir = Path('./outdir')
    self.output_dir.mkdir_p()
    pass
  def __concat__(self,first_line=False):
    files = self.base.files('*.csv')
    csv_list = []
    for file in files:
      csv_item = pd.read_csv(file)
      # for idx,row in csv_item.iterrows():
      #   pass

      csv_list .append(csv_item)

    df_total = pd.concat(csv_list)
    print('ok')



  def dev_stat(self):
    dev = ['mm','hdd','ssd','case','sc','gc']

    mm_dict = {'内存'}
    hdd_dict = {'机械硬盘'}
    ssd_dict = {'固态硬盘'}
    case_dict = {'机箱'}
    sc_dict = {'显示器'}
    gc_dict = {'显卡'}


    total = self.__concat__()





    pass


def main():
  print('????')
  stater = Stater(base='./CSVs')
  stater.dev_stat()

  pass

if __name__ == "__main__":
  main()



