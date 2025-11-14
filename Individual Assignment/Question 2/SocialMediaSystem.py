# ============================
#       Graph Class
# ============================
class Graph: #models a directed graph using an adjacency list (each vertex maps to a list of outgoing neighbors)
    def __init__(self):
        self.adjacency_list = {} #initialized empty Python dictionary. Key will be vertex identifiers (username)
        #and value will be lists of vertices that key has outgoing edges to (who they follow)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list: #check for existence
            self.adjacency_list[vertex] = [] #creates an empty list for vertex's outgoing edges

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.adjacency_list:
            self.add_vertex(from_vertex) #ensure the source vertex exists
        if to_vertex not in self.adjacency_list:
            self.add_vertex(to_vertex) #ensure the target vertex exists (even if target has no outgoing edges)
        self.adjacency_list[from_vertex].append(to_vertex)#appends to_vertex to the source's outgoing list (creating a directed edge)
        # allows duplicate edges if called repeatedly with the same pair (no duplicate-checking), Complexity of append: O(1)
    def list_outgoing_adjacent_vertex(self, vertex): #returns the list of nodes this vertex follows (outgoing neighbors)
        return self.adjacency_list.get(vertex, []) #uses dict.get to safely return an empty list if vertex is not present (avoids KeyError)
#does not add the vertex to the graph, only returns a safe default
    def list_incoming_adjacent_vertex(self, vertex): #computes who follows the given vertex
        followers = [] #initialize empty list to collect follower username
        for v, edges in self.adjacency_list.items(): #iterates over each vertex v and its outgoing edges list
            if vertex in edges: #check whether current v has an edge to vertex
                followers.append(v) #adds the follower to the result list
        return followers #return the collected list of incoming neighbors

    def display(self): #prints the adjacency list to the console
        for vertex, edges in self.adjacency_list.items(): #loops each entry
            print(f"{vertex} -> {edges}") #shows the vertex and its outgoing list in a readable format


# ============================
#       Person Class
# ============================
class Person:
    def __init__(self, username, name, gender, bio, privacy="Public"): #Constructor (Person)
        self.username = username
        self.name = name
        self.gender = gender
        self.bio = bio
        self.privacy = privacy

    def __repr__(self): #return a concise representation of the object used by the REPL or print (when printing lists/dicts)
        return f"@{self.username}"#returns @username format, easy to spot in data structures

    def detailed_profile(self): #returns a string describing user's profile
        if self.privacy.lower() == "private": #checks privacy case-insensitively
            return f"👤 {self.name} (@{self.username}) [Private Profile]" #returns short string marking profile private
        return ( #return name, username, gender, bio and privacy status
            f"👤 {self.name} (@{self.username})\n"
            f"Gender: {self.gender}\n"
            f"Bio: {self.bio}\n"
            f"Privacy: {self.privacy}"
        )


# ============================
#       Sample Data
# ============================
p1 = Person("alice", "Alice Tan", "Female", "Loves baby fashion & cute toys", "Public")
p2 = Person("ben", "Ben Wong", "Male", "New dad sharing parenting tips", "Private")
p3 = Person("chloe", "Chloe Lim", "Female", "Baby food blogger", "Public")
p4 = Person("david", "David Lee", "Male", "Photographer of baby moments", "Public")
p5 = Person("eva", "Eva Chan", "Female", "Infant care specialist", "Private")

people = {p.username: p for p in [p1, p2, p3, p4, p5]} #constructs a dictionary people mapping username

social_graph = Graph() #instantiates a graph object named social_graph to hold follow relationships

# Add vertices
for user in people.values(): #iterate all person objects in people and call social_graph.add_vertex(user.username) to create a vertex for each username in the graph
    social_graph.add_vertex(user.username)

# Add edges (follows)
social_graph.add_edge("alice", "ben")
social_graph.add_edge("alice", "chloe")
social_graph.add_edge("ben", "chloe")
social_graph.add_edge("chloe", "alice")
social_graph.add_edge("david", "chloe")
social_graph.add_edge("eva", "alice")
social_graph.add_edge("eva", "david")


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
        print("5. Add a new user")
        print("6. Follow another user")
        print("7. Unfollow a user")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nAll Users:")
            for username, person_obj in people.items(): #iterates over the people dict
                print(f"- {person_obj.name} (@{username})")#printing uses person_obj.name and username

        elif choice == "2":
            uname = input("Enter username: ").strip()
            if uname in people: #check existence, then prints detailed_profile() string for that Person
                print("\n" + people[uname].detailed_profile())
            else:
                print("User not found.")

        elif choice == "3":
            uname = input("Enter username: ").strip()
            if uname in people: #if username exist, follows = social_graph.list_outgoing_adjacent_vertex(uname) gets the outgoing list
                follows = social_graph.list_outgoing_adjacent_vertex(uname)
                print(f"\n{uname} follows:") #print header and then either the list of followed users (by resolving each username f to people[f].name of no followings if list empty
                if follows:
                    for f in follows:
                        print(f"  - {people[f].name} (@{f})")
                else:
                    print("  (No followings)")
            else:
                print("User not found.")

        elif choice == "4":
            uname = input("Enter username: ").strip()
            if uname in people: #if user exists, followers = social_graph.list_incoming_adjacent_vertex(uname) computes the list earlier described
                followers = social_graph.list_incoming_adjacent_vertex(uname)
                print(f"\nFollowers of {uname}:")#prints each follower by resolving to people[f].name
                if followers:
                    for f in followers:
                        print(f"  - {people[f].name} (@{f})")
                else:
                    print("  (No followers)")
            else:
                print("User not found.")

        elif choice == "5":
            uname = input("Enter new username: ").strip()
            if uname in people: #check uniqueness,if present, warns user
                print("Username already exists.")
            else:
                full_name = input("Enter full name: ")
                gender = input("Enter gender: ")
                bio = input("Enter bio: ")
                privacy = input("Privacy (Public/Private): ").strip()

                new_user = Person(uname, full_name, gender, bio, privacy)
                people[uname] = new_user
                social_graph.add_vertex(uname) #add a vertex to the graph for that username (creates an empty outgoing list)

                print("User added successfully!")

        elif choice == "6":
            follower = input("Enter your username: ").strip()
            followed = input("Enter username to follow: ").strip()

            if follower in people and followed in people: #ensures both exist(important to avoid creating graph entries for unknown users)
                social_graph.add_edge(follower, followed) #appends the followed username to follower's outgoing list
                print(f"{follower} now follows {followed}")
            else:
                print("Invalid usernames.")

        elif choice == "7":
            follower = input("Enter your username: ").strip() #.strip() removes leading and trailing whitespace from a string
            followed = input("Enter username to unfollow: ").strip()

            if follower in social_graph.adjacency_list: #checks that the follower vertex exists in the graph
                try:
                    social_graph.adjacency_list[follower].remove(followed) #attempts to remove the followed username from the follower's outgoing list
                    #.remove() raises ValueError if followed is not present, the except ValueError handles that by telling the user they are not following that person
                    print(f"{follower} unfollowed {followed}")
                except ValueError:
                    print("You are not following this user.")
            else:
                print("Invalid usernames.")

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    social_media_system()
