# incubyte
# Chandrayaan 3 Command Execution

This program is designed to simulate the movement of Chandrayaan 3 in the galaxy using given command instructions.

## Structure:

### 1. Command Class
Represents a movement command with specified movement coordinates and a direction to face.

```python
class Command:
    def __init__(self, movement, direction):
        self.movement = movement
        self.direction = direction
```

### 2. Chandrayaan Class
Represents the Chandrayaan 3 entity. It can execute given commands, keeping track of its current position and direction.

```python
class Chandrayaan:
    def __init__(self):
        self.position = (0, 0, 0)
        self.direction = 'N'

    def execute_command(self, cmd: Command):
        self.position = tuple(sum(x) for x in zip(self.position, cmd.movement))
        self.direction = cmd.direction
```

### 3. Test Function
A suite of test cases to validate the program's correctness. 

```python
def test():
    ...
    print("Test 1 passed!")
    ...
    print("Test 2 passed!")
```
