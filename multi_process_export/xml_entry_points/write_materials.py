"""Script to export a Standard Interface Template materials file."""
# 1. Standard python modules

# 2. Third party modules

# 3. Aquaveo modules

# 4. Local modules


if __name__ == "__main__":
    import os
    from xmsapi.dmi import Query
    from xmsguipy.data.target_type import TargetType
    from standard_interface_template.components.sim_query_helper import SimQueryHelper
    from standard_interface_template.file_io.materials_writer import MaterialsWriter
    from standard_interface_template.mapping.coverage_mapper import CoverageMapper

    query = Query()
    query.get_xms_agent().set_retries(1)
    r = query.get('simulation_name')
    simulation_name = r['simulation_name'][0].get_as_string()
    # SimQueryHelper assumes that the context of the query is already at the simulation's hidden component.
    query.select('StandardInterfaceTemplate#Sim_Manager')

    sim_query_helper = SimQueryHelper(query)
    sim_query_helper.get_geometry(False)
    sim_query_helper.get_materials_coverage()
    sim_query_helper.load_component_feature_ids(query, sim_query_helper.material_component, TargetType.polygon)
    coverage_mapper = CoverageMapper(sim_query_helper, generate_snap=False)
    coverage_mapper.do_map()

    path = os.getcwd()
    base_name = f'{simulation_name}.example_materials'
    file_name = os.path.join(path, base_name)
    writer = MaterialsWriter(file_name=file_name,
                             mat_grid_cells=coverage_mapper.material_comp_id_to_grid_cell_ids,
                             mat_component=sim_query_helper.material_component)
    writer.write()
