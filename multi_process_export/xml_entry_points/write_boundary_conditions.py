"""Script to export a Standard Interface Template boundary conditions file."""
# 1. Standard python modules

# 2. Third party modules

# 3. Aquaveo modules

# 4. Local modules


if __name__ == "__main__":
    import os
    from xmsapi.dmi import Query
    from xmsguipy.data.target_type import TargetType
    from standard_interface_template.components.sim_query_helper import SimQueryHelper
    from standard_interface_template.file_io.boundary_conditions_writer import BoundaryConditionsWriter
    from standard_interface_template.mapping.coverage_mapper import CoverageMapper

    query = Query()
    query.get_xms_agent().set_retries(1)
    r = query.get('simulation_name')
    simulation_name = r['simulation_name'][0].get_as_string()
    query.select('StandardInterfaceTemplate#Sim_Manager')

    sim_query_helper = SimQueryHelper(query)
    sim_query_helper.get_geometry(False)
    sim_query_helper.get_boundary_conditions_coverage()
    sim_query_helper.load_component_feature_ids(query, sim_query_helper.boundary_conditions_component, TargetType.arc)
    coverage_mapper = CoverageMapper(sim_query_helper, generate_snap=False)
    coverage_mapper.do_map()

    path = os.getcwd()
    base_name = f'{simulation_name}.example_boundary'
    file_name = os.path.join(path, base_name)
    writer = BoundaryConditionsWriter(file_name=file_name, arc_to_ids=coverage_mapper.bc_arc_id_to_comp_id,
                                      arc_points=coverage_mapper.bc_arc_id_to_grid_ids,
                                      bc_component=coverage_mapper.bc_component)
    writer.write()
