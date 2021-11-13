class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node

        return self
    
    def print_values(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        
        return self

    def add_to_back(self,val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node

        return self

    def remove_from_front(self):
        runner = self.head
        self.head = runner.next
        print(runner.value)
        print('#########################')

        return self 

    def remove_from_back(self):
        runner = self.head
        while(runner.next != None):
            previo = runner
            runner = runner.next
        runner = previo
        runner.next = None

        return self

    def remove_val(self, val):
        runner = self.head
        while runner.value != val:
            previo = runner
            runner = runner.next        
        link = runner
        runner = previo
        runner.next = link.next

        return self

    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)

        else:        
            runner = self.head
            contador = 0
        
            while contador != n:
                previo = runner
                runner = runner.next
                contador += 1

            if runner != None:  
                new_node = SLNode(val)
                previo.next = new_node
                new_node.next = runner
            else:
                self.add_to_back(val)
        return self


paises = SList()
paises.add_to_front("Bolivia").add_to_front("Chile").add_to_back("Peru").add_to_back("Alemania").print_values()
print("##############################")
#paises.remove_from_back().print_values()
paises.remove_val("Peru").print_values()
print("##################################")
paises.insert_at("Holanda",0).print_values()
