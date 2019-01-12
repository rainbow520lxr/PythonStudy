from cat import Cat
from mouse import Mouse
from person import Person


per = Person()
tom = Cat("tom")
jerry = Mouse("jerry")

#这里太麻烦了
per.feedAnimal(tom)
per.feedAnimal(jerry)
# per.feedCat(tom)
# per.feedMouse(jerry)

tom.eat()
jerry.eat()

