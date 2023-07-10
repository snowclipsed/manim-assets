from manim import *
import random

class GraphPoints(Scene):

    def construct(self):
        axes= Axes(x_range = [0, 21, 2], 
                   y_range = [0, 21, 2], 
                   x_length = 8,
                   y_length = 6,
                   axis_config = {"include_tip" : True, "numbers_to_exclude": [0]}).add_coordinates()
        #axes.to_edge(UR)
        axes.scale(0.9)

        dot_radius = 0.05
        dots_A = VGroup()
        dots_B = VGroup()
        cluster_1_color = RED
        cluster_2_color = BLUE

        dataset_A = [
            (2, 4, 0), (3, 5, 0), (1, 4, 0), (4, 5, 0), (5, 4, 0),
            (9, 2, 0), (8, 1, 0), (7, 3, 0), (10, 1, 0), (6, 2, 0)
        ]
        
        dataset_B = [
            (12, 14, 0), (11, 13, 0), (10, 15, 0), (13, 12, 0), (9, 11, 0),
            (17, 10, 0), (15, 9, 0), (16, 11, 0), (18, 9, 0), (14, 10, 0)
        ]

        for point in dataset_A:
            x, y, _ = point
            dot = Dot(point=axes.c2p(x,y,0), color=cluster_1_color, radius=dot_radius)
            dots_A.add(dot)  # Add the dot to the group

        for point in dataset_B:
            x, y, _ = point
            dot = Dot(point=axes.c2p(x,y,0), color=cluster_2_color, radius=dot_radius)
            dots_B.add(dot)  # Add the dot to the group            
        
        graph1 = axes.plot(lambda x : -x/3 + 10,
                          color = YELLOW_D
                          )
        graph2 = axes.plot(lambda x : -x/4 + 8,
                          color = TEAL_C
                          )

        graph3 = axes.plot(lambda x : -x/2 + 11,
                          color = PURPLE_C
                          )
        text = Tex("Class A", "Class B").scale(0.5)
        quesText = Tex("Let's plot two classes").scale(0.5)

        animations = [
            DrawBorderThenFill(axes),
            FadeIn(dots_A, target_position = axes.c2p(0,0,0)),
            FadeIn(text[0].next_to(dots_A)),
            FadeIn(dots_B, target_position = axes.c2p(0,0,0)),
            FadeIn(text[1].next_to(dots_B)),
            FadeIn(quesText[0].next_to(axes, UP)),
            #Write(graph1),
            #Write(graph2),
            #Write(graph3),
        ]
        
        self.play(AnimationGroup(*animations, lag_ratio=0.8))
        #self.play(ReplacementTransform(quesText[0], Tex("Class A and B").next_to(axes, UP).scale(0.5)))
        self.wait(2)
        #self.play(
            #FadeOut(graph2),
            #FadeOut(graph3)
        #    )
        #self.wait(3)


class GraphSVM(Scene):

    def construct(self):
        axes= Axes(x_range = [0, 21, 2], 
                   y_range = [0, 21, 2], 
                   x_length = 8,
                   y_length = 6,
                   axis_config = {"include_tip" : True, "numbers_to_exclude": [0]}).add_coordinates()
        #axes.to_edge(UR)
        axes.scale(0.9)

        dot_radius = 0.05
        dots_A = VGroup()
        dots_B = VGroup()
        cluster_1_color = RED
        cluster_2_color = BLUE

        dataset_A = [
            (2, 4, 0), (3, 5, 0), (1, 4, 0), (4, 5, 0), (5, 4, 0),
            (9, 2, 0), (8, 1, 0), (7, 3, 0), (10, 1, 0), (6, 2, 0)
        ]
        
        dataset_B = [
            (12, 14, 0), (11, 13, 0), (10, 15, 0), (13, 12, 0), (9, 11, 0),
            (17, 10, 0), (15, 9, 0), (16, 11, 0), (18, 9, 0), (14, 10, 0)
        ]

        for point in dataset_A:
            x, y, _ = point
            dot = Dot(point=axes.c2p(x,y,0), color=cluster_1_color, radius=dot_radius)
            dots_A.add(dot)  # Add the dot to the group

        for point in dataset_B:
            x, y, _ = point
            dot = Dot(point=axes.c2p(x,y,0), color=cluster_2_color, radius=dot_radius)
            dots_B.add(dot)  # Add the dot to the group            
        
        graph1 = axes.plot(lambda x : -x/3 + 10,
                          color = YELLOW_D
                          )
        graph2 = axes.plot(lambda x : -x/4 + 8,
                          color = TEAL_C
                          )

        graph3 = axes.plot(lambda x : -x/2 + 11,
                          color = PURPLE_C
                          )
        text = Tex("Class A", "Class B").scale(0.5)
        quesText = Tex("Say we wanna divide the two groups with a line..").scale(0.5)

        animations = [
            DrawBorderThenFill(axes),
            FadeIn(dots_A, target_position = axes.c2p(0,0,0)),
            FadeIn(text[0].next_to(dots_A)),
            FadeIn(dots_B, target_position = axes.c2p(0,0,0)),
            FadeIn(text[1].next_to(dots_B)),
            FadeIn(quesText[0].next_to(axes, UP)),
            Write(graph1),
            Write(graph2),
            Write(graph3),
        ]
        
        self.play(AnimationGroup(*animations, lag_ratio=0.8))
        self.play(ReplacementTransform(quesText[0], Tex("Which one is the most optimal line?").next_to(axes, UP).scale(0.5)))
        self.wait(2)
        self.play(
            FadeOut(graph2),
            FadeOut(graph3)
            )
        self.wait(3)