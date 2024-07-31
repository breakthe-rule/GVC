import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Rotation angles
angle_x = 0.0
angle_y = 0.0

def cursor_position_callback(window, xpos, ypos):
    global angle_x, angle_y
    width, height = glfw.get_window_size(window)
    
    # Calculate angles based on cursor position
    angle_x = (xpos / width) * 360 - 180  # Map cursor x position to [-180, 180]
    angle_y = -((ypos / height) * 360 - 180)  # Map cursor y position to [-180, 180], flip y-axis

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 640 / 480, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_cube():
    glBegin(GL_QUADS)
    
    # Front face
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    
    # Back face
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    
    # Top face
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    
    # Bottom face
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    
    # Right face
    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    
    # Left face
    glColor3f(0.0, 1.0, 1.0)  # Cyan
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    
    glEnd()

def display():
    global angle_x, angle_y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Apply rotations based on cursor position
    glTranslatef(0.0, 0.0, -6.0)
    glRotatef(angle_x, 0.0, 1.0, 0.0)  # Rotate around y-axis
    glRotatef(angle_y, 1.0, 0.0, 0.0)  # Rotate around x-axis
    
    draw_cube()
    
    glfw.swap_buffers(window)

def main():
    global window

    if not glfw.init():
        raise Exception("GLFW could not be initialized.")

    window = glfw.create_window(640, 480, "Rotate 3D Cube with Cursor", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window could not be created.")

    glfw.make_context_current(window)
    
    # Set the cursor position callback
    glfw.set_cursor_pos_callback(window, cursor_position_callback)
    
    init()

    while not glfw.window_should_close(window):
        display()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
