class dumbo_octopus():
    def __init__(self,energy_level,x,y):
        self.energy_level = energy_level
        self.__flashing = False
        self.__flashed = False
        self.x = x
        self.y = y
        
    def increase_energy(self):
        if not self.__flashing and not self.__flashed:
            self.energy_level += 1
            if self.energy_level > 9:
                self.energy_level = 0
                self.__flashing = True

    def flashing(self):
        x = False

        if self.__flashing and not self.__flashed:
            self.__flashing = False
            self.__flashed = True
            x = True
            
        return x

    def flashed(self):
        return self.__flashed

    def reset(self):
        self.__flashing = False
        self.__flashed = False
  
octopus_grid = [[ dumbo_octopus( int(y),i2,i1) for i2, y in enumerate(x)] for i1, x in enumerate(open('input.txt').read().split('\n'))]

def print_octopus():
    for x in octopus_grid:
        print([y.energy_level for y in x])

def get_neighbors(x,y):
    neighbors = []
    top = y-1
    right = x+1
    bottom = y+1
    left = x-1
    row_len = len(octopus_grid[y])
    col_height = len(octopus_grid)
    # Top
    if top >= 0:
        neighbors.append(octopus_grid[top][x])
    # Top right
    if top >= 0 and right < row_len:
        neighbors.append(octopus_grid[top][right])
    # Right 
    if right < row_len:
        neighbors.append(octopus_grid[y][right])
    # Bottom right
    if bottom < col_height and right < row_len:
        neighbors.append(octopus_grid[bottom][right])
    # Bottom
    if bottom < col_height:
        neighbors.append(octopus_grid[bottom][x])
    # Bottom left 
    if bottom < col_height and left >= 0:
        neighbors.append(octopus_grid[bottom][left])
    # Left
    if left >= 0:
        neighbors.append(octopus_grid[y][left])
    # Top left
    if top >= 0 and left >=0:
        neighbors.append(octopus_grid[top][left])

    return neighbors

def increase_energy(x,y):
    # Increnent energy
    octopus_grid[y][x].increase_energy()

def flash(x,y):
    flashed = False
    if octopus_grid[y][x].flashing():
        flashed  = True
        for z in get_neighbors(x, y):
            increase_energy(z.x,z.y)            
    return flashed

flashes = 0
step = 1
sync_flash_step = 0
# print_octopus()
while True:

    # Increase energy levels
    for y,row in enumerate(octopus_grid):
        for x,cell in enumerate(row):
            increase_energy(x,y)

    # Flash Octopus
    while True:
        new_flashes = False
        for y,row in enumerate(octopus_grid):
            for x,cell in enumerate(row):
                if flash(x,y):
                    new_flashes = True 
        
        if not new_flashes:
            break
        
    # Count flashes in current step
    current_count = 0
    for y,row in enumerate(octopus_grid):
        for x,cell in enumerate(row):
            if cell.energy_level == 0:
                current_count += 1

    # Accumulate flashes up to 100 steps
    if step < 100:
        flashes += current_count

    # Check of all are flashing
    if current_count == 100:
        sync_flash_step = step
        break

    # Reset flashed octopus
    for y,row in enumerate(octopus_grid):
        for x,cell in enumerate(row):
            cell.reset()

    step += 1

print("Flashes after 100 steps:",flashes)
print("Sync flash step:",sync_flash_step)