"""
Compute the total weight of widgets and gizmos
"""

WIDGET_WEIGHT = 0.075
GIZMO_WEIGHT = 0.112

# Get input
num_gizmos = int(input("Enter number of gizmos: "))
num_widgets = int(input("Enter number of widgets: "))

# Compute
total_weight = (num_gizmos * GIZMO_WEIGHT) + (num_widgets * WIDGET_WEIGHT)

# Display
print("Total weight of %d gizmos & %d widgets is %.2f kgs" % \
     (num_gizmos, num_widgets, total_weight))
print("Total weight of {:d} gizmos & {:d} widgets is {:.2f} kgs".format(
    num_gizmos, num_widgets, total_weight))
    