This project is a simple GUI application built using Flet (a Python framework for building interactive GUI and web applications). The application features a landing page and a profile page with user details, organized into tabs for better structure.

Features:

1. Landing Page (ViewPage)
    a.Displays a lock icon and an informational message.
    b.Includes a button labeled "Check Linkage" to navigate to the profile page.

2. Profile Page (ProfilePage)
    a.Organized into two tabs:
        Personal Profile: Displays user's name, role, email, and mobile number.
        Professional Profile: Displays ongoing project, domain, work experience, and education.
    b.Features a circular image container for the profile picture.
    c.Uses a custom Link class to display read-only fields with consistent styling.

3. Routing
    a.The app supports navigation between pages using routes (/view and /profile).
    b.Default route is set to /profile.
