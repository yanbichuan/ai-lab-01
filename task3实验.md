  # task3Linux终端基础实验
##1.实验环境

##2.命令所用笔记
 1  pwd
    2  madir -p project/logs
    3  mkdir -p project/logs
    4  cd project
    5  touch file1.txt
    6  touch file2.txt
    7  touch file3.txt
    8  mv file1.txt demo1.txt
    9  mv file2.txt demo2.txt
   10  'mv --help'
   11  mv file2.txt demo2.txt
   12  mv file3.txt demo3.txt
   13  cat > app.log
   14  grep "error" app.log > error_out.log
   15  cat error_out.log
   16  ls -l
   17  head -n 2 app.log
   18  df -h
   19  free -m
   20  chmod 644 error_out.log
   21  history > history.txt
