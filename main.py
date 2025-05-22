import multiprocessing
import ifcopenshell
import ifcopenshell.geom


def process_ifc_model(model_path):
    """Processes an IFC model to find intersections, collisions, and clearance issues."""
    print(f"\n--- Processing {model_path} ---")
    model = ifcopenshell.open(model_path)

    all_elements = model.by_type("IfcElement")
    # or get IfcDuctSegment and IfcColumn seperately
    # ducts = model.by_type("IfcDuctSegment")
    # columns = model.by_type("IfcColumn")

    tree = ifcopenshell.geom.tree()
    settings = ifcopenshell.geom.settings()
    iterator = ifcopenshell.geom.iterator(
        settings, model, multiprocessing.cpu_count()
    )

    if iterator.initialize():
        while True:
            tree.add_element(iterator.get())
            if not iterator.next():
                break

    def format_clash_output(clash, clash_type_str):
        element1 = clash.a
        element2 = clash.b
        a_global_id = element1.get_argument(0)
        b_global_id = element2.get_argument(0)
        a_ifc_class = element1.is_a()
        b_ifc_class = element2.is_a()
        distance_meters = clash.distance

        # Convert distance from meters to millimeters
        distance_millimeters = distance_meters * 1000

        return (
            f"{clash_type_str} between {a_ifc_class} {a_global_id}"
            f" and {b_ifc_class} {b_global_id} with distance"
            f" {distance_millimeters:.7f} mm"  # Format distance in mm
        )

    intersections = tree.clash_intersection_many(
        all_elements, all_elements, check_all=True
    )
    print("\n--- Intersections ---")
    for clash in intersections:
        print(format_clash_output(clash, "Intersection"))

    collisions = tree.clash_collision_many(
        all_elements, all_elements, allow_touching=True
    )
    print("\n--- Collisions (allowing touching) ---")
    for clash in collisions:
        print(format_clash_output(clash, "Collision"))

    clearances = tree.clash_clearance_many(
        all_elements, all_elements, clearance=0.01
    )
    print("\n--- Clearance Issues (clearance < 0.01) ---")
    for clash in clearances:
        print(format_clash_output(clash, "ClearanceIssue"))


def main():
    print(f"ifcopenshell version: {ifcopenshell.version}")

    # Define the models to process
    models_to_process = [
        "./column_duct_touching.ifc",
        "./column_duct_collision.ifc",
    ]

    for model_path in models_to_process:
        process_ifc_model(model_path)


if __name__ == "__main__":
    main()
