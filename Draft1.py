class Command:
    def __init__(self, movement, direction):
        self.movement = movement  
        self.direction = direction  
class Chandrayaan:
    def __init__(self):
        self.position = (0, 0, 0) 
        self.direction = 'N'  

    def execute_command(self, cmd: Command):
        self.position = tuple(sum(x) for x in zip(self.position, cmd.movement))
        self.direction = cmd.direction

def test():
    # Test 1
    commands = [
        Command((0, 1, 0), "N"),
        Command((0, 1, 0), "E"),
        Command((0, 1, 0), "U"),
        Command((0, 1, -1), "U"),
        Command((0, 1, -1), "N")
    ]
    chandrayaan_test = Chandrayaan()
    for cmd in commands:
        chandrayaan_test.execute_command(cmd)
    assert chandrayaan_test.position == (0, 5, -2), f"Expected (0, 5, -2), got {chandrayaan_test.position}"
    assert chandrayaan_test.direction == "N", f"Expected N, got {chandrayaan_test.direction}"
    print("Test 1 passed!")
    
    # Test 2
    commands2 = [
        Command((0, 1, 0), "E"),
        Command((0, 0, 1), "U"),
        Command((1, 0, 0), "N"),
        Command((0, 0, -1), "W"),
        Command((-1, 0, 0), "D")
    ]
    chandrayaan_test2 = Chandrayaan()
    for cmd in commands2:
        chandrayaan_test2.execute_command(cmd)
    assert chandrayaan_test2.position == (0, 1, 0), f"Expected (0, 1, 0), got {chandrayaan_test2.position}"
    assert chandrayaan_test2.direction == "D", f"Expected D, got {chandrayaan_test2.direction}"
    print("Test 2 passed!")

if __name__ == "__main__":
    test()