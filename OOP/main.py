from person import Person
from librarian import Librarian
from maker import make
from stamp_collector import StampCollector
from woodworker import Woodworker

# This is Chris's screen

if __name__ == "__main__":
    plain_person = Person("Fred Jones", make)
    print(plain_person)
    plain_person.change_name("Fred K. Jones")
    print(plain_person)
    #plain_person.do_your_job()
    plain_person.do_hobby()
    plain_person.add_hobby(StampCollector("USA"))
    plain_person.add_hobby(Woodworker("Table", "Jatoba"))
    plain_person.do_hobby()
