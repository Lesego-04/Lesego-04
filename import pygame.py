# import pygame
# from random import choice

# class Cell:
#     def __init__(self, x, y, thickness):
#         self.x, self.y = x, y
#         self.thickness = thickness
#         self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
#         self.visited = False

# # cell.py
# class Cell:
#     ...
#     # draw grid cell walls
#     def draw(self, sc, tile):
#         x, y = self.x * tile, self.y * tile
#         if self.walls['top']:
#             pygame.draw.line(sc, pygame.Color('darkgreen'), (x, y), (x + tile, y), self.thickness)
#         if self.walls['right']:
#             pygame.draw.line(sc, pygame.Color('darkgreen'), (x + tile, y), (x + tile, y + tile), self.thickness)
#         if self.walls['bottom']:
#             pygame.draw.line(sc, pygame.Color('darkgreen'), (x + tile, y + tile), (x , y + tile), self.thickness)
#         if self.walls['left']:
#             pygame.draw.line(sc, pygame.Color('darkgreen'), (x, y + tile), (x, y), self.thickness)




# # cell.py

# class Cell:
#     ...
#     # checks if cell does exist and returns it if it does
#     def check_cell(self, x, y, cols, rows, grid_cells):
#         find_index = lambda x, y: x + y * cols
#         if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
#             return False
#         return grid_cells[find_index(x, y)]

#     # checking cell neighbors of current cell if visited (carved) or not
#     def check_neighbors(self, cols, rows, grid_cells):
#         neighbors = []
#         top = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
#         right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)
#         bottom = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
#         left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)
#         if top and not top.visited:
#             neighbors.append(top)
#         if right and not right.visited:
#             neighbors.append(right)
#         if bottom and not bottom.visited:
#             neighbors.append(bottom)
#         if left and not left.visited:
#             neighbors.append(left)
#         return choice(neighbors) if neighbors else False



# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}


from collections import deque

def bfs(graph, start):
    visited = set()         # To keep track of visited vertices
    queue = deque([start])  # Initialize the queue with the starting vertex

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

# Example usage
start_vertex = 'A'
print(f"BFS starting from vertex {start_vertex}:")
bfs(graph, start_vertex)



import pygame
from random import choice

def create_cell(x, y, thickness):
    cell = {
        'x': x,
        'y': y,
        'thickness': thickness,
        'walls': {'top': True, 'right': True, 'bottom': True, 'left': True},
        'visited': False
    }
    return cell

# Example of creating a cell
x_coordinate = 10
y_coordinate = 20
cell_thickness = 5

new_cell = create_cell(x_coordinate, y_coordinate, cell_thickness)


