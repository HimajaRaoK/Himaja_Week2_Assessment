'''17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, 
and `delete()`. 
Implement this in `SQLDatabase` and `NoSQLDatabase`.'''

from abc import ABC,abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def Insert(self):
        pass
    @abstractmethod
    def Update(self):
        pass
    @abstractmethod
    def Delete(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def Insert(self):
        print("inserted into SQL Database")
    def Update(self):
        print("updated in SQL Database")
    def Delete(self):
        print("deleted from SQL Database")
        
class NOSQLDatabase(IDatabaseOperations):
    def Insert(self):
        print("inserted into NOSQL Database")
    def Update(self):
        print("updated in NOSQL Database")
    def Delete(self):
        print("deleted from NOSQL Database")
        
def main():
    sql=SQLDatabase()
    nosql=NOSQLDatabase()
    sql.Insert()
    sql.Update()
    sql.Delete()

    nosql.Insert()
    nosql.Update()
    nosql.Delete()

main()