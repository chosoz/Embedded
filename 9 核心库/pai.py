//pai.py
PI = 3.14

def main():
  print("PI:", PI)

//如果被直接运行(python xx.py)，则后面语句(main())会被执行（类似c c++ 里的程序main入口）
if __name__ == "__main__":  
  main()

//area.py
from pai import PI

def calc_round_area(radius):
  return PI * (radius ** 2)

def main():
  print("round area: ", calc_round_area(2))

//如果被直接运行(python xx.py)，则后面语句(main())会被执行（类似c c++ 里的程序main入口）
if __name__ == "__main__":
  main()

  if __name__ == "__main__":  
