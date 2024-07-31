import glfw
from OpenGL.GL import *
import numpy as np

def main():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "OpenGL Triangle", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Define the vertex data for the triangle
    vertices = np.array([
        [0.0,  0.5, 0.0],  # Top vertex
        [-0.5, -0.5, 0.0],  # Bottom left vertex
        [0.5, -0.5, 0.0]   # Bottom right vertex
    ], dtype=np.float32)

    # Create a Vertex Buffer Object (VBO) to hold the vertices
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    # Create and compile the vertex shader
    vertex_shader_source = """
    #version 330 core
    layout(location = 0) in vec3 position;
    void main()
    {
        gl_Position = vec4(position, 1.0);
    }
    """
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, vertex_shader_source)
    glCompileShader(vertex_shader)

    # Check for vertex shader compilation errors
    if not glGetShaderiv(vertex_shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex_shader)
        print(f"Vertex Shader compilation failed with error: {error}")
        return

    # Create and compile the fragment shader
    fragment_shader_source = """
    #version 330 core
    out vec4 color;
    void main()
    {
        color = vec4(1.0, 1.0, 1.0, 1.0);  // White color
    }
    """
    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, fragment_shader_source)
    glCompileShader(fragment_shader)

    # Check for fragment shader compilation errors
    if not glGetShaderiv(fragment_shader, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(fragment_shader)
        print(f"Fragment Shader compilation failed with error: {error}")
        return

    # Link the vertex and fragment shader into a shader program
    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, fragment_shader)
    glLinkProgram(shader_program)

    # Check for linking errors
    if not glGetProgramiv(shader_program, GL_LINK_STATUS):
        error = glGetProgramInfoLog(shader_program)
        print(f"Shader Program linking failed with error: {error}")
        return

    # Delete the shaders as they are linked into our program now and no longer necessary
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    # Specify the layout of the vertex data
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here, e.g. using glClear()
        glClear(GL_COLOR_BUFFER_BIT)

        # Use the shader program and draw the triangle
        glUseProgram(shader_program)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
