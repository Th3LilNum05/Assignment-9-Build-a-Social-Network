class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            print(f"Friendship not created. {person1_name if person1_name not in self.people else person2_name} doesn't exist!")

    def print_network(self):
        for name, person in self.people.items():
            friends_names = ", ".join(friend.name for friend in person.friends)
            print(f"{name} is friends with: {friends_names}")


# Test your code
network = SocialNetwork()

network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")  # "Friendship not created. Johnny doesn't exist!"
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()

#200-300 Word Design Memo

#The implemented system models a simple social network using object-oriented principles in Python. The design is centered around two classes: Person and SocialNetwork.
#The Person class holds the details of the individual users of the online community. The Person class contains a name attribute and an attribute called friends that holds lists of friends. The add_friend functionality prevents friend duplication. The above design encourages data integrity for an individual. The friend management system remains simple.
#TheSocialNetworkclass holds the overall management of the network. TheSocialNetworkclass uses a dictionary calledpeople that contains usernames askeys to Person objects. This helps in easy lookups and handling of users. The add_person function helps add new users only if those users are not present in the list. The add_friendship function helps add friendship to two users only when both users are present in the overall network. The print_network function helps print the networking details of each person.
#The design emphasizes clarity, modularity, and maintainability. By separating the individual (Person) and network (SocialNetwork) responsibilities, the code is flexible for future extensions, such as removing friends, suggesting connections, or implementing advanced analytics. Error handling is basic but informative, alerting users when attempted operations involve nonexistent individuals.
#Nevertheless, it offers a sound starting point for simulating the networking relationships that incorporates simplicity and accuracy. The object-oriented design of the code makes it easy to manage and test and thus can serve as a demonstration version of a more complex social networking program."""
