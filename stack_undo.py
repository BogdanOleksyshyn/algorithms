class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def main():
    stack = Stack()
    current_text = ""

    while True:
        print(f"Debug: {stack.items}")
        print(f"Current text: {current_text}")
        print("1. Add item")
        print("2. Undo")
        print("3. Exit")
        choice = input("Enter your option: ")

        if choice == "1":
            text = input("Enter text to add:")
            stack.push(current_text)
            current_text += text
        elif choice == "2":
            if stack.is_empty():
                print("Stack is empty nothing to undo")
            else:
                current_text = stack.pop()
        elif choice == "3":
            print("Exit")
            break
        else:
            print("Try another option")


if __name__ == "__main__":
    main()