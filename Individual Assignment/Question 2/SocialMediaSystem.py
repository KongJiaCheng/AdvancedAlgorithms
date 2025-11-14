# ============================
#       Graph Class
# ============================
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def addEdge(self, from_vertex, to_vertex):
        if from_vertex not in self.adjacency_list:
            self.addVertex(from_vertex)
        if to_vertex not in self.adjacency_list:
            self.addVertex(to_vertex)
        self.adjacency_list[from_vertex].append(to_vertex)

    def listOutgoingAdjacentVertex(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def listIncomingAdjacentVertex(self, vertex):
        followers = []
        for v, edges in self.adjacency_list.items():
            if vertex in edges:
                followers.append(v)
        return followers

    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex} -> {[e for e in edges]}")


# ============================
#       Person Class
# ============================
class Person:
    def __init__(self, username, name, gender, bio, privacy="Public"):
        self.username = username
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy

    def __repr__(self):
        return f"@{self.username}"

    def detailed_profile(self):
        if self.privacy.lower() == "private":
            return f"👤 {self.name} (@{self.username}) [Private Profile]"
        else:
            return (
                f"👤 {self.name} (@{self.username})\n"
                f"Gender: {self.gender}\n"
                f"Bio: {self.bio}\n"
                f"Privacy: {self.privacy}"
            )


# ============================
#       Sample Data
# ============================
# Create people
p1 = Person("alice", "Alice Tan", "Female", "Loves baby fashion & cute toys", "Public")
p2 = Person("ben", "Ben Wong", "Male", "New dad sharing parenting tips", "Private")
p3 = Person("chloe", "Chloe Lim", "Female", "Baby food blogger", "Public")
p4 = Person("david", "David Lee", "Male", "Photographer of baby moments", "Public")
p5 = Person("eva", "Eva Chan", "Female", "Infant care specialist", "Private")

people = {p.username: p for p in [p1, p2, p3, p4, p5]}

# Create graph
social_graph = Graph()

# Add vertices
for person in people.values():
    social_graph.addVertex(person.username)

# Add edges (follows)
social_graph.addEdge("alice", "ben")
social_graph.addEdge("alice", "chloe")
social_graph.addEdge("ben", "chloe")
social_graph.addEdge("chloe", "alice")
social_graph.addEdge("david", "chloe")
social_graph.addEdge("eva", "alice")
social_graph.addEdge("eva", "david")


# ============================
#       Menu System
# ============================
def social_media_system():
    while True:
        print("\n=== Mini Social Media App ===")
        print("1. Display all users")
        print("2. View a user's profile")
        print("3. View who a user follows")
        print("4. View a user's followers")
        print("5. Add a new user (optional)")
        print("6. Follow another user (optional)")
        print("7. Unfollow a user (optional)")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n All Users:")
            for username, person in people.items():
                print(f"- {person.name} (@{username})")

        elif choice == "2":
            uname = input("Enter username: ").strip()
            if uname in people:
                print("\n" + people[uname].detailed_profile())
            else:
                print(" User not found.")

        elif choice == "3":
            uname = input("Enter username: ").strip()
            if uname in people:
                follows = social_graph.listOutgoingAdjacentVertex(uname)
                print(f"\n {uname} follows:")
                if follows:
                    for f in follows:
                        print(f"  - {people[f].name} (@{f})")
                else:
                    print("  (No followings)")
            else:
                print(" User not found.")

        elif choice == "4":
            uname = input("Enter username: ").strip()
            if uname in people:
                followers = social_graph.listIncomingAdjacentVertex(uname)
                print(f"\n Followers of {uname}:")
                if followers:
                    for f in followers:
                        print(f"  - {people[f].name} (@{f})")
                else:
                    print("  (No followers)")
            else:
                print(" User not found.")

        elif choice == "5":
            uname = input("Enter new username: ").strip()
            if uname in people:
                print(" Username already exists.")
            else:
                name = input("Enter full name: ")
                gender = input("Enter gender: ")
                bio = input("Enter bio: ")
                privacy = input("Privacy (Public/Private): ")
                new_user = Person(uname, name, gender, bio, privacy)
                people[uname] = new_user
                social_graph.addVertex(uname)
                print(" User added successfully!")

        elif choice == "6":
            follower = input("Enter your username: ").strip()
            followed = input("Enter username to follow: ").strip()
            if follower in people and followed in people:
                social_graph.addEdge(follower, followed)
                print(f" {follower} now follows {followed}")
            else:
                print(" Invalid usernames.")

        elif choice == "7":
            follower = input("Enter your username: ").strip()
            followed = input("Enter username to unfollow: ").strip()
            if follower in social_graph.adjacency_list:
                try:
                    social_graph.adjacency_list[follower].remove(followed)
                    print(f" {follower} unfollowed {followed}")
                except ValueError:
                    print(" You are not following this user.")
            else:
                print(" Invalid usernames.")

        elif choice == "8":
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    social_media_system()
