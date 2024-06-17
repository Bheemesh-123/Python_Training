# Base Class
class Faculty:
    def __init__(self, f_name, department, f_id):
        self.f_name = f_name
        self.department = department
        self.f_id = f_id

    def print_info(self):
        print("Faculty Information:", self.f_name, self.department, self.f_id)

# Derived Class (Single Inheritance)
class Cse(Faculty):
    pass

# Multiple Inheritance
class Researcher:
    def __init__(self, research_area):
        self.research_area = research_area

    def print_research_info(self):
        print("Research Area:", self.research_area)

class CseResearcher(Faculty, Researcher):
    def __init__(self, f_name, department, f_id, research_area):
        Faculty.__init__(self, f_name, department, f_id)
        Researcher.__init__(self, research_area)

    def print_all_info(self):
        self.print_info()
        self.print_research_info()

# Multilevel Inheritance
class SeniorFaculty(Cse):
    def __init__(self, f_name, department, f_id, experience):
        super().__init__(f_name, department, f_id)
        self.experience = experience

    def print_senior_info(self):
        self.print_info()
        print("Experience:", self.experience)

# Hybrid Inheritance
class CseSeniorResearcher(SeniorFaculty, Researcher):
    def __init__(self, f_name, department, f_id, experience, research_area):
        SeniorFaculty.__init__(self, f_name, department, f_id, experience)
        Researcher.__init__(self, research_area)

    def print_complete_info(self):
        self.print_senior_info()
        self.print_research_info()

# Test the classes
if __name__ == "__main__":
    obj = Faculty("Ashish", "Computer Science", 1001)
    obj.print_info()
    print()

    obj1 = Cse("Jyothi", "Computer Science", 1002)
    obj1.print_info()
    print()

    obj2 = CseResearcher("Priya", "Computer Science", 1003, "AI and ML")
    obj2.print_all_info()
    print()

    obj3 = SeniorFaculty("Rahul", "Computer Science", 1004, "10 years")
    obj3.print_senior_info()
    print()

    obj4 = CseSeniorResearcher("Sonia", "Computer Science", 1005, "15 years", "Data Science")
    obj4.print_complete_info()
