import flet as ft

#link style dictionary
link_style = {
    "height": 50,
    "focused_border_color": "#BED754",
    "border_radius": 10,
    "cursor_height": 20,
    "cursor_color": "white",
    "content_padding": 10,
    "border_width": 1.5,
    "text_size": 14,
    "label_style": ft.TextStyle(color = "#BED754")
}

#define a link class
class Link(ft.TextField):
    def __init__(self, label: str, value: str, page: ft.page):
        super().__init__(
            hint_text = value,
            label = label,
            read_only = True,
            **link_style
        )

        self.page = page

#define a profile page
class ProfilePage(ft.View):
    def __init__(self, page: ft.page):
        super().__init__(route = "/profile", padding = 20)

        self.page = page

        self.controls = [
            ft.SafeArea(
                expand =True,
                content = ft.Column(
                    horizontal_alignment = "center",
                    controls = [
                        ft.Tabs(
                            selected_index = 1,
                            animation_duration = 300,
                            tabs = [
                                ft.Tab(
                                    tab_content = ft.Text("Personal Profile"),
                                    content = ft.Column(
                                        horizontal_alignment = "center",
                                        controls = [
                                            ft.Divider(height = 20, color = "transparent"),
                                            ft.Container(
                                            bgcolor = "white70",
                                            width = 130,
                                            height = 130,
                                            shape = ft.BoxShape("circle"),

                                            #Define image for rpofile
                                            image_src = "/home/kpit/Downloads/kpit.png",
                                            image_fit = "cover",
                                            shadow = ft.BoxShadow(
                                                spread_radius = 6,
                                                blur_radius = 20,
                                                color = ft.colors.with_opacity(0.71,"black")
                                                )
                                            ),
                                            ft.Divider(height = 20, color = "transparent"),
                                            ft.Text(value = "Profile Page", size = 32, text_align = "center"),
                                            ft.Text(value = "Python Programming | Flet | GUI & Web Apps", weight = "w700", text_align = "center"),
                                            ft.Divider(height = 50, color = "transparent"),
                                            ft.Column(
                                                spacing = 20,
                                                controls = [
                                                Link("Name", "Profile Name", self.page),
                                                Link("Role", "Developer", self.page),
                                                Link("Email", "example@gmail.com", self.page),
                                                Link("Mobile No.","xxxxxx9578", self.page)
                                                ]
                                            )                                                                                      
                                        ]
                                    )
                                ),
                                ft.Tab(
                                    tab_content = ft.Text("Professional Profile"),
                                    content = ft.Column(
                                        horizontal_alignment = "center",
                                        controls = [
                                            ft.Divider(height = 20, color = "transparent"),
                                            ft.Text(value = "Preformance Rating", size = 32, text_align = "center"),
                                            ft.Text(value = "APR 2023 - MAR 2024\nKBA rating: 4.4", weight = "w700", text_align = "center"),
                                            ft.Divider(height = 50, color = "transparent"),
                                            ft.Column(
                                                spacing = 20,
                                                controls = [
                                                Link("OnGoing Project", "Machine Vision Extension", self.page),
                                                Link("Domain", "Development/UI/DevOps", self.page),
                                                Link("Work Experince", "0", self.page),
                                                Link("Education","B.Tech/BCA/Dipolma", self.page)
                                                ]
                                            )                                                                                                                                  
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            )
        ]


#Define a starting view page
class ViewPage(ft.View):
    def __init__(self, page: ft.page):
        super().__init__(route = "/view", padding = 60)

        self.page = page

        #creating lock icon
        self.lock = ft.Icon(
            name = "lock",
            scale = ft.Scale(4)
        )

        #creating button to route to main/profile page
        self.routebutton = ft.Container(
            border_radius = 5,
            expand = True,
            bgcolor = "#F4CE14",
            content = ft.Text(value = "Check Linkage", color = "black", size = 18, text_align = "center"),
            padding = ft.padding.only(left=25,right=25,top=10,bottom=10),
            alignment = ft.alignment.center,
            on_click = None
        )

        self.controls = [
            ft.SafeArea(
                expand = True,
                content = ft.Column(
                    alignment = "SPACEBETWEEN",
                    controls = [
                        ft.Column(
                            controls = [
                                ft.Divider(height = 120, color = "transparent"),
                                self.lock,
                                ft.Divider(height = 120, color = "transparent"),
                                ft.Text("Link management involves organizing,tracking and optimizing URLs for effective online presence.",
                                size = 18, text_align = "center", color = "white70")
                            ],
                            horizontal_alignment = "center",
                        ),
                        ft.Row(
                            controls = [
                                self.routebutton
                            ],
                            alignment = "center"
                        )
                    ]
                )
            )
        ]

def main(page: ft.page):

    page.theme_mode = ft.ThemeMode.DARK

    #method to handle page routing
    def router(route):
        page.views.clear()

        if page.route == "/view":
            landing = ViewPage(page)
            page.views.append(landing)
        
        if page.route == "/profile":
            profile = ProfilePage(page)
            page.views.append(profile)
        
        page.update()

    page.on_route_change = router
    #page.go("/view")
    page.go("/profile") 


if __name__ == "__main__":
    ft.app(target = main)