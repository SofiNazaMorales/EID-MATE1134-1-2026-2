from manim import *

class Presentacion(Scene):
    def construct(self):
        titulo = Text("Evaluación Integrada de Desempeño", font_size=32)
        sub = Text("Cálculo Intermedio - Grupo 12", font_size=28, color=BLUE)
        tema = Text("Tema: Sumas inferiores y superiores", font_size=24, color=YELLOW)
        
        grupo_txt = VGroup(titulo, sub, tema).arrange(DOWN, buff=0.5)
        
        self.play(Write(grupo_txt))
        self.wait(2)
        self.play(FadeOut(grupo_txt))

class TeoriaYEjemplo(Scene):
    def construct:
        # Espacio reservado para la escena de Macarena (Teoría y Ejemplo)
        pass

class VisualizacionSumas(Scene):
    def construct(self):
        # Espacio reservado para la escena de Sofía (Visualización en Manim)
        pass

class ConclusionYCierre(Scene):
    def construct(self):
        pregunta = Text("¿Cómo podemos encerrar el valor de una región?", font_size=24, color=BLUE)
        concl = Text("El área real se acota entre las sumas inferiores y superiores.", font_size=22)
        limite = MathTex("\\lim_{n \\to \\infty} S_n = \\int_{0}^{2} (4 - x^2) dx", color=YELLOW)
        
        bloque = VGroup(pregunta, concl, limite).arrange(DOWN, buff=0.6)
        
        self.play(Write(pregunta))
        self.wait(1)
        self.play(Write(concl), Write(limite))
        self.wait(2)
