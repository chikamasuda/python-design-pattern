class Employee:
  def __init__(self, emp_id: int, name: str, salary: int):
    self.__emp_id = emp_id
    self.__name = name
    self.__salary = salary

  def _work(self) -> None:
    print('働きます')
  
  # def gey_salary(self) -> int:
  #   return self.__salary

  # def set_salary(self, salary: int) -> None:
  #   self.__salary = salary

  @property
  def salary(self) -> int:
    return self.__salary

  @salary.setter
  def salary(self, salary: int) -> None:
    self.__salary = salary