print("Hello World")

class Hello:  # 클래스 생성
    def greeting(self):
        print("Hello, World!")

a = Hello() # 인스턴스 생성

a.greeting() # 메소드 호출

##############################################

class Member: # 클래스 생성

    def __init__(self, name, age, address): # 속성 생성
        self.name = name
        self.age = age
        self.address = address

    def info(self): # 메소드 생성
        print("저의 이름은 {0} 이고, 나이는 {1}, 사는곳은 {2} 입니다.".format(self.name , self.age, self.address))

# Member의 introduce 인스턴스 생성
introduce = Member("tnswo", 80, "광주광역시") 

# introduce 인스턴스의 info 메소드 호출
introduce.info()

class Members:

    value = [] # 클래스 속성을 빈 리스트로 추가. 클래스 속성은 모든
    # 인스턴스에서 공유할 수 있으며 값을 공유하며 각각의 인스턴스에서 클래스 속성을 공유

    def info2(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print("저의 이름은 {0} 이고, 나이는 {1}, 사는곳은 {2} 입니다.".format(self.name , self.age, self.address))

        Members.value.append(age)
        print("클래스 속성 {}".format(Members.value))

    def info3(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print("저의 이름은 {0} 이고, 나이는 {1}, 사는곳은 {2} 입니다.".format(self.name , self.age, self.address))

        Members.value.append(age)
        print("클래스 속성 {}".format(Members.value))

introduce2 = Members()

introduce2.info2("tnswo", 80, "부산")
introduce2.info3("tnswoo", 90, "서울")

