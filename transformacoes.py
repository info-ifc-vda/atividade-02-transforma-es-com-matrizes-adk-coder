import glfw
import math
from OpenGL.GL import *

#tupla
vertices = (
    (-0.2, -0.2),
    (0.2, -0.2),
    (0.0, 0.2)
)

def init():
    glClearColor(0, 0, 0, 1)
    
def translacao(v, tx, ty):
    novo = []
    for x, y in v:
        novo.append([x+tx, y+ty])
    return novo

def rotacao(v, angulo_graus):
    novo = []
    rad = math.radians(angulo_graus)
    cos_theta = math.cos(rad)
    sin_theta = math.sin(rad)

    for x, y in v:
        x_novo = x * cos_theta - y * sin_theta
        y_novo = x * sin_theta + y * cos_theta
        novo_valor([x_novo, y_novo])
    
    return novo

def reflexao(v, eixo='y'):
    novo[]
    for x, y in v:
        if eixo == 'x':
            novo_valor([x, -y])
        elif eixo == 'y' :
            novo_valor([-x, y])
        else:
            novo_valor([x,y])
    return novo


def render(v):    
    glColor3f(r,g,b):
    glBegin(GL_TRIANGLES)    
    for x, y in v:
        glVertex2f(x,y)                    
    glEnd()
    

def main():
    glfw.init() #inicializa biblioteca glfw
    window = glfw.create_window(800, 600, "Matrizes de Transformação", None, None)
    glfw.make_context_current(window) #cria o contexto
    init()
    v_translado = translacao(vertices, -0.5 , 0.5)
    v_rotacionado = rotacao(vertices, 'x') #pra refletir o eixo x(pra ficar de ponta cabeça)
    while not glfw.window_should_close(window): #roda enquanto não fecha a janela
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.poll_events() #captura eventos
        render(vertices, 1.0, 1.0, 1.0)
        render(v_translado, 1.0, 0.0, 0.0)
        render(v_rotacionado, 0.0, 0.0, 1.0)
        glfw.swap_buffers(window)
    glfw.terminate()
    
if __name__ == "__main__":
    main()