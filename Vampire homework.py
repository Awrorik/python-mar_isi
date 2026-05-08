class Vampire :
    def __init__(self, name, age,subjects ):
        self.name = name
        self.hunger = 0
        self.alive = True
        self.has_ring = False
        self.days_alive = 0
        self.age = age
        self.subjects = subjects
        self.money =20000
        self.energy = 100

    def new_day(self):
            self.days_alive += 1
            self.hunger += 1
            print(f"\nДень {self.days_alive}")
            print(f"Голод: {self.hunger}")

            if self.hunger >= 2:
                self.alive = False
                print(f"{self.name} умер от недостатка крови")
    def energy(self):
        if self.energy >20:
            print("пойду отдохну а то устал")
        else:
            print("еще буду убивать людей))")
    def drink_blood(self):
                self.hunger = 0
                print(f"{self.name} бегу быстро пить кровь")
    def go_out(self,time_of_day):
                if time_of_day == "day":
                    if self.has_ring:
                        print("могу выйти пока день, кольцо защитит")
                else:
                    print("не могу выйти кольца нет, я згорю")

    def get_ring_from_witch(self):
        if self.money >= 15000:
            self.has_ring = True
            self.money -= 15000
    print("Ведьма сделала колечко света за много денег надо идти работать :(")


    def work(self):
      if self.money <= 500:
         print("Быстро иду работать!")
      else:
       print("денюжки есть еще можно дома посидеть")

    def __str__(self):
        return "Student:" + self.name

    def live_day(self):
        print(self.name, "прожил ещё один день")

    def __len__(self):
        return len(self.subjects)

vamp1 = Vampire("Клаус", 1488,  ["веревка", "кровь", "кольцо света" ])
vamp1.get_ring_from_witch()
for day in range(365):
    if not vamp1.alive:
        print("Вампир умер так как выпил крови с подмешенной вербеной :0")
        break

    vamp1.new_day()

print("\nГод уже прошёл")
vamp1.alive = False
print("Вампир умер от  времени :(")
print(len(vamp1))
print(vamp1.name)
print(vamp1.money)
print(vamp1.energy)
if vamp1.alive==False:
    print("окончательно умер :(")
else:
    print("еще живет! ")
print("мне пока что столько лет -",vamp1.age)