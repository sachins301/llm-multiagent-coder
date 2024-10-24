class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_to_linked_list(input_list):
    if not input_list:
        return None

    head = Node(input_list[0])
    current = head
    for i in range(1, len(input_list)):
        node = Node(input_list[i])
        current.next = node
        current = node

    return head

# Example usage
input_list = [1, 2, 3, 4, 5]
linked_list = list_to_linked_list(input_list)
print("Linked List:")
current_node = linked_list
while current_node:
    print(current_node.value)
    current_node = current_node.next