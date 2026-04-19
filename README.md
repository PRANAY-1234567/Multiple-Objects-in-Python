# 👥 Multiple Objects in Python (Person Class)

## 📌 Description

This Python program demonstrates how to create **multiple objects** from a single class. It uses a `Person` class to store and display information like name and age for different individuals.

---

## 🚀 Features

* Defines a `Person` class
* Uses separate methods to set and get data
* Creates multiple objects (`p1`, `p2`, `p3`)
* Stores different data for each object

---

## 🛠️ How It Works

1. A class `Person` is created with attributes:

   * `name`
   * `age`

2. Methods:

   * `setInfo()` → Assigns values to attributes
   * `getInfo()` → Displays the stored data

3. Three objects are created:

   * `p1`, `p2`, `p3`

4. Each object is assigned different values using `setInfo()`.

5. The `getInfo()` method is called for each object to display their details.

---

## 💻 Code

```python id="w7n4kp"
class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def setInfo(self, nm, a):
        self.name = nm
        self.age = a

    def getInfo(self):
        print("Name   :", self.name)
        print("Age    :", self.age)


# Main program
p1 = Person()
p2 = Person()
p3 = Person()

p1.setInfo("Akshay", 26)
p2.setInfo("Saurabh", 20)
p3.setInfo("Shrijeet", 25)

p1.getInfo()
p2.getInfo()
p3.getInfo()
```

---

## ▶️ Example Output

```id="q9m2lx"
Name   : Akshay
Age    : 26
Name   : Saurabh
Age    : 20
Name   : Shrijeet
Age    : 25
```

---

## 📚 Concepts Used

* Class and Object
* Instance variables
* Methods (`setInfo`, `getInfo`)
* Multiple object creation

---

## 🎯 Use Case

This program helps beginners understand:

* How one class can represent multiple real-world entities
* How each object maintains its own data independently

---

## 🔧 Future Improvements

* Use constructor to initialize values directly
* Store multiple persons in a list
* Add more attributes (address, phone number)
* Add input-based data entry

---

## 📄 License

This project is open-source and free to use.
