"Todo Checker"
import datetime,os,sys,pickle

SUBJECTS = "Arrays Strings Search_and_Sort Recursion Hashing Matrices Linked_list Bit_manipulation Stacks_and_Queues Trees Tries Heapst Graphs Dynamic_prog".split(" ")
UNITS = 4
log = "todo.txt"
filename = "progress.pkl"

# Create the file if doesn't exist
if not os.path.exists(filename):
    open(filename,"w+").close()

# For logging purpose 

def write(text):
    f = open(log,"a+")
    f.write(f"{datetime.datetime.now()}:{text}\n")
    f.close()

    
class Todo:
    def __init__(self,name):
        self.name = name
        self.subject = ""
        self.__status = 0
        write(f"Todo Created - {name}")
    
    def mark_completed(self):
        self.__status = 1
        write(f"{self} marked as Completed")
        self.subject.set_current_target()
        
    
    def mark_uncompleted(self):
        self.__status = 0
        write(f"{self} marked as Not Completed")
        self.subject.set_current_target()
    
    def get_status(self):
        return "Completed" if self.__status else "Uncompleted"
    
    def status(self):
        return self.__status
    
    def add_subject(self,subject):
        self.subject = subject
        write(f"Subject Added to {self}")
    
    def __str__(self):
        return f"{self.subject.name}-{self.name}"

class Subject:
    def __init__(self,name):
        self.table = []
        self.name = name
        self.current_target = "" 
    
    def add(self,todo):
        if len(self.table) == 0:
            self.current_target = todo 
        self.table.append(todo)
        
        # Append the Subject name to Todo 
        todo.add_subject(self)
    
    def show_current_target(self):
        if self.current_target and self.current_target.status() == 0:
            return self.current_target
        return ""
    
    def set_current_target(self):
        for i in self.table:
            if i.status() == 0:
                self.current_target = i 
                break
        write(f"Current Target Set to {self.current_target}")
        return self.current_target
    
    def mark_uncompleted(self):
        for i in self.table:    
            i.mark_uncompleted()

    def mark_completed(self):
        for i in self.table:    
            i.mark_completed()
    
    def get_all_todos(self):
        return self.table.copy()
    
    def __str__(self):
        return self.name 

# Creation
try:
    all_subjects = pickle.load(open(filename,"rb+"))
except EOFError as e:
    print(e)
    all_subjects = []
if all_subjects == []:
    for i in SUBJECTS:
        s = Subject(i)
        print("Adding to Subject:",s)
        _ = 1
        user_input = input(f"Enter Sub-Subject {_}:")
        while user_input:
            _ += 1
            s.add(Todo(user_input))
            user_input = input(f"Enter Sub-Subject {_}:")
        all_subjects.append(s)
        print("Subject Added to the file")
    pickle.dump(all_subjects,open(filename,"wb"))
    print("Created All subjects and saved it")
def show_todo():
    for i in all_subjects:
        print(i.show_current_target())
def mark_completed():
    for i,j in enumerate(all_subjects,start=1):
        print(str(i)+".",j.show_current_target())
    print("Which one should be marked as Completed?")
    x = int(input("(0 for not marking)>"))
    if x == 0:
        return
    all_subjects[x-1].current_target.mark_completed()
    print("Marked as completed")

def mark_uncompleted():
    count = 1
    all_completed_todos = []
    for i in all_subjects:
        for j in i.table:
            if j.status() == 1:
                all_completed_todos.append(j)
                print(count,j)
                count+=1
    if len(all_completed_todos) == 0:
        print("No Completed Todos Found")
        return
    print("Which one should be marked as Uncompleted?")
    x = int(input("(0 for not marking)>"))
    if x == 0:
        return
    all_completed_todos[x-1].mark_uncompleted()
    print("Marked as completed")
d = {
    "Show the current Target":show_todo,
    "Mark Completed":mark_completed,
    "Mark Uncompleted":mark_uncompleted,
    "Exit":sys.exit
}
commands = list(d.keys())
# Prompt
while True:
    # print commands 
    for i,j in enumerate(commands,start=1):
        print(f"{i}. {j}")
    x = input(">")
    os.system("cls")
    if (not x.isdigit()) or int(x) > len(commands):
        continue
    print(d[commands[int(x)-1]]())
    pickle.dump(all_subjects,open(filename,"wb"))