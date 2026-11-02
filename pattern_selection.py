import turtle
from tkinter import END


def distance_to_line(px, py, x1, y1, x2, y2):
    """Calculate the shortest distance from a point to a line segment."""

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return ((px - x1) ** 2 + (py - y1) ** 2) ** 0.5

    t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)

    # Keep the closest point within the line segment.
    t = max(0, min(1, t))

    closest_x = x1 + t * dx
    closest_y = y1 + t * dy

    return ((px - closest_x) ** 2 + (py - closest_y) ** 2) ** 0.5


def point_inside_polygon(px, py, points):
    """Return True if the point lies inside a closed polygon."""

    if len(points) < 4:
        return False

    inside = False
    j = len(points) - 1

    for i in range(len(points)):
        xi, yi = points[i]
        xj, yj = points[j]

        if (yi > py) != (yj > py):
            intersection_x = (
                (xj - xi) * (py - yi) / (yj - yi) + xi
            )

            if px < intersection_x:
                inside = not inside

        j = i

    return inside


def select_pattern(x, y, patterns, T1):
    """Find the clicked pattern and display its matrix in T1."""

    tolerance = 10

    # Check newer patterns first, since they may overlap older ones.
    for pattern in reversed(patterns):

        matrix = pattern["matrix"]

        # Ignore invalid coordinate rows.
        points = [
            (point[0], point[1])
            for point in matrix
            if len(point) >= 2
        ]

        if len(points) < 2:
            continue

        selected = False

        # 1. Check whether the click is near any line.
        for i in range(len(points) - 1):

            x1, y1 = points[i]
            x2, y2 = points[i + 1]

            distance = distance_to_line(
                x, y, x1, y1, x2, y2
            )

            if distance <= tolerance:
                selected = True
                break

        # 2. If no line was selected, check the shape's interior.
        if not selected:
            if points[0] == points[-1]:
                selected = point_inside_polygon(x, y, points)

        # 3. Display the selected pattern's coordinates.
        if selected:
            T1.delete("1.0", END)

            for point in matrix:
                T1.insert(
                    END,
                    " ".join(str(value) for value in point) + "\n"
                )

            print("Selected pattern:", pattern["id"])
            return pattern

    print("No pattern found at this position.")
    return None


def enable_pattern_selection(screen, patterns, T1):
    """Register mouse-click selection on the Turtle canvas."""

    def handle_click(x, y):
        select_pattern(x, y, patterns, T1)

    screen.onclick(handle_click)