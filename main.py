from manim import *

class Presentacion(Scene):
    def construct(self):
        # TAREA BENJAMÍN: Textos iniciales, nombres de los integrantes y tema
        titulo = Text("Evaluación Integrada de Desempeño", font_size=32)
        sub = Text("Cálculo Intermedio - Grupo 12", font_size=28, color=BLUE)
        tema = Text("Tema: Sumas inferiores y superiores", font_size=24, color=YELLOW)
        
        grupo_txt = VGroup(titulo, sub, tema).arrange(DOWN, buff=0.5)
        
        self.play(Write(grupo_txt))
        self.wait(2)
        self.play(FadeOut(grupo_txt))

class TeoriaYEjemplo(Scene):
    def construct(self):
        # Espacio para la teoría y el ejemplo de Macarena
        # f(x) = 4 - x^2 en [0, 2]
        texto_teoria = Text("Concepto: Aproximación por sumas de Riemann", font_size=26, color=BLUE)
        funcion_tex = MathTex("f(x) = 4 - x^2, \\quad x \\in [0, 2]", color=WHITE)
        
        bloque_teoria = VGroup(texto_teoria, funcion_tex).arrange(DOWN, buff=0.6)
        
        self.play(Write(bloque_teoria))
        self.wait(2)
        self.play(FadeOut(bloque_teoria))

class VisualizacionSumas(Scene):
    def construct(self):
        # Animación principal de Sofía integrada
        ejes = Axes(
            x_range=[-0.5, 3, 0.5],
            y_range=[-1, 5, 1],
            axis_config={"include_numbers": True}
        )

        curva = ejes.plot(lambda x: 4 - x**2, x_range=[0, 2], color=BLUE)
        etiqueta = ejes.get_graph_label(curva, label="f(x) = 4 - x^2", x_val=1.5, direction=UR)

        self.play(Create(ejes))
        self.play(Create(curva), Write(etiqueta))
        self.wait(1)

        valores_n = [4, 8, 16, 32]

        # Sumas inferiores (evaluación por la derecha)
        rects_inf = VGroup()
        for n in valores_n:
            dx = 2 / n
            nuevos_rects = ejes.get_riemann_rectangles(
                curva, x_range=[0, 2], dx=dx, input_sample_type="right", color=RED, fill_opacity=0.5
            )
            if n == 4:
                self.play(Create(nuevos_rects))
                rects_inf = nuevos_rects
            else:
                self.play(Transform(rects_inf, nuevos_rects))
            self.wait(1)
            
        self.play(FadeOut(rects_inf))
        self.wait(0.5)

        # Sumas superiores (evaluación por la izquierda)
        rects_sup = VGroup()
        for n in valores_n:
            dx = 2 / n
            nuevos_rects = ejes.get_riemann_rectangles(
                curva, x_range=[0, 2], dx=dx, input_sample_type="left", color=GREEN, fill_opacity=0.5
            )
            if n == 4:
                self.play(Create(nuevos_rects))
                rects_sup = nuevos_rects
            else:
                self.play(Transform(rects_sup, nuevos_rects))
            self.wait(1)

        self.wait(2)

class ConclusionYCierre(Scene):
    def construct(self):
        # TAREA BENJAMÍN: Respuesta a la pregunta central y cierre
        pregunta = Text("¿Cómo podemos encerrar el valor de una región?", font_size=24, color=BLUE)
        concl = Text("El área real se acota entre las sumas inferiores y superiores.", font_size=22)
        limite = MathTex("\\lim_{n \\to \\infty} S_n = \\int_{0}^{2} (4 - x^2) dx", color=YELLOW)
        
        bloque = VGroup(pregunta, concl, limite).arrange(DOWN, buff=0.6)
        
        self.play(Write(pregunta))
        self.wait(1)
        self.play(Write(concl), Write(limite))
        self.wait(2)
