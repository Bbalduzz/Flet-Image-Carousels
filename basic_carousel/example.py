import flet as ft
from manual_carousel import BasicCarousel

def main(page: ft.Page):
    images = [
		('https://images.unsplash.com/photo-1676049938043-def72f6b3cae?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2340&q=80','image description 1'),
		('https://images.unsplash.com/photo-1676085272653-5e77875eed3d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2342&q=80','image description 2'),
		('https://images.unsplash.com/photo-1676044980901-bf50cc624273?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1745&q=80', 'image description 3'),

	]
    carousel = BasicCarousel(images, [ft.AnimationCurve.EASE_IN, ft.AnimationCurve.EASE_IN_OUT_CUBIC_EMPHASIZED], descriptive=True)
    page.add(carousel)

ft.app(target=main)