## Experiments with IfcOpenShell and the bvh tree clash detection

### Output for example files
    ifcopenshell version: 0.8.2
    
    --- Processing ./column_duct_touching.ifc ---
    
    --- Intersections ---
    
    --- Collisions (allowing touching) ---
    Collision between IfcColumn 1wQY3jDRvEB8H0b7wCIytt and IfcDuctSegment 3PunUxjrPFIxoU519bU8In with distance 0.0000000 mm
    Collision between IfcWall 0NjhZFH8v4VuBULXb8CzCv and IfcWall 2KCh$j0rD8SguzpTlV_KuZ with distance 0.0000000 mm
    Collision between IfcWall 2KCh$j0rD8SguzpTlV_KuZ and IfcDuctSegment 3PunUxjrPFIxoU519bU8In with distance 0.0000000 mm
    
    --- Clearance Issues (clearance < 0.01) ---
    ClearanceIssue between IfcColumn 1wQY3jDRvEB8H0b7wCIytt and IfcSlab 0tXY6Lyu98CenDKNYMQ6Li with distance 0.0001222 mm
    ClearanceIssue between IfcColumn 1wQY3jDRvEB8H0b7wCIytt and IfcDuctSegment 3PunUxjrPFIxoU519bU8In with distance 0.0000316 mm
    ClearanceIssue between IfcSlab 0tXY6Lyu98CenDKNYMQ6Li and IfcWall 0NjhZFH8v4VuBULXb8CzCv with distance 0.0000030 mm
    ClearanceIssue between IfcSlab 0tXY6Lyu98CenDKNYMQ6Li and IfcWall 2KCh$j0rD8SguzpTlV_KuZ with distance 0.0000030 mm
    ClearanceIssue between IfcWall 0NjhZFH8v4VuBULXb8CzCv and IfcWall 2KCh$j0rD8SguzpTlV_KuZ with distance 0.0000000 mm
    ClearanceIssue between IfcWall 2KCh$j0rD8SguzpTlV_KuZ and IfcDuctSegment 3PunUxjrPFIxoU519bU8In with distance 0.0011979 mm
    
    --- Processing ./column_duct_collision.ifc ---
    
    --- Intersections ---
    Intersection between IfcDuctSegment 3PunUxjrPFIxoU519bU8In and IfcColumn 1wQY3jDRvEB8H0b7wCIytt with distance 500.0000000 mm
    
    --- Collisions (allowing touching) ---
    Collision between IfcColumn 1wQY3jDRvEB8H0b7wCIytt and IfcDuctSegment 3PunUxjrPFIxoU519bU8In with distance 0.0000000 mm
    Collision between IfcWall 0NjhZFH8v4VuBULXb8CzCv and IfcWall 2KCh$j0rD8SguzpTlV_KuZ with distance 0.0000000 mm
    Collision between IfcWall 2KCh$j0rD8SguzpTlV_KuZ and IfcDuctSegment 3PunUxjrPFIxoU519bU8In with distance 0.0000000 mm
    
    --- Clearance Issues (clearance < 0.01) ---
    ClearanceIssue between IfcColumn 1wQY3jDRvEB8H0b7wCIytt and IfcSlab 0tXY6Lyu98CenDKNYMQ6Li with distance 0.0001222 mm
    ClearanceIssue between IfcColumn 1wQY3jDRvEB8H0b7wCIytt and IfcDuctSegment 3PunUxjrPFIxoU519bU8In with distance 8.8885150 mm
    ClearanceIssue between IfcSlab 0tXY6Lyu98CenDKNYMQ6Li and IfcWall 0NjhZFH8v4VuBULXb8CzCv with distance 0.0000030 mm
    ClearanceIssue between IfcSlab 0tXY6Lyu98CenDKNYMQ6Li and IfcWall 2KCh$j0rD8SguzpTlV_KuZ with distance 0.0000030 mm
    ClearanceIssue between IfcWall 0NjhZFH8v4VuBULXb8CzCv and IfcWall 2KCh$j0rD8SguzpTlV_KuZ with distance 0.0000000 mm
    ClearanceIssue between IfcWall 2KCh$j0rD8SguzpTlV_KuZ and IfcDuctSegment 3PunUxjrPFIxoU519bU8In with distance 0.0017218 mm
