actor = ("Tom Hardy", "English", 42)  # name, nationality, age

def to_dic(actor):
        name, nationally, age = actor

        return {
            "name": name,
            "nationally": nationally,
            "age": age
        }


print(to_dic(actor))