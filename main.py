class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Суммируем значения и перенос
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10

            # Создаем новый узел с вычисленным значением
            current.next = ListNode(new_val)
            current = current.next

            # Переходим к следующим узлам
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next


def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Создаем два связанных списка: (2 -> 4 -> 3) и (5 -> 6 -> 4)
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

# Создаем экземпляр решения и вызываем метод addTwoNumbers
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Печатаем результат
print_linked_list(result)  # Вывод: 7 -> 0 -> 8 -> None

