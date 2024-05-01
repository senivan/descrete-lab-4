import random


class Me:

    def prime_state(func):
        def wrapper(*args, **kwargs):
            v = func(*args, **kwargs)
            v.send(None)
            return v
        return wrapper

    enum = {
        "SLEEP":0,
        "STUDY":1,
        "EAT":2,
        "CHILL":3,
        "WALK":4
    }
    def __init__(self):
        self.me_status = self.enum["SLEEP"]
        self.hour = 8
        self.start = self._create_start()
        self._q1 = self._create_q1()
        self._q2 = self._create_q2()    
        self._q3 = self._create_q3()
        self._q4 = self._create_q4()
        self._q5 = self._create_q5()
        self._q6 = self._create_q6()
        self._q7 = self._create_q7()
        self._q8 = self._create_q8()
        self._q9 = self._create_q9()
        self._q10 = self._create_q10()
        self.end = self._create_end()
        self._current_state = self.start
    def run_day(self):
        print("Starting a day")
        while self._current_state != self.end:
            print(f"Hour: {self.hour} Status: "+ str([key for key, value in self.enum.items() if value == self.me_status][0]))
            self()
        print(f"Hour: {self.hour} Status: "+ str([key for key, value in self.enum.items() if value == self.me_status][0]))
        self()
    

    @prime_state
    def _create_start(self):
        while True:
            hour = yield
            rand = random.random()
            if rand < 0.5 and hour == 8:
                self._current_state = self._q1
                self.lazy_coef = 0.5
            elif rand > 0.5 and hour == 8:
                self._current_state = self._q2
                self.lazy_coef = 0.2
            else:
                break
    
    @prime_state
    def _create_q1(self):
        while True:
            hour = yield
            print("I did not wake up on time")
            self._current_state = self._q3
            self.hour = hour + 2
            self.me_status = self.enum["SLEEP"]
            
    
    @prime_state
    def _create_q2(self):
        while True:
            hour = yield
            print("I woke up on time")
            self._current_state = self._q3
            self.hour = hour + 2
            self.me_status = self.enum["STUDY"]
            
    
    @prime_state
    def _create_q3(self):
        while True:
            hour = yield
            print("I am eating breakfast")
            self._current_state = self._q5
            self.hour = hour + 1
            self.me_status = self.enum["EAT"]
            rand = random.random()
            if rand < self.lazy_coef:
                self._current_state = self._q4
            else:
                self._current_state = self._q5
            
    
    @prime_state
    def _create_q4(self):
        while True:
            hour = yield
            print("I am going to study again")
            self._current_state = self._q6
            self.hour = hour + 4
            self.me_status = self.enum["STUDY"]
            
    
    @prime_state
    def _create_q5(self):
        while True:
            hour = yield
            print("I am feeling lazy now")
            self._current_state = self._q6
            self.hour = hour + 4
            self.me_status = self.enum["CHILL"]
            
    
    @prime_state
    def _create_q6(self):
        while True:
            hour = yield
            print("I am going to eat lunch")
            self._current_state = self._q7
            self.hour = hour + 1
            self.me_status = self.enum["EAT"]
            
    
    @prime_state
    def _create_q7(self):
        while True:
            hour = yield
            print("I am going to rest right now")
            self._current_state = self._q8
            self.hour = hour + 4
            self.me_status = self.enum["CHILL"]

            rain_rand = random.random()
            if rain_rand < 0.5:
                self._current_state = self._q9 # not raining
            else:
                self._current_state = self._q8 # raining
            
    
    @prime_state
    def _create_q8(self):
        while True:
            hour = yield
            print("I am going to rest some more")
            self._current_state = self.end
            self.hour = hour + 2
            self.me_status = self.enum["CHILL"]
            
    
    @prime_state
    def _create_q9(self):
        while True:
            hour = yield
            print("I am going to walk")
            self._current_state = self._q10
            self.hour = hour + 2
            self.me_status = self.enum["WALK"]
            
    
    @prime_state
    def _create_q10(self):
        while True:
            hour = yield
            print("I am going to rest")
            self._current_state = self.end
            self.hour = hour + 2
            self.me_status = self.enum["CHILL"]
            
    
    @prime_state
    def _create_end(self):
        while True:
            hour = yield
            print("I am going to sleep")
            self.hour = 8
    
    def __call__(self):
        self._current_state.send(self.hour)
    
if __name__ == "__main__":
    me = Me()
    me.run_day()


