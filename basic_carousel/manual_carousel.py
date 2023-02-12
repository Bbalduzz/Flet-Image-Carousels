import flet as ft
import threading

class BasicCarousel(ft.UserControl):
    def __init__(self, images_list:list, animations:list, descriptive=False):
        self.current_image_index = 0
        self.number_of_items = len(images_list)
        super().__init__()
        self.descriptive = descriptive
        self.images_list = images_list
        self.animation_in = animations[0]
        self.animation_out = animations[1]
        self.carousel = self.build_carousel()

    def build_carousel(self):
        def next_image(e):
            self.current_image_index += 1
            if self.current_image_index not in range(self.number_of_items):
                self.current_image_index = 0
            carousel_row.content.controls = None
            contents_to_append = ft.Column([
                                    ft.Container(
                                        ft.Image(src=self.images_list[self.current_image_index][0],fit=ft.ImageFit.FILL,border_radius=ft.border_radius.all(5)),
                                        width=600,
                                        height=400,
                                        )
                                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            if self.descriptive == True:
                contents_to_append.controls.append(ft.Text(self.images_list[self.current_image_index][1]))
            carousel_row.content.controls.append(contents_to_append)
            self.update()
        def prev_image(e):
            self.current_image_index -= 1
            if self.current_image_index not in range(self.number_of_items):
                self.current_image_index = self.number_of_items-1
            carousel_row.content.controls = None
            contents_to_append = ft.Column([
                        ft.Container(
                            ft.Image(src=self.images_list[self.current_image_index][0],fit=ft.ImageFit.FILL,border_radius=ft.border_radius.all(5)),
                            width=600,
                            height=400,
                            )
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            if self.descriptive == True:
                contents_to_append.controls.append(ft.Text(self.images_list[self.current_image_index][1]))
            carousel_row.content.controls.append(contents_to_append)
            self.update()

        carousel_row = ft.AnimatedSwitcher(
                ft.Row([]),
                transition=ft.AnimatedSwitcherTransition.FADE,
                duration=500,
                reverse_duration=500,
                switch_in_curve=self.animation_in,
                switch_out_curve=self.animation_out,
            )
        ## default values ##
        contents_to_append = ft.Column([
                ft.Container(
                    ft.Image(src=self.images_list[self.current_image_index][0],fit=ft.ImageFit.FILL,border_radius=ft.border_radius.all(5)),
                    width=600,
                    height=400,
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        if self.descriptive == True:
            contents_to_append.controls.append(ft.Text(self.images_list[self.current_image_index][1]))
        carousel_row.content.controls.append(contents_to_append)
        ## carousel + commands ##
        carousel = ft.Row([
            ft.Container(
                ft.FloatingActionButton(icon=ft.icons.NAVIGATE_BEFORE_ROUNDED, bgcolor=ft.colors.TRANSPARENT, shape=ft.CircleBorder(), on_click=prev_image),
                margin=10,
                padding=10,
                alignment=ft.alignment.center_right,
                border_radius=10,
                visible = True,
                disabled=False
            ),
            carousel_row,
            ft.Container(
                    ft.FloatingActionButton(icon=ft.icons.NAVIGATE_NEXT_ROUNDED, bgcolor=ft.colors.TRANSPARENT, shape=ft.CircleBorder(), on_click=next_image),
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center_left,
                    border_radius=10,
                    visible = True,
                    disabled=False
                ),
        ])
        return carousel
    
    def build(self):
        return self.carousel